FROM python:3.11-slim
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . .

RUN pip install poetry

RUN poetry install --without=dev


RUN poetry run python manage.py migrate 
RUN poetry run python manage.py collectstatic --noinput 

EXPOSE 80


