from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.database.movie_database import (
    movies_all,
    get_top10_movies,
    get_top10_movies_year,
    get_top5_movies_country,
    add_movie,
    update_movie,
    delete_movie
)
from app.server.models.movie_models import (
    ErrorResponseModel,
    ResponseModel,
    MovieSchema,
    UpdateMovieModel
)

rotas = APIRouter()

@rotas.get("/api/all", response_description="Get a list of all movies")
async def get_all_movies():
    movies = await movies_all()
    if movies:
        return ResponseModel(movies, "Movies successfully returned.")
    return ResponseModel(movies, "Returned empty list")

@rotas.get('/api/top10', response_description="Get top10 movies")
async def get_top_movies():
    movies = await get_top10_movies()
    if movies:
        return ResponseModel(movies, "Returned top10 movies")
    return ResponseModel(movies, "Returned empty list")

@rotas.get("/api/top10/{year}", response_description="Get top10 movies for year")
async def get_top_movies_year(year: int):
    movies = await get_top10_movies_year(year)
    if movies:
        return ResponseModel(movies, "Returned top10 movies for year")
    return ResponseModel(movies, "Returned empty list")

@rotas.get("/api/top5/{country}", response_description="Returned top5 movies for country")
async def get_top_movies_country(country: str):
    movies = await get_top5_movies_country(country)
    if movies:
        return ResponseModel(movies, "Returned top5 movies for country")
    return ResponseModel(movies, "Returned empty list")

@rotas.post("/api/post", response_description="Movie data added into the database")
async def add_movie_database(movie: UpdateMovieModel):
    movie = jsonable_encoder(movie)
    new_movie = await add_movie(movie)
    return ResponseModel(new_movie, "Movie added successfully.")

@rotas.put("/api/put/{id}", response_description="Movie updated into the base")
async def update_movie_data(id: str, movie: UpdateMovieModel):
    movie = jsonable_encoder(movie)
    updated_movie = await update_movie(id, movie)
    return ResponseModel(
            f"Movie with ID: {id} updated successfully")

@rotas.delete("/api/delete/{id}", response_description="Movie deleted from the base")
async def delete_movie_data(id: str):
    deleted = await delete_movie(id)
    if deleted:
        return ResponseModel(f"Movie with ID: {id} deleted successfully")
    else:
        return ResponseModel(f"Movie with ID: {id} not found", status_code=404)
