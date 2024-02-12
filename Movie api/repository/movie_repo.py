from fastapi import Depends
from sqlalchemy.orm import Session

from utils.logger import Logger
from utils.db_connection import get_db_session
from models.movie import Movie as MovieModel
from schema.movie_schema import MovieSchema

logger = Logger.get_logger(__name__)
# print(logger)
class MovieRepository():
    def __init__(self, db_session:Session = Depends(get_db_session)) -> None:
        print("dsad")
        self.db = db_session
    
    def read(self):
        logger.debug(f'Getting all movies from db')
        return self.db.query(MovieModel).all()
    
    def get_by_id(self, id):
        logger.debug(f'Getting movie {id} from db')
        return self.db.query(MovieModel).filter(MovieModel.id == id).first()
    
    def insert(self, movie: MovieSchema):
        '''Inserting the movie in the db'''
        logger.debug(f'Insert movie {movie}')
        db_movie = MovieModel(id = movie.id, name=movie.name, rating = movie.rating, image = movie.image)
        self.db.add(db_movie)
        self.db.commit()
        self.db.refresh(db_movie)

    def delete(self, movieId):
        '''Delete query for the deleting movie from db'''
        db_movie = self.db.query(MovieModel).filter(MovieModel.id == movieId).first()
        # print(db_movie.id)
        if db_movie is None:
            return False
        logger.debug(f'Delete movie {db_movie}')
        self.db.delete(db_movie)
        self.db.commit()
        return True
        # self.db.refresh()

    def update(self, movie: MovieSchema):
        '''Update the movie in the database'''
        logger.debug(f"Update movie {movie}")
        db_movie_query = self.db.query(MovieModel).filter(MovieModel.id == movie.id)
        db_movie = db_movie_query.first()
        if db_movie is None:
            return None
        db_movie.name = movie.name
        db_movie.image = movie.image
        db_movie.rating = movie.rating
        # db_movie_query.update(id = movie.id, name= movie.name)
        self.db.commit()
        self.db.refresh(db_movie)
        return db_movie

        
