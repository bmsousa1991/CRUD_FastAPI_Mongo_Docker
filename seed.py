import asyncio
import motor.motor_asyncio
import pandas as pd
import requests
from pymongo.errors import DuplicateKeyError

# Configurações do MongoDB com usuário e senha
mongo_uri = "mongodb://root:password@127.0.0.1:27017"
database_name = "imdb"
collection_name = "movie"

# Caminho do arquivo CSV
csv_file_path = "movie.csv"

# Separador do arquivo CSV
csv_separator = ";"

# URL da API de filmes
api_url = "http://localhost:8080/movie/api/post"

async def read_csv_and_insert_to_mongodb():
    # Conectar ao banco de dados MongoDB
    client = motor.motor_asyncio.AsyncIOMotorClient(mongo_uri)
    db = client[database_name]
    collection = db[collection_name]

    # Ler o arquivo CSV
    df = pd.read_csv(csv_file_path, sep=csv_separator)

    # Remover linhas com valores NaN
    df = df.dropna()

    # Iterar sobre as linhas do DataFrame e enviar dados para a API e MongoDB
    for index, row in df.iterrows():
        movie_data = row.to_dict()

        # Tentar inserir no MongoDB
        try:
            await collection.insert_one(movie_data)
        except DuplicateKeyError:
            print(f"Duplicado: {movie_data['_id']}")

        # Enviar dados para a API
        response = requests.post(api_url, json=movie_data)

        if response.status_code == 200:
            print(f"Filme {movie_data['_id']} inserido com sucesso na API")
        else:
            print(f"Filme {movie_data['_id']} inserido com sucesso na API")

    # Fechar a conexão com o MongoDB
    client.close()

if __name__ == "__main__":
    # Executar a lógica assíncrona
    asyncio.run(read_csv_and_insert_to_mongodb())
