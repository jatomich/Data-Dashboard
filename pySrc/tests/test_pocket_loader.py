import unittest
from unittest.mock import patch, Mock
import requests
import pandas as pd
import json
from pocket_loader import pb_load

class TestPocketLoader(unittest.TestCase):
    @patch('pocket_loader.pd.read_excel')
    @patch('pocket_loader.requests.get')
    @patch('pocket_loader.requests.post')
    def test_pb_load_collection_exists(self, mock_post, mock_get, mock_read_excel):
        # Mock the response for checking collection existence
        mock_get.return_value.status_code = 200

        # Call the pb_load function
        pb_load()

        # Assertions
        mock_read_excel.assert_called_once_with('data/FULLY_COMBINED_DATASET.xlsx')
        mock_get.assert_called_once_with('http://127.0.0.1:8090/api/collections/NetflixIMDb')
        mock_post.assert_not_called()

    @patch('pocket_loader.pd.read_excel')
    @patch('pocket_loader.requests.get')
    @patch('pocket_loader.requests.post')
    def test_pb_load_collection_not_exists(self, mock_post, mock_get, mock_read_excel):
        # Mock the response for checking collection existence
        mock_get.return_value.status_code = 404

        # Mock the response for creating collection
        mock_post.return_value.status_code = 200

        # Call the pb_load function
        pb_load()

        # Assertions
        mock_read_excel.assert_called_once_with('data/FULLY_COMBINED_DATASET.xlsx')
        mock_get.assert_called_once_with('http://127.0.0.1:8090/api/collections/NetflixIMDb')
        mock_post.assert_called_once_with('http://127.0.0.1:8090/api/collections/NetflixIMDb')
        mock_post.assert_called_once_with('http://127.0.0.1:8090/api/NetflixIMDb/records', data=json.dumps(mock_read_excel.return_value.to_dict('records')[0]), headers={'Content-Type': 'application/json'})

if __name__ == '__main__':
    unittest.main()