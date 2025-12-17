import unittest
from unittest.mock import patch, Mock

import requests

class TestLogin(unittest.TestCase):

    @patch("requests.post")
    def test_login_ok(self, mock_post):
        mock_data = {
            "data": {
                "access_token": "jwt",
                "expires_in": 3600,
                "user": {
                    "id": 1,
                    "name": "Admin",
                    "roles": ["Role"]
                }
            }
        }

        mock_post.return_value = Mock()
        mock_post.return_value.json.return_value = mock_data
        mock_post.return_value.status_code = 200

        response = requests.post(
            "/login",
            json={"username": "string", "password": "string"}
        )
        body = response.json()

        self.assertEqual(body, mock_data)
        assert response is not None
        assert response.status_code == 200


if __name__ == "__main__":
    unittest.main()

