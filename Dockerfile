FROM python:3

WORKDIR /hoopsoup/app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
