FROM python:3-slim as base
WORKDIR /bot
ENV PYTHONBUFFERED True
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD ['python', 'main.py']