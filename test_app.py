import unittest

from app import app


class AppTest(unittest.TestCase):
    def test_index(self):
        with app.test_client() as client:
            response = client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_data(as_text=True), "CI/CD test")


if __name__ == "__main__":
    unittest.main()