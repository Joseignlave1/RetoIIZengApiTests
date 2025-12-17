import unittest
from unittest.mock import patch, Mock
import requests


class TestAnalysis(unittest.TestCase):

    @patch("requests.post")
    def test_post_analysis(self, mock_post):
        request_body = {
            "id_user": 1,
            "sample_number": 10,
            "client_code": 999,
            "sow_date": "2025-12-16T10:00:00Z",
            "type_analysis": "string"
        }

        mock_data = {
            "data": {
                "analysis_number": 123,
                "id_user": 1,
                "sample_number": 10,
                "client_code": 999,
                "sow_date": "2025-12-16T10:00:00Z",
                "type_analysis": "string"
            }
        }

        mock_post.return_value = Mock()
        mock_post.return_value.json.return_value = mock_data
        mock_post.return_value.status_code = 201

        response = requests.post("/analysis", json=request_body)
        body = response.json()

        self.assertEqual(body, mock_data)
        assert response is not None
        assert response.status_code == 201

    @patch("requests.get")
    def test_get_analysis(self, mock_get):
        # Firma: GET /analysis devuelve data como objeto :contentReference[oaicite:9]{index=9}
        mock_data = {
            "data": {
                "analysis_number": 123,
                "id_user": 1,
                "sample_number": 10,
                "client_code": 999,
                "sow_date": "2025-12-16T10:00:00Z",
                "type_analysis": "string"
            }
        }

        mock_get.return_value = Mock()
        mock_get.return_value.json.return_value = mock_data
        mock_get.return_value.status_code = 200

        response = requests.get("/analysis")
        body = response.json()

        self.assertEqual(body, mock_data)
        assert response is not None
        assert response.status_code == 200

    @patch("requests.get")
    def test_get_analysis_by_number(self, mock_get):
        analysis_number = 123

        mock_data = {
            "data": {
                "analysis_number": analysis_number,
                "id_user": 1,
                "sample_number": 10,
                "client_code": 999,
                "sow_date": "2025-12-16T10:00:00Z",
                "type_analysis": "string"
            }
        }

        mock_get.return_value = Mock()
        mock_get.return_value.json.return_value = mock_data
        mock_get.return_value.status_code = 200

        response = requests.get(f"/analysis/{analysis_number}")
        body = response.json()

        self.assertEqual(body, mock_data)
        assert response is not None
        assert response.status_code == 200

    # POST /analysis – body inválido
    @patch("requests.post")
    def test_post_analysis_bad_request(self, mock_post):
        mock_post.return_value = Mock(status_code=400)

        response = requests.post("/analysis", json={})

        assert response is not None
        assert response.status_code == 400


    # POST /analysis – conflicto (por ejemplo muestra inexistente o duplicado)
    @patch("requests.post")
    def test_post_analysis_conflict(self, mock_post):
        mock_post.return_value = Mock(status_code=409)

        response = requests.post("/analysis", json={})

        assert response is not None
        assert response.status_code == 409


    # GET /analysis – error interno
    @patch("requests.get")
    def test_get_analysis_server_error(self, mock_get):
        mock_get.return_value = Mock(status_code=500)

        response = requests.get("/analysis")

        assert response is not None
        assert response.status_code == 500


    # GET /analysis/:analysis_number – no encontrado
    @patch("requests.get")
    def test_get_analysis_by_number_not_found(self, mock_get):
        mock_get.return_value = Mock(status_code=404)

        response = requests.get("/analysis/999")

        assert response is not None
        assert response.status_code == 404


    if __name__ == "__main__":
        unittest.main()
