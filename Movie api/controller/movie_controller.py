from pathlib import Path
from fastapi_router_controller import Controller
from fastapi import Depends, HTTPException, status, Query
from fastapi.responses import JSONResponse
from typing import Annotated,Optional
from schema.errors import Errors, ErrorModel, throw_error
from environment.Router import movie_router
from schema.movie_schema import MovieSchema
from service.movie_service import MovieService
from utils.logger import Logger
from fastapi.encoders import jsonable_encoder

controller = Controller(movie_router)
logger = Logger.get_logger(__name__)

@controller.use()
@controller.resource()
class MovieController:
    def __init__(self, movieService:MovieService = Depends()) -> None:
        # print("dsfs")
        self.movieService = movieService

    @controller.route.get("", summary="fsfds")
    def getMovieById(self, id:str= None) :
        '''Get movie from the db'''
        try:
            movie = self.movieService.getMovieById(movieId=id)
            if movie is None:
                return Errors.HTTP_404_NOT_FOUND
            return  JSONResponse(status_code=status.HTTP_200_OK, content={"movie": jsonable_encoder(movie)})
        except Exception as error:
            logger.error(f"Error in getting user {error}")
            return throw_error(status= status.HTTP_500_INTERNAL_SERVER_ERROR, message= "Internal Server Error", error_code= 500, error= error)
        

    @controller.route.get("s", summary="fsfds")
    def getAllMovies(self) :
        '''Get all the movies from the db'''
        try:
            movie = self.movieService.getAllMovies()
            if movie is None:
                return Errors.HTTP_404_NOT_FOUND
            return  JSONResponse(status_code=status.HTTP_200_OK, content={"movies": jsonable_encoder(movie)})
        except Exception as error:
            logger.error(f"Error in getting user {error}")
            return throw_error(status= status.HTTP_500_INTERNAL_SERVER_ERROR, message= "Internal Server Error", error_code= 500, error= error)

    
    
    

    @controller.route.post("", summary="fsfds")
    def createMovie(self, new_movie: MovieSchema):
        '''Create movie'''
        try:
            movie = self.movieService.createMovie(new_movie)
            return JSONResponse(status_code=status.HTTP_201_CREATED, content={"message":"Movie created", "movie":jsonable_encoder(new_movie)})
        except Exception as error:
            logger.error(f"Error in creating movie {error}")
            return throw_error(status= status.HTTP_500_INTERNAL_SERVER_ERROR, message= "Internal Server Error", error_code= 500, error= error)
    
    
    @controller.route.put("", responses={
            Errors.HTTP_500_INTERNAL_SERVER_ERROR.status_code: { 
                'model': ErrorModel, 'description': 'Generic Error Occured' }
        })
    async def updateMovie(self, movie: MovieSchema):
        '''Update the movie have the given details.'''
        try:
            updated_movie = self.movieService.updateMovie(movie)
            if updated_movie is None:
                return Errors.HTTP_404_NOT_FOUND
            # item = self.service.insertTask(newItem)
            return JSONResponse(status_code=status.HTTP_200_OK, content={"message":"Movie updated", "movie":jsonable_encoder(updated_movie)})
            # return {"message":"Task created", "task": item}
        except Exception as error:
            logger.error(f'Error insterting task: {error}')
            return throw_error(status= status.HTTP_500_INTERNAL_SERVER_ERROR, message= "Internal Server Error", error_code= 500 , error= error)
    
    @controller.route.delete("/{movie_id}",responses={
            Errors.HTTP_404_NOT_FOUND.status_code: { 'model': ErrorModel, 'description': 'Movie not found on DB' },
            Errors.HTTP_500_INTERNAL_SERVER_ERROR.status_code: { 'model': ErrorModel, 'description': 'Generic Error Occured' }
        })
    async def deleteMovie(self,movie_id: Annotated[int, Path(title="The ID of the item to get")]):
        '''Delete movie is the controller allows us delete movie from the database'''
        try:
            # print(movie_id)
            success = self.movieService.deleteMovie(movie_id)
            if success is not True:
                return Errors.HTTP_404_NOT_FOUND
            return JSONResponse(status_code=status.HTTP_202_ACCEPTED, content={"message":"Movie deleted"}) 
        except Exception as error:
            logger.error(f"Error deleting task: {error}")
            return throw_error(status= status.HTTP_500_INTERNAL_SERVER_ERROR, message= "Internal Server Error", error_code= 500, error= error)
    
    
