
FROM python:3.9.6-slim


# set work directory
WORKDIR /code

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip

COPY ./requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt



ADD db.sqlite3 /code/


# copy project
COPY . /code/


