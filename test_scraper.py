import scraper
import pandas as pd


class TestScraper:

    def test_scraping(self):
        assert isinstance(scraper.parse_and_get_df('tt0903747'), pd.DataFrame)

    def test_mp(self):
        assert isinstance(scraper.main_df(['tt0903747', 'tt4158110']), list)