FROM python:3.9.10
ARG DIR=/code

WORKDIR $DIR

RUN apt update

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .