FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND=noninteractive

USER root  
WORKDIR /app

COPY requirements.txt /app
RUN pip install -r /app/requirements.txt
COPY . /app
USER root  


EXPOSE 8095
ENTRYPOINT uvicorn main:app --host 0.0.0.0 --port 8095