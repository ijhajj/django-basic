FROM python:3.7-alpine
MAINTAINER Inderpreet Kaur Jhajj

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client

RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev linux-headers postgresql-dev

RUN apk add --no-cache jpeg-dev zlib-dev

RUN apk add --no-cache --virtual .build-deps build-base linux-headers \
    && pip install Pillow

RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps


RUN mkdir /app
WORKDIR /app

COPY ./app /app
RUN adduser -D user
USER user
