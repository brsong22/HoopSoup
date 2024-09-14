import argparse
import certifi
import json
import os
import ssl
import urllib.request as request
from urllib.parse import parse_qs, urlparse
from bs4 import BeautifulSoup as bs
from constants.columns import METRICS_CATEGORIES, METRICS_STATS_HEADERS

class BbrefScraper:
    def __init__(self, **kwargs):
        self.base_url = 'https://www.basketball-reference.com/'
        self.ssl = ssl.create_default_context(cafile=certifi.where())
        self.metric_key = kwargs['metric']
        self.start = kwargs['start']
        self.end = kwargs['end']
        self.debug = kwargs['debug']

    def scrape_player_metrics_from_url(self):
        stat_metric = METRICS_CATEGORIES[self.metric_key]['name']

        urls = [{'year': year, 'url': f'{self.base_url}leagues/NBA_{year}_{stat_metric}.html'} for year in range(self.start, self.end+1)]
        for url in urls:
            print(f'fetching from: {url}')
            per_player_stats_html = request.urlopen(url['url'], context=self.ssl).read().decode('utf-8')
            year = url['year']

            if self.debug:
                htmls_dir = f'files/html/{year}'
                if not os.path.exists(htmls_dir):
                    os.makedirs(htmls_dir)
                with open(f'{htmls_dir}/players_{self.metric_key}_{year}.html', 'w') as stats_html:
                    print(f'saving {year} {self.metric_key} html')
                    stats_html.write(per_player_stats_html)
            
            self.__parse_player_data_html(per_player_stats_html, year)

    def scrape_player_metrics_from_html(self):
        files = [{'file': f'files/html/{year}/players_{self.metric_key}_{year}.html', 'year': year} for year in range(self.start, self.end+1)]
        for file in files:
            f = file['file']
            y = file['year']
            try:
                with open(f, 'r') as html_file:
                    print(f'parsing {f} for player data')
                    self.__parse_player_data_html(html_file.read(), y)
            except FileNotFoundError:
                print(f'{f} was not found. skipping')
    
    def __parse_player_data_html(self, html, year: int):
        html_soup = bs(html, 'html.parser')
        metric_identifier = METRICS_CATEGORIES[self.metric_key]['identifier']
        table = html_soup.find(id=f'{metric_identifier}_stats')
        tbody = table.find('tbody')
        rows = tbody.find_all('tr', class_=lambda class_: class_ is None)
        player_stats = []
        for p_row in rows:
            player_name = p_row.find_all('td', attrs={'data-stat': 'name_display'})
            position = p_row.find_all('td', attrs={'data-stat': 'pos'})
            stats = p_row.find_all('td', attrs={'data-stat': lambda stat: stat in METRICS_STATS_HEADERS[self.metric_key]['stats']})
            player_stats.append({
                'name': player_name[0].text,
                'position': position[0].text,
                'stats': {stat.get('data-stat'): float(stat.text) if stat.text else '' for stat in stats}
            })
        if self.debug:
            stats_dir = f'files/stats/{year}'
            if not os.path.exists(stats_dir):
                os.makedirs(stats_dir)
            with open(f'{stats_dir}/{self.metric_key}.json', 'w') as stats_file:
                print(f'saving {year} {self.metric_key} stats json')
                json.dump(player_stats, stats_file)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='args for player stat parsing')
    parser.add_argument('-m', '--metric', type=str, choices=METRICS_CATEGORIES.keys(), required=True, help='metric to grab stats for')
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