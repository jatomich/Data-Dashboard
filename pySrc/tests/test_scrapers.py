import unittest
from unittest.mock import Mock
from bs4 import BeautifulSoup
from webscraper.scrapers import StarScraper

class TestStarScraper(unittest.TestCase):
    def setUp(self):
        self.filename = "data/FULLY_COMBINED_DATASET.xlsx"
        self.webdriver = Mock()
        self.scraper = StarScraper(filename=self.filename, webdriver=self.webdriver)

    def test_make_soup(self):
        # Mock the webdriver's get method to return a mock response
        self.webdriver.get.return_value = Mock(text='<html><body><h1>Test</h1></body></html>')

        # Call the make_soup method
        soup = self.scraper.make_soup('https://www.example.com')

        # Assertions
        self.assertIsInstance(soup, BeautifulSoup)
        self.assertEqual(soup.find('h1').text, 'Test')

    def test_get_url_cast(self):
        # Mock the scraper's df attribute to return a mock DataFrame
        self.scraper.df = Mock()
        self.scraper.df.iloc.return_value.iterrows.return_value = [
            (0, {'tconst': 'tt1234567', 'cast': 'Actor 1, Actor 2'}),
            (1, {'tconst': 'tt2345678', 'cast': 'Actor 3, Actor 4'}),
            (2, {'tconst': 'tt3456789', 'cast': 'Actor 5, Actor 6'})
        ]

        # Call the get_url_cast method
        result = list(self.scraper.get_url_cast())

        # Assertions
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0], ('https://www.imdb.com/title/tt1234567', ['Actor 1', 'Actor 2']))
        self.assertEqual(result[1], ('https://www.imdb.com/title/tt2345678', ['Actor 3', 'Actor 4']))
        self.assertEqual(result[2], ('https://www.imdb.com/title/tt3456789', ['Actor 5', 'Actor 6']))

    def test_write_to_file(self):
        # Mock the scraper's cast_dicts attribute to return a mock list
        self.scraper.cast_dicts = Mock()

        # Call the write_to_file method
        self.scraper.write_to_file()

        # Assertions
        self.scraper.df.to_excel.assert_called_once_with('data/star_info.xlsx', index=False)

if __name__ == '__main__':
    unittest.main()