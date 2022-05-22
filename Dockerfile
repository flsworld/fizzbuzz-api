FROM python:3.9

WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

RUN pip install jupyter

# Detect changes in this file and use the cache for the next step if possible
COPY requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . .

CMD uvicorn src.fizzbuzz:app --reload --host 0.0.0.0 --port 8000
