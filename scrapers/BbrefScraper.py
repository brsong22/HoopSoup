import argparse
import certifi
import json
import os
import ssl
import urllib.request as request
from urllib.parse import parse_qs, urlparse
from bs4 import BeautifulSoup as bs

class BbrefScraper:
    def __init__(self, metric):
        self.base_url = 'https://www.basketball-reference.com/'
        self.ssl = ssl.create_default_context(cafile=certifi.where())
        self.metric = metric

    def scrape_player_metrics_per_season_html(self, start: int, end: int):
        stat_metrics = {
            'totals': 'totals',
            'pergame': 'per_game',
            'per36': 'per_minute',
            'per100': 'per_poss',
            'advanced': 'advanced',
            'pbp': 'play-by-play',
            'shooting': 'shooting',
            'adjshooting': 'adj_shooting'
        }

        htmls_dir = f'players_{self.metric}_per_season_html'
        if not os.path.exists(htmls_dir):
            os.mkdir(htmls_dir)

        stat_metric = stat_metrics[self.metric]

        urls = [{'year': year, 'url': f'{self.base_url}leagues/NBA_{year}_{stat_metric}.html'} for year in range(start, end+1)]
        for url in urls:
            print(f'fetching from: {url}')
            per_player_stats_html = request.urlopen(url['url'], context=self.ssl).read().decode('utf-8')
            year = url['year']
            with open(f'{htmls_dir}/players_{self.metric}_{year}.html', 'w') as stats_html:
                stats_html.write(per_player_stats_html)

    def parse_player_data(self):
        return

if __name__ == '__main__':
    scraper = BbrefScraper('pergame')
    scraper.scrape_player_metrics_per_season_html(2020, 2024)