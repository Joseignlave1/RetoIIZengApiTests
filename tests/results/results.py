import unittest
from unittest.mock import patch, Mock

import requests
class TestGetResults(unittest.TestCase):
    @patch('requests.get')
    def test_get_results(self, mock_get_data):
        mock_data =  {
          "data": {
            "result_number": "int",
            "analysis_number": "int",
            "sample_number": "int",
            "id_user": "int",
            "client_code": "int",
            "result_date": "DateTime",
            "result": "string"
          }
        }
        mock_get_data.return_value = Mock()

        mock_get_data.return_value.json.return_value = mock_data
        mock_get_data.return_value.status_code = 200

        response = requests.get("/results")
        body = response.json()
        self.assertEqual(body,mock_data)

        assert response is not None
        assert response.status_code == 200
