FROM python:3.11


WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

COPY ./backend/app /code/app

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

EXPOSE 8080

CMD ["uvicorn", "app.server.app:app", "--host", "0.0.0.0", "--port", "8080"]