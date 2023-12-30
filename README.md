<h1 align='center'> CRUD com Python, FastAPI, MongoDB e Docker </h1>

<img src="https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white"/> <img src="https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=FASTAPI&logoColor=white"/> <img src="https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white"/> <img src="https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white"/>

Projeto em Python utilizando FastAPI, MongoDB e Docker. Nesse projeto crei uma APIREST utilizando uma base de dados com filmes do IMDB.

## Executando a API

1. Clone o repositorio:

```
https://github.com/bmsousa1991/CRUD_FastAPI_Mongo_Docker.git
```

2. Instale o docker-compose e execute o comando no diretório em que você deseja que seu projeto fique:

```
$ docker-compose up -d
```

3. Rode o script seed.py para popular o banco de dados com os filmes contidos no arquivo movie.csv:
   
```
$ python seed.py
```

4. Teste a aplicação:

FastAPI também gerou automaticamente documentação de API totalmente interativa que podemos usar para interagir com nossa API. Podemos visitar http://localhost:8080/docs em nosso navegador para ver a documentação interativa da API fornecida pelo Swagger UI :

![image](https://github.com/bmsousa1991/CRUD_FastAPI_Mongo_Docker/assets/151109415/35a43cdd-c1d2-429a-ac1a-3eb0aa8bc4a6)






