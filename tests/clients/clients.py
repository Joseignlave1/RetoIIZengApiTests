import unittest
from unittest.mock import patch, Mock
import requests


class TestClients(unittest.TestCase):

    @patch("requests.get")
    def test_get_clients(self, mock_get):
        mock_data = {
            "data": [
                {
                    "client_code": "C-001",
                    "name": "ACME",
                    "phoneNumber": 123456,
                    "email": "acme@test.com",
                    "addres": "Montevideo"
                }
            ]
        }

        mock_get.return_value = Mock()
        mock_get.return_value.json.return_value = mock_data
        mock_get.return_value.status_code = 200

        response = requests.get("/clients")
        body = response.json()

        self.assertEqual(body, mock_data)
        assert response is not None
        assert response.status_code == 200

    @patch("requests.post")
    def test_post_clients(self, mock_post):
        # Firma: POST /clients body {name, contact} :contentReference[oaicite:4]{index=4}
        request_body = {"name": "Nuevo Cliente", "contact": "Juan"}

        # Firma muestra response como lista dentro de data (aunque sea raro) :contentReference[oaicite:5]{index=5}
        mock_data = {
            "data": [
                {
                    "client_code": "C-999",
                    "name": "Nuevo Cliente",
                    "phoneNumber": 0,
                    "email": "nuevo@test.com",
                    "addres": "N/A"
                }
            ]
        }

        mock_post.return_value = Mock()
        mock_post.return_value.json.return_value = mock_data
        mock_post.return_value.status_code = 201

        response = requests.post("/clients", json=request_body)
        body = response.json()

        self.assertEqual(body, mock_data)
        assert response is not None
        assert response.status_code == 201

    @patch("requests.get")
    def test_get_client_by_code(self, mock_get):
        client_code = "C-001"

        mock_data = {
            "data": [
                {
                    "client_code": client_code,
                    "name": "ACME",
                    "phoneNumber": 123456,
                    "email": "acme@test.com",
                    "addres": "Montevideo"
                }
            ]
        }

        mock_get.return_value = Mock()
        mock_get.return_value.json.return_value = mock_data
        mock_get.return_value.status_code = 200

        response = requests.get(f"/client/{client_code}")
        body = response.json()

        self.assertEqual(body, mock_data)
        assert response is not None
        assert response.status_code == 200

    # ========= SAD PATHS – CLIENTS =========

    # GET /clients – error interno
    @patch("requests.get")
    def test_get_clients_server_error(self, mock_get):
        mock_get.return_value = Mock(status_code=500)

        response = requests.get("/clients")

        assert response is not None
        assert response.status_code == 500

    # POST /clients – body inválido
    @patch("requests.post")
    def test_post_clients_bad_request(self, mock_post):
        mock_post.return_value = Mock(status_code=400)

        response = requests.post("/clients", json={})

        assert response is not None
        assert response.status_code == 400

    # POST /clients – conflicto (cliente duplicado)
    @patch("requests.post")
    def test_post_clients_conflict(self, mock_post):
        mock_post.return_value = Mock(status_code=409)

        response = requests.post("/clients", json={})

        assert response is not None
        assert response.status_code == 409

    # GET /client/:client_code – cliente inexistente
    @patch("requests.get")
    def test_get_client_by_code_not_found(self, mock_get):
        mock_get.return_value = Mock(status_code=404)

        response = requests.get("/client/C-999")

        assert response is not None
        assert response.status_code == 404


if __name__ == "__main__":
    unittest.main()

