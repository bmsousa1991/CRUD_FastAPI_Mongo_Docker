import motor.motor_asyncio
from bson.objectid import ObjectId
import json


MONGO_DETAILS = "mongodb://root:password@mongo:27017"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.imdb
movies_collection = database.get_collection("movie")

def movie_dict(movie) -> dict:
    return {
        "title": movie["title"],
        "year": movie["year"],
        "genre": movie["genre"],
        "rating": movie["rating"],
        "country": movie["country"],
        "director": movie["director"]
    }

def movie_update_dict(movie) -> dict:
    return {
        "title": movie["title"],
        "year": movie["year"],
        "genre": movie["genre"],
        "rating": movie["rating"],
        "country": movie["country"],
        "director": movie["director"]
    }

async def movies_all():
    movies = []
    async for movie in movies_collection.find():
        movies.append(movie_dict(movie))
    return movies

async def get_top10_movies():
    movies = []
    async for movie in movies_collection.find().sort("rating", -1).limit(10):
        movies.append(movie_dict(movie))
    return movies    

async def get_top10_movies_year(year):
    movies = []
    async for movie in movies_collection.find({"year": year}).sort("rating", -1).limit(10):
        movies.append(movie_dict(movie))
    return movies

async def get_top5_movies_country(country):
    movies = []
    async for movie in movies_collection.find({"country": {"$regex": country, "$options": "i"}}).sort("rating", -1).limit(5):
        movies.append(movie_dict(movie))
    return movies

async def add_movie(movie_data: dict) -> dict:
    movie_data["genre"] = json.dumps(movie_data.get("genre", []))
    movie_data["country"] = json.dumps(movie_data.get("country", []))
    movie_data["director"] = json.dumps(movie_data.get("director", []))
    movie = await movies_collection.insert_one(movie_data)
    new_movie = await movies_collection.find_one({"_id": movie.inserted_id})
    return movie_update_dict(new_movie)

async def update_movie(id: str, movie_data: dict):
    movie_data["genre"] = json.dumps(movie_data.get("genre", []))
    movie_data["country"] = json.dumps(movie_data.get("country", []))
    movie_data["director"] = json.dumps(movie_data.get("director", []))
    movie = await movies_collection.update_one({"_id": ObjectId(id)}, {"$set": movie_data})
    return movie_update_dict(movie)

async def delete_movie(id: str):
    movie = await movies_collection.find_one({"_id": ObjectId(id)})
    if movie:
        await movies_collection.delete_one({"_id": ObjectId(id)})
        return True

