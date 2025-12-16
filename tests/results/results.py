import unittest
from unittest.mock import patch, Mock
import requests


class TestResultsEndpoints(unittest.TestCase):

    # Endpoint 24 - POST /results
    @patch('requests.post')
    def test_post_results(self, mock_post_data):
        request_body = {
            "analysis_number": "int",
            "sample_number": "int",
            "id_user": "int",
            "client_code": "int",
            "result_date": "DateTime",
            "result": "string"
        }

        mock_data = {
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

        mock_post_data.return_value = Mock()
        mock_post_data.return_value.json.return_value = mock_data
        mock_post_data.return_value.status_code = 201  # si tu API devuelve 200, cambialo a 200

        response = requests.post("/results", json=request_body)
        body = response.json()

        self.assertEqual(body, mock_data)

        assert response is not None
        assert response.status_code in (200, 201)

    # Endpoint 25 - GET /results
    @patch('requests.get')
    def test_get_results_list(self, mock_get_data):
        mock_data = {
            "data": [
                {
                    "result_number": "int",
                    "analysis_number": "int",
                    "sample_number": "int",
                    "id_user": "int",
                    "client_code": "int",
                    "result_date": "DateTime",
                    "result": "string"
                }
            ]
        }

        mock_get_data.return_value = Mock()
        mock_get_data.return_value.json.return_value = mock_data
        mock_get_data.return_value.status_code = 200

        response = requests.get("/results")
        body = response.json()

        self.assertEqual(body, mock_data)

        assert response is not None
        assert response.status_code == 200

    # Endpoint 26 - GET /results/:result_number
    @patch('requests.get')
    def test_get_result_by_number(self, mock_get_data):
        result_number = 1

        mock_data = {
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

        response = requests.get(f"/results/{result_number}")
        body = response.json()

        self.assertEqual(body, mock_data)

        assert response is not None
        assert response.status_code == 200

    # Endpoint 27 - PATCH /results/:result_number
    @patch('requests.patch')
    def test_patch_result_by_number(self, mock_patch_data):
        result_number = 1

        patch_body = {
            "result": "string",
            "result_date": "DateTime"
        }

        mock_data = {
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

        mock_patch_data.return_value = Mock()
        mock_patch_data.return_value.json.return_value = mock_data
        mock_patch_data.return_value.status_code = 200

        response = requests.patch(f"/results/{result_number}", json=patch_body)
        body = response.json()

        self.assertEqual(body, mock_data)

        assert response is not None
        assert response.status_code == 200

    # Endpoint 28 - DELETE /results/:result_number
    @patch('requests.delete')
    def test_delete_result_by_number(self, mock_delete_data):
        result_number = 1

        mock_data = {
            "data": {
                "deleted": True,
                "analysis_number": "int"
            }
        }

        mock_delete_data.return_value = Mock()
        mock_delete_data.return_value.json.return_value = mock_data
        mock_delete_data.return_value.status_code = 200

        response = requests.delete(f"/results/{result_number}")
        body = response.json()

        self.assertEqual(body, mock_data)

        assert response is not None
        assert response.status_code == 200
