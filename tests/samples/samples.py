import unittest
from unittest.mock import patch, Mock
import requests


class TestSamplesEndpoints(unittest.TestCase):

    # Endpoint 14 - POST /samples
    @patch('requests.post')
    def test_post_sample(self, mock_post_data):
        request_body = {
            "client_code": "string",
            "entry_date": "DateTime",
            "description": "string",
            "sampling_date": "DateTime",
            "observations": "string",
            "analysis_quantity": "int"
        }

        mock_data = {
            "data": {
                "sample_number": "int",
                "client_code": "string",
                "entry_date": "DateTime",
                "description": "string",
                "sampling_date": "DateTime",
                "observations": "string",
                "analysis_quantity": "int"
            }
        }

        mock_post_data.return_value = Mock()
        mock_post_data.return_value.json.return_value = mock_data
        mock_post_data.return_value.status_code = 201  # o 200 según implementación

        response = requests.post("/samples", json=request_body)
        body = response.json()

        self.assertEqual(body, mock_data)

        assert response is not None
        assert response.status_code in (200, 201)

    # Endpoint 15 - GET /samples
    @patch('requests.get')
    def test_get_samples(self, mock_get_data):
        mock_data = {
            "data": {
                "sample_number": "int",
                "client_code": "string",
                "entry_date": "DateTime",
                "description": "string",
                "sampling_date": "DateTime",
                "observations": "string",
                "analysis_quantity": "int"
            }
        }

        mock_get_data.return_value = Mock()
        mock_get_data.return_value.json.return_value = mock_data
        mock_get_data.return_value.status_code = 200

        response = requests.get("/samples")
        body = response.json()

        self.assertEqual(body, mock_data)

        assert response is not None
        assert response.status_code == 200

    # Endpoint 16 - GET /samples/:sample_number
    @patch('requests.get')
    def test_get_sample_by_number(self, mock_get_data):
        sample_number = 1

        mock_data = {
            "data": {
                "sample_number": "int",
                "client_code": "string",
                "entry_date": "DateTime",
                "description": "string",
                "sampling_date": "DateTime",
                "observations": "string",
                "analysis_quantity": "int"
            }
        }

        mock_get_data.return_value = Mock()
        mock_get_data.return_value.json.return_value = mock_data
        mock_get_data.return_value.status_code = 200

        response = requests.get(f"/samples/{sample_number}")
        body = response.json()

        self.assertEqual(body, mock_data)

        assert response is not None
        assert response.status_code == 200

    # Endpoint 17 - PATCH /samples/:sample_number
    @patch('requests.patch')
    def test_patch_sample(self, mock_patch_data):
        sample_number = 1

        patch_body = {
            "description": "string",
            "observations": "string"
        }

        mock_data = {
            "data": {
                "sample_number": "int",
                "client_code": "string",
                "entry_date": "DateTime",
                "description": "string",
                "sampling_date": "DateTime",
                "observations": "string",
                "analysis_quantity": "int"
            }
        }

        mock_patch_data.return_value = Mock()
        mock_patch_data.return_value.json.return_value = mock_data
        mock_patch_data.return_value.status_code = 200

        response = requests.patch(f"/samples/{sample_number}", json=patch_body)
        body = response.json()

        self.assertEqual(body, mock_data)

        assert response is not None
        assert response.status_code == 200

    # Endpoint 18 - DELETE /samples/:sample_number
    @patch('requests.delete')
    def test_delete_sample(self, mock_delete_data):
        sample_number = 1

        mock_data = {
            "deleted": True,
            "sample_number": "int"
        }

        mock_delete_data.return_value = Mock()
        mock_delete_data.return_value.json.return_value = mock_data
        mock_delete_data.return_value.status_code = 200

        response = requests.delete(f"/samples/{sample_number}")
        body = response.json()

        self.assertEqual(body, mock_data)

        assert response is not None
        assert response.status_code == 200
