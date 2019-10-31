# flask-postgres-base
Minimal flask-app with a postgreSQL database.

## 1. Prerequisites

- Docker

## 2. Build

`$ docker build -t flaskapp:latest .`

## 3. Run

When running the container you will need to set the following environment variables:
- SECRET_KEY

You may also wish to set the following environment variables:
- FLASK_CONFIG
- FLASK_ENV

`$ docker run --name flaskapp -e SECRET_KEY=hardtoguessstring -e FLASK_CONFIG=dev -e FLASK_ENV=development -p 8080:5000 flaskapp:latest`
