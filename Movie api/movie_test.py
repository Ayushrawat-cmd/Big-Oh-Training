import mock
import sys
from fastapi.testclient import TestClient
from pathlib import Path
from alchemy_mock.mocking import AlchemyMagicMock
from unittest import TestCase
from main import app


client = TestClient(app)
test_dir = (Path(__file__).parent.parent) / 'server'
sys.path.insert(0, test_dir)

mock_db_session = AlchemyMagicMock()
client = TestClient(app)
def get_mock_session():
    return mock_db_session

class MovieControllerTest(TestCase):
    @mock.patch('utils.db_connection.get_db_session', new=get_mock_session)
    def setup(self):
        from main import app
        
    
    def test_get_movies(self):
        # expected_id = "123"
        # mock_db_session.return_value= { 'id': expected_id }
        
        response = client.get(f'/movies')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),{
        "movies": [
            {
            "name": "ksdsjd",
            "rating": 8.0,
            "image": "124",
            "id": "124"
            },
            {
            "name": "ksdsjd",
            "rating": 5.0,
            "image": "df",
            "id": "123"
            }
        ]
        })
    
    def test_get_movie_exist(self):
        expected_id = "123"
        # mock_db_session.return_value= { 'id': expected_id }
        
        response = client.get(f'/movie?id={expected_id}')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),{
        "movie": {
            "name": "ksdsjd",
            "rating": 5.0,
            "id": "123",
            "image": "df"
        }
        })
        
# def test_read_movie():
        
# test = MovieControllerTest()
# test.test_get_movie_exist()

# client = TestClient(app=app)

