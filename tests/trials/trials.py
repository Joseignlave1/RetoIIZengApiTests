import unittest
from unittest.mock import patch, Mock
import requests


class TestTrialsEndpoints(unittest.TestCase):

    # Endpoint 29 - GET /trials
    @patch('requests.get')
    def test_get_trials(self, mock_get_data):
        mock_data = {
            "data": [
                {
                    "trial_number": "int",
                    "analysis_number": "int",
                    "sample_number": "int",
                    "result_number": "int",
                    "id_role": "int",
                    "id_user": "int",
                    "client_code": "int",
                    "emission_date": "DateTime"
                }
            ]
        }

        mock_get_data.return_value = Mock()
        mock_get_data.return_value.json.return_value = mock_data
        mock_get_data.return_value.status_code = 200

        response = requests.get("/trials")
        body = response.json()

        self.assertEqual(body, mock_data)

        assert response is not None
        assert response.status_code == 200

    # Endpoint 30 - POST /trials
    @patch('requests.post')
    def test_post_trial(self, mock_post_data):
        request_body = {
            "analysis_number": "int",
            "sample_number": "int",
            "result_number": "int",
            "emission_date": "DateTime"
        }

        mock_data = {
            "data": {
                "trial_number": "int",
                "analysis_number": "int",
                "sample_number": "int",
                "result_number": "int",
                "id_role": "int",
                "id_user": "int",
                "client_code": "int",
                "emission_date": "DateTime"
            }
        }

        mock_post_data.return_value = Mock()
        mock_post_data.return_value.json.return_value = mock_data
        mock_post_data.return_value.status_code = 201  # o 200 según API

        response = requests.post("/trials", json=request_body)
        body = response.json()

        self.assertEqual(body, mock_data)

        assert response is not None
        assert response.status_code in (200, 201)

    # Endpoint 31 - GET /trials/:trial_number
    @patch('requests.get')
    def test_get_trial_by_number(self, mock_get_data):
        trial_number = 1

        mock_data = {
            "data": {
                "trial_number": "int",
                "analysis_number": "int",
                "sample_number": "int",
                "result_number": "int",
                "id_role": "int",
                "id_user": "int",
                "client_code": "int",
                "emission_date": "DateTime"
            }
        }

        mock_get_data.return_value = Mock()
        mock_get_data.return_value.json.return_value = mock_data
        mock_get_data.return_value.status_code = 200

        response = requests.get(f"/trials/{trial_number}")
        body = response.json()

        self.assertEqual(body, mock_data)

        assert response is not None
        assert response.status_code == 200

    # Endpoint 32 - PATCH /trials/:trial_number
    @patch('requests.patch')
    def test_patch_trial(self, mock_patch_data):
        trial_number = 1

        patch_body = {
            "emission_date": "DateTime"
        }

        mock_data = {
            "data": {
                "trial_number": "int",
                "analysis_number": "int",
                "sample_number": "int",
                "result_number": "int",
                "id_role": "int",
                "id_user": "int",
                "client_code": "int",
                "emission_date": "DateTime"
            }
        }

        mock_patch_data.return_value = Mock()
        mock_patch_data.return_value.json.return_value = mock_data
        mock_patch_data.return_value.status_code = 200

        response = requests.patch(f"/trials/{trial_number}", json=patch_body)
        body = response.json()

        self.assertEqual(body, mock_data)

        assert response is not None
        assert response.status_code == 200

    # Endpoint 33 - DELETE /trials/:trial_number
    @patch('requests.delete')
    def test_delete_trial(self, mock_delete_data):
        trial_number = 1

        mock_data = {
            "deleted": True,
            "trial_number": "string"
        }

        mock_delete_data.return_value = Mock()
        mock_delete_data.return_value.json.return_value = mock_data
        mock_delete_data.return_value.status_code = 200

        response = requests.delete(f"/trials/{trial_number}")
        body = response.json()

        self.assertEqual(body, mock_data)

        assert response is not None
        assert response.status_code == 200

    # ========= SAD PATHS – TRIALS =========

    # GET /trials – error interno
    @patch("requests.get")
    def test_get_trials_server_error(self, mock_get):
        mock_get.return_value = Mock(status_code=500)

        response = requests.get("/trials")

        assert response is not None
        assert response.status_code == 500

    # POST /trials – body inválido
    @patch("requests.post")
    def test_post_trial_bad_request(self, mock_post):
        mock_post.return_value = Mock(status_code=400)

        response = requests.post("/trials", json={})

        assert response is not None
        assert response.status_code == 400

    # POST /trials – conflicto (relaciones inexistentes)
    @patch("requests.post")
    def test_post_trial_conflict(self, mock_post):
        mock_post.return_value = Mock(status_code=409)

        response = requests.post("/trials", json={})

        assert response is not None
        assert response.status_code == 409

    # GET /trials/:trial_number – no encontrado
    @patch("requests.get")
    def test_get_trial_not_found(self, mock_get):
        mock_get.return_value = Mock(status_code=404)

        response = requests.get("/trials/999")

        assert response is not None
        assert response.status_code == 404

    # PATCH /trials/:trial_number – body inválido
    @patch("requests.patch")
    def test_patch_trial_bad_request(self, mock_patch):
        mock_patch.return_value = Mock(status_code=400)

        response = requests.patch("/trials/1", json={})

        assert response is not None
        assert response.status_code == 400

    # DELETE /trials/:trial_number – no encontrado
    @patch("requests.delete")
    def test_delete_trial_not_found(self, mock_delete):
        mock_delete.return_value = Mock(status_code=404)

        response = requests.delete("/trials/999")

        assert response is not None
        assert response.status_code == 404
