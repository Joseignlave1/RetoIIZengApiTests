import unittest
from unittest.mock import patch, Mock
import requests


class TestUsersEndpoints(unittest.TestCase):

    # Endpoint 2 - GET /users
    @patch('requests.get')
    def test_get_users(self, mock_get_data):
        mock_data = {
            "data": [
                {
                    "username": "string",
                    "id": "int",
                    "name": "string",
                    "roles": ["Role"]
                }
            ]
        }

        mock_get_data.return_value = Mock()
        mock_get_data.return_value.json.return_value = mock_data
        mock_get_data.return_value.status_code = 200

        response = requests.get("/users")
        body = response.json()

        self.assertEqual(body, mock_data)

        assert response is not None
        assert response.status_code == 200

    # Endpoint 3 - POST /users
    @patch('requests.post')
    def test_post_user(self, mock_post_data):
        request_body = {
            "name": "string",
            "username": "string",
            "password": "string",
            "roles": ["Role"]
        }

        mock_data = {
            "data": {
                "id": "int",
                "name": "string",
                "roles": ["Role"],
                "username": "string"
            }
        }

        mock_post_data.return_value = Mock()
        mock_post_data.return_value.json.return_value = mock_data
        mock_post_data.return_value.status_code = 201  # o 200 según tu API

        response = requests.post("/users", json=request_body)
        body = response.json()

        self.assertEqual(body, mock_data)

        assert response is not None
        assert response.status_code in (200, 201)

    # Endpoint 4 - GET /users/:id
    @patch('requests.get')
    def test_get_user_by_id(self, mock_get_data):
        user_id = 1

        mock_data = {
            "id": "int",
            "name": "string",
            "roles": ["Role"],
            "username": "string"
        }

        mock_get_data.return_value = Mock()
        mock_get_data.return_value.json.return_value = mock_data
        mock_get_data.return_value.status_code = 200

        response = requests.get(f"/users/{user_id}")
        body = response.json()

        self.assertEqual(body, mock_data)

        assert response is not None
        assert response.status_code == 200

    # Endpoint 5 - PATCH /users/:id
    @patch('requests.patch')
    def test_patch_user(self, mock_patch_data):
        user_id = 1

        patch_body = {
            "name": "string",
            "username": "string",
            "roles": ["Role"]
        }

        mock_data = {
            "data": {
                "id": "int",
                "name": "string",
                "roles": ["Role"],
                "username": "string"
            }
        }

        mock_patch_data.return_value = Mock()
        mock_patch_data.return_value.json.return_value = mock_data
        mock_patch_data.return_value.status_code = 200

        response = requests.patch(f"/users/{user_id}", json=patch_body)
        body = response.json()

        self.assertEqual(body, mock_data)

        assert response is not None
        assert response.status_code == 200

    # Endpoint 6 - PATCH /users/:id (asignar roles)
    @patch('requests.patch')
    def test_patch_user_roles(self, mock_patch_data):
        user_id = 1

        patch_body = {
            "roles": ["Role"]
        }

        mock_data = {
            "data": {
                "id": "int",
                "name": "string",
                "roles": ["Role"],
                "username": "string"
            }
        }

        mock_patch_data.return_value = Mock()
        mock_patch_data.return_value.json.return_value = mock_data
        mock_patch_data.return_value.status_code = 200

        response = requests.patch(f"/users/{user_id}", json=patch_body)
        body = response.json()

        self.assertEqual(body, mock_data)

        assert response is not None
        assert response.status_code == 200

    # Endpoint 7 - DELETE /users/:id
    @patch('requests.delete')
    def test_delete_user(self, mock_delete_data):
        user_id = 1

        mock_data = {
            "deleted": True,
            "id": "int"
        }

        mock_delete_data.return_value = Mock()
        mock_delete_data.return_value.json.return_value = mock_data
        mock_delete_data.return_value.status_code = 200

        response = requests.delete(f"/users/{user_id}")
        body = response.json()

        self.assertEqual(body, mock_data)

        assert response is not None
        assert response.status_code == 200


    # GET /users – error interno
    @patch("requests.get")
    def test_get_users_server_error(self, mock_get):
        mock_get.return_value = Mock(status_code=500)

        response = requests.get("/users")

        assert response is not None
        assert response.status_code == 500

    # POST /users – body inválido
    @patch("requests.post")
    def test_post_user_bad_request(self, mock_post):
        mock_post.return_value = Mock(status_code=400)

        response = requests.post("/users", json={})

        assert response is not None
        assert response.status_code == 400

    # POST /users – username duplicado
    @patch("requests.post")
    def test_post_user_conflict(self, mock_post):
        mock_post.return_value = Mock(status_code=409)

        response = requests.post("/users", json={})

        assert response is not None
        assert response.status_code == 409

    # GET /users/:id – usuario inexistente
    @patch("requests.get")
    def test_get_user_not_found(self, mock_get):
        mock_get.return_value = Mock(status_code=404)

        response = requests.get("/users/999")

        assert response is not None
        assert response.status_code == 404

    # PATCH /users/:id – body inválido
    @patch("requests.patch")
    def test_patch_user_bad_request(self, mock_patch):
        mock_patch.return_value = Mock(status_code=400)

        response = requests.patch("/users/1", json={})

        assert response is not None
        assert response.status_code == 400

    # DELETE /users/:id – usuario inexistente
    @patch("requests.delete")
    def test_delete_user_not_found(self, mock_delete):
        mock_delete.return_value = Mock(status_code=404)

        response = requests.delete("/users/999")

        assert response is not None
        assert response.status_code == 404
