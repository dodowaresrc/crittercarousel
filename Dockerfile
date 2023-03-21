FROM python:3.10-slim-bullseye

RUN apt-get update -y --quiet

RUN apt-get upgrade -y --quiet

RUN apt-get install -y curl gcc

RUN curl -LsS https://r.mariadb.com/downloads/mariadb_repo_setup | bash

RUN apt-get install -y --quiet libmariadb3 libmariadb-dev

WORKDIR /app

COPY crittercarousel ./crittercarousel/

COPY requirements.txt .

RUN python -m venv .venv

RUN .venv/bin/pip install -r requirements.txt --progress-bar off --no-color

EXPOSE 8888

CMD [".venv/bin/python", "-u", "-m", "crittercarousel.api"]
