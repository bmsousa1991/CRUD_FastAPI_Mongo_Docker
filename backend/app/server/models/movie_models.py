from typing import Optional, List
from pydantic import BaseModel

class MovieSchema(BaseModel):
    title: str
    year: int
    genre: List[str]
    rating: float
    country: List[str]
    director: List[str]

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Carandiru",
                "year": 2003,
                "genre": ["Drama", "Crime"],
                "rating": 8.0,
                "country": ["Brazil", "Argentina", "Italy"],      
                "director": ["Hector Babenco"]
            }
        }

class UpdateMovieModel(BaseModel):
    title: Optional[str]
    year: Optional[int]
    genre: Optional[List[str]]
    rating: Optional [float]
    country: Optional[List[str]]
    director: Optional[List[str]]

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Carandiru",
                "year": 2003,
                "genre": ["Drama", "Crime"],
                "rating": 8.0,
                "country": ["Brazil", "Argentina", "Italy"],      
                "director": ["Hector Babenco"]
            }
        }

def ResponseModel(data, message):
    return {
        "data": data,
        "code": 200,
        "message": message,
    }

def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}