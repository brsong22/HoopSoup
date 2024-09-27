import argparse
import certifi
import json
import os
import ssl
from urllib.error import HTTPError, URLError
import urllib.request as request
from dotenv import load_dotenv
from pymongo import MongoClient
from bs4 import BeautifulSoup as bs
from constants.metrics import METRICS_CATEGORIES
from constants.info_defs import GENERAL_INFO, AWARDS_INFO

class BbrefScraper:
    def __init__(self, **kwargs):
        self.base_url = 'https://www.basketball-reference.com/'
        self.ssl = ssl.create_default_context(cafile=certifi.where())
        self.metric_keys = kwargs['metrics']
        self.start = kwargs['start']
        self.end = kwargs['end']
        self.debug = kwargs['debug']
        self.stat_defs = {}

        if not self.debug:
            load_dotenv()
            mongo_user = os.getenv('MONGO_USER')
            mongo_pass = os.getenv('MONGO_PASSWORD')
            mongo_connection = os.getenv('MONGO_CONNECTION_STRING').format(mongo_user=mongo_user, mongo_password=mongo_pass)
            self.mdb = MongoClient(mongo_connection, tls=True, tlsCAFile=certifi.where())

    def scrape_player_metrics_from_url(self):
        for metric in self.metric_keys:
            stat_metric_url = METRICS_CATEGORIES[metric]['url_name']

            urls = [{'year': year, 'url': f'{self.base_url}leagues/NBA_{year}_{stat_metric_url}.html'} for year in range(self.start, self.end+1)]
            for url in urls:
                print(f'fetching from: {url}')
                try:
                    per_player_stats_html = request.urlopen(url['url'], context=self.ssl).read().decode('utf-8')
                    year = url['year']

                    if self.debug:
                        self.save_html_to_file(per_player_stats_html, metric, year)
                    
                    self.__parse_player_data_html(per_player_stats_html, metric, year)
                except HTTPError as e:
                    print(f'HTTPError: {e.code} - {e.reason}')
                except URLError as e:
                    print(f'URLError: {e.reason}')

    def scrape_player_metrics_from_html(self):
        for metric in self.metric_keys:
            files = [{'file': f'files/html/{year}/players_{metric}_{year}.html', 'year': year} for year in range(self.start, self.end+1)]
            for file in files:
                f = file['file']
                y = file['year']
                try:
                    with open(f, 'r') as html_file:
                        print(f'parsing {f} for player data')
                        self.__parse_player_data_html(html_file.read(), metric, y)
                except FileNotFoundError:
                    print(f'{f} was not found. skipping')
    
    def __parse_player_data_html(self, html, metric, year):
        print(f'parsing {year} {metric} stats')
        html_soup = bs(html, 'html.parser')
        metric_table_id = METRICS_CATEGORIES[metric]['table_id']
        table = html_soup.find(id=f'{metric_table_id}')
        if year == self.start:
            self.__build_stat_defs(table.find('thead').find_all('tr')[-1].find_all('th'), metric)
        tbody = table.find('tbody')
        rows = tbody.find_all('tr', class_=lambda class_: class_ is None or class_ == 'full_table')
        player_stats = []
        for idx, p_row in enumerate(rows):
            stats_dict = {'season': year, 'stats': {}}
            row_stats = p_row.find_all(attrs={'data-stat': lambda stat: stat in self.stat_defs[metric]})
            row_infos = p_row.find_all(attrs={'data-stat': lambda info: info in GENERAL_INFO.keys()})
            # stats_dict = {**stats_dict, 'stats': {stat.get('data-stat'): float(stat.text) if self.stat_defs[metric][stat.get('data-stat')]['type'] == 'float' and stat.text != '' else stat.text for stat in stats if stat.get('data-stat') not in general_info_stat_keys}}
            for stat in row_stats:
                stat_id = stat.get('data-stat')
                # if stat_id not in GENERAL_INFO:
                if idx == 0 and year == self.start:
                    try:
                        stat_val = float(stat.text)
                        self.stat_defs[metric][stat_id]['type'] = 'float'
                        # print(f'{stat_id} is TYPE float with VALUE {stat_val}')
                    except (ValueError, TypeError):
                        stat_val = stat.text
                        self.stat_defs[metric][stat_id]['type'] = 'string'
                        # some numeric stats (such as %s) can be empty so maybe we want to flag the type to recheck on later rows if '' value
                        if stat_val == '':
                            self.stat_defs[metric][stat_id]['recheck'] = True
                        # print(f'{stat_id} is TYPE string with VALUE {stat_val}')
                    stats_dict['stats'][stat_id] = stat_val if stat_val != '' else None
                else:
                    stat_type = self.stat_defs[metric][stat_id]['type']
                    type_recheck = self.stat_defs[metric][stat_id].get('recheck')
                    if type_recheck and stat.text != '':
                        try:
                            float(stat.text)
                            self.stat_defs[metric][stat_id]['type'] = 'float'
                            stat_type = 'float'
                        except (ValueError, TypeError):
                            self.stat_defs[metric][stat_id]['recheck'] = False # could maybe just pop this out of dict too
                    # print(f'{stat_id} is TYPE {stat_type} with VALUE {stat.text}')
                    stat_val = None if stat.text == '' else float(stat.text) if stat_type == 'float' else stat.text
                    stats_dict['stats'][stat_id] = stat_val
            for info_stat in row_infos:
                info_id = info_stat.get('data-stat')
                info_val = float(info_stat.text) if GENERAL_INFO[info_id]['type'] == 'float' else info_stat.text if info_id != AWARDS_INFO else info_stat.text.split(',') if info_stat.text != '' else []
                stats_dict[info_stat.get('data-stat')] = info_val
            player_stats.append(stats_dict)

        if year == self.start:
            with open('constants/stat_defs.json', 'w') as stat_def_file:
                print(f'writing stat defs to const file')
                json.dump(self.stat_defs, stat_def_file)
        
        if self.debug:
            self.save_json_to_file(player_stats, metric, year)
        else:
            self.__save_to_db(player_stats, metric)

    def __build_stat_defs(self, stat_headers, metric):
        print(f'building {metric} stat defs')
        self.stat_defs[metric] = {}
        for stat in stat_headers:
            stat_header = stat.get_text()
            stat_id = stat.get('data-stat')
            stat_description = stat.get('data-tip') if stat.get('data-tip') else ''
            if (stat_id not in GENERAL_INFO) and (stat_id != 'DUMMY') and (stat_id != ''):
                self.stat_defs[metric][stat_id] = {
                    'description': stat_description,
                    'display_name': stat_header
                }

    def __save_to_db(self, documents, metric):
        print('saving to db')
        db = self.mdb['per_season_stats']
        collection = db[metric]
        doc_ids = collection.insert_many(documents)
        print(f'saved {len(doc_ids.inserted_ids)} rows')

    def save_html_to_file(self, html, metric, year):
        htmls_dir = f'files/html/{metric}'
        if not os.path.exists(htmls_dir):
            os.makedirs(htmls_dir)
        with open(f'{htmls_dir}/{year}.html', 'w') as stats_html:
            print(f'saving {year} {metric} html')
            stats_html.write(html)
    
    def save_json_to_file(self, stats_json, metric, year):
        stats_dir = f'files/stats/{metric}'
        if not os.path.exists(stats_dir):
            os.makedirs(stats_dir)
        with open(f'{stats_dir}/{year}.json', 'w') as stats_file:
            print(f'saving {year} {metric} stats json')
            json.dump(stats_json, stats_file)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='args for player stat parsing')
    parser.add_argument('-m', '--metrics', choices=list(METRICS_CATEGORIES.keys()), default=list(METRICS_CATEGORIES.keys()), nargs='*', help='metric to grab stats for. omit for all stat metrics')
    parser.add_argument('-s', '--start', type=int, required=True, help="start year to get stats for")
    parser.add_argument('-e', '--end', type=int, required=True, help="end year to get stats for")
    parser.add_argument('--debug', action='store_true', help='save html files and player stats. skips saving to db')
    parser.add_argument('--source', type=str, choices=['url', 'html'], default='html', help='get player data from url (bball-ref) or saved html files (from debug)')

    print(parser.parse_args())
    kwargs = vars(parser.parse_args())
    scraper = BbrefScraper(**kwargs)
    if kwargs['source'] == 'url':
        scraper.scrape_player_metrics_from_url()
    else:
        scraper.scrape_player_metrics_from_html()