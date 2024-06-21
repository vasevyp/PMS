# syntax=docker/dockerfile:1
# pull official base image

# FROM spartakode/sqlite3
# FROM python:3.9.6-alpine
FROM python

# пакеты сборки, необходимые для успешной установки numpy и pandas на Alpine для контейнера.
# RUN apk add --no-cache --update \
#   python3 python3-dev gcc \
#   gfortran musl-dev g++ \
#   libffi-dev openssl-dev \
#   libxml2 libxml2-dev \
#   libxslt libxslt-dev \
#   libjpeg-turbo-dev zlib-dev



# set work directory
WORKDIR /code

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
# RUN pip install --upgrade cython 
COPY ./requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt


ADD db.sqlite3 /code/


# copy project
COPY . /code/


