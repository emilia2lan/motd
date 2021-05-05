# syntax=docker/dockerfile:1

FROM python:3.8.10-buster
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
CMD [ "python", "app.py"]