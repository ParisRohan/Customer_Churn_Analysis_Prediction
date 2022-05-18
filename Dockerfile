# syntax=docker/dockerfile:1

FROM python:3.7.13-slim-buster

WORKDIR /customer-churn-docker

COPY requirements.txt requirements.txt
RUN apt-get update
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]