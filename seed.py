import asyncio
import motor.motor_asyncio
import pandas as pd
import requests
from pymongo.errors import DuplicateKeyError

mongo_uri = "mongodb://root:password@127.0.0.1:27017"
database_name = "imdb"
collection_name = "movie"
csv_file_path = "movie.csv"
csv_separator = ";"
api_url = "http://localhost:8080/movie/api/post"

async def read_csv_and_insert_to_mongodb():
    client = motor.motor_asyncio.AsyncIOMotorClient(mongo_uri)
    db = client[database_name]
    collection = db[collection_name]

    df = pd.read_csv(csv_file_path, sep=csv_separator)
    df = df.dropna()

    for index, row in df.iterrows():
        movie_data = row.to_dict()

        try:
            await collection.insert_one(movie_data)
        except DuplicateKeyError:
            print(f"Duplicado: {movie_data['_id']}")

        response = requests.post(api_url, json=movie_data)

        if response.status_code == 200:
            print(f"Filme {movie_data['_id']} inserido com sucesso na API")
        else:
            print(f"Filme {movie_data['_id']} inserido com sucesso na API")

    client.close()

if __name__ == "__main__":
    asyncio.run(read_csv_and_insert_to_mongodb())
