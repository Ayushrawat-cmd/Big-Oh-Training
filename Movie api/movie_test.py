import mock
import sys
from fastapi.testclient import TestClient
from pathlib import Path
from alchemy_mock.mocking import AlchemyMagicMock, UnifiedAlchemyMagicMock
from unittest import TestCase
from main import app



test_dir = (Path(__file__).parent.parent) / 'server'
sys.path.insert(0, test_dir)

mock_db_session = UnifiedAlchemyMagicMock()
client = TestClient(app)
def get_mock_session():
    return mock_db_session

class MovieControllerTest(TestCase):
    client = TestClient(app)
    @mock.patch('utils.db_connection.get_db_session', new=get_mock_session)
    def setup(self):
        from main import app
        # self.client = TestClient(app)
    
    def test_get_movies(self):
        '''Get all the movie testcase'''
        # expected_id = "123"
        # mock_db_session.return_value= { 'id': expected_id }
        
        response = self.client.get(f'/movies')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),{
  "movies": [
    {
      "name": "ksdsjd",
      "rating": 5.0,
      "id": "124",
      "image": "df"
    },
    {
      "name": "ksdsjd",
      "rating": 5.0,
      "id": "123",
      "image": "df"
    }
  ]
})
    
    def test_get_movie_exist(self):
        '''Test is the movie exist in the db'''
        expected_id = "123"
        
        response = self.client.get(f'/movie?id={expected_id}')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),{
        "movie": {
            "name": "ksdsjd",
            "rating": 5.0,
            "id": "123",
            "image": "df"
        }
        })
    
    def test_moviecreate_success(self):
        '''Is the movie create success or not'''
        insert_movie = {
        "id":"127",
        "name":"ksdsjd",
        "rating":5,
        "image":"df"
        }
        response = self.client.post('/movie', json=insert_movie)
        self.assertEqual(response.status_code,201)
        self.assertEqual(response.json(), {
        "message": "Movie created",
        "movie": {
            "id": "127",
            "name": "ksdsjd",
            "rating": 5,
            "image": "df"
        }
        })        

    def test_moviedelete_success(self):
        '''Delete movie is success or not'''
        expected_id = "127"
        response = self.client.delete(f'/movie/{expected_id}')
        self.assertEqual(response.status_code,202 )
        self.assertEqual(response.json(), {
        "message": "Movie deleted"
        })
    
    def test_rating(self):
        '''Check the rating of the new movie which is inserting'''
        insert_movie = {
        "id":"127",
        "name":"ksdsjd",
        "rating":11,
        "image":"df"
        }
        response = self.client.post('/movie', json=insert_movie)
        self.assertEqual(response.status_code,400)
        self.assertEqual(response.json()["error"],"body Value error, Rating should not be less than 1 or greater than 10")        
    
# def test_read_movie():
        
# test = MovieControllerTest()
# test.test_get_movie_exist()

# client = TestClient(app=app)

