from fastapi import Depends
from schema.movie_schema import MovieSchema
from utils.logger import Logger
from repository.movie_repo import MovieRepository
# from Models.item import Item

logger = Logger.get_logger(__name__)

class MovieService():
    def __init__(self, repository: MovieRepository = Depends()) -> None:
        self.repository = repository
    
    def getMovieById(self, movieId):
        '''Get the movie by the id'''
        return self.repository.get_by_id(movieId)

    def getAllMovies(self):
        '''Get all the movies from the db'''
        logger.debug("Getting all movies from db")
        return self.repository.read()
    
    def createMovie(self, new_movie: MovieSchema):
        '''Create movie in the db'''
        logger.debug(f'Insert new-movie {new_movie}')
        self.repository.insert(new_movie)

    def updateMovie(self, movie:MovieSchema):
        '''update movie in the db'''
        logger.debug(f'Update movie {movie}')
        return self.repository.update(movie)

    def deleteMovie(self, oldMovieID):
        '''delete movie from the db'''
        # print(oldMovieID)
        return self.repository.delete(oldMovieID)

    
    # def addTask(self,userId:int, task:Item):
    #     if userId not in self.__users :
    #         return None
    #     self.__users[userId].task.append(task)
    #     return self.__users[userId]
    
    
