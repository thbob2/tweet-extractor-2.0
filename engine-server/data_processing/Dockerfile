FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN python -m spacy download en_core_web_sm

CMD ["celery", "-A", "data_processing", "worker", "--loglevel=info"]
