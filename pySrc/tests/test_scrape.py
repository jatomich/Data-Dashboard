import unittest
from unittest.mock import patch
from webscraper import scrape

class TestScrape(unittest.TestCase):
    @patch('builtins.input', return_value='data/FULLY_COMBINED_DATASET.xlsx')
    @patch('builtins.print')
    def test_scrape_successful(self, mock_print):
        # Call the scrape function
        scrape()

        # Assertions
        mock_print.assert_called_once_with("Scraping complete.")

    @patch('builtins.input', return_value='data/FULLY_COMBINED_DATASET.xlsx')
    @patch('builtins.print')
    def test_scrape_failed(self, mock_print):
        # Mock the scrape_star_data method to return False
        with patch('webscraper.scrapers.StarScraper.scrape_star_data', return_value=False):
            # Call the scrape function
            scrape()

            # Assertions
            mock_print.assert_called_once_with("Scraping failed.")

if __name__ == '__main__':
    unittest.main()