<h1 align="center">Welcome to tweet-extractor-2 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0-blue.svg?cacheSeconds=2592000" />
</p>

# Twitter Sentiment Analysis System

## Overview

This project is a microservices-based Twitter sentiment analysis system. It fetches tweets, performs lexical and semantic analysis, and provides an API to interact with the data. The architecture ensures scalability, maintainability, and separation of concerns.

## Architecture

```
+------------------+         +--------------------+         +---------------------+
|                  |         |                    |         |                     |
|   Frontend App   | <-----> |    API Gateway     | <-----> |  Data Extraction    |
|  (React/Vue.js)  |         | (Django + DRF)     |         |     Service         |
|                  |         |                    |         | (Tweepy + Celery)   |
+------------------+         +--------------------+         +---------------------+
                                      |                               |
                                      |                               |
                                      v                               v
                           +--------------------+         +---------------------+
                           |                    |         |                     |
                           |      MongoDB       | <-----> | Data Processing     |
                           |                    |         |     Service         |
                           +--------------------+         | (spaCy + TextBlob + |
                                                          |    Celery)          |
                                                          +---------------------+
```

## Folder Structure

```
project_root/
│
├── api_gateway/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   └── urls.py
│   ├── api_gateway/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── celery.py
│   ├── manage.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── data_extraction/
│   ├── data_extraction.py
│   ├── celery.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── data_processing/
│   ├── data_processing.py
│   ├── celery.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── docker-compose.yml
└── .env
```

## Compatibility Check

### API Gateway (Django + DRF)

-   Django >= 4.0
-   Djongo compatible with Django >= 3.2
-   MongoDB >= 4.0
-   Celery >= 5.0
-   Redis >= 5.0

### Data Extraction Service

-   Tweepy >= 4.0 (Compatible with Python >= 3.6)
-   Pymongo
-   Celery
-   Redis

### Data Processing Service

-   TextBlob >= 0.15 (Compatible with Python >= 3.6)
-   spaCy >= 3.0
-   en_core_web_sm model compatible with spaCy >= 3.0
-   Celery
-   Redis

## Step-by-Step Setup Instructions

### MongoDB Setup

1. **Docker Compose Configuration for MongoDB**:

    - Add a service for MongoDB in `docker-compose.yml`.

2. **Run Docker Compose**:
    - Run `docker-compose up -d db` to start the MongoDB service.

### API Gateway Microservice

1. **Create Django Project for API Gateway**:

    - Use `django-admin startproject api_gateway` and `cd api_gateway`.
    - Create a Django app with `django-admin startapp api`.

2. **Configure `settings.py` for API Gateway**:

    - Update `INSTALLED_APPS` to include `rest_framework` and `api`.
    - Configure the `DATABASES` setting to use Djongo with MongoDB.
    - Set Celery configurations.

3. **Define Models, Serializers, and Views**:

    - Define `Tweet` and `UserProfile` models.
    - Create serializers for the models.
    - Implement viewsets for the models.

4. **Create `Dockerfile` for API Gateway**:

    - Create a Dockerfile to build the API Gateway service.

5. **Create `requirements.txt` for API Gateway**:
    - List dependencies: Django, djangorestframework, djongo, pymongo, celery, redis.

### Data Extraction Microservice

1. **Create a Python Script for Data Extraction**:

    - Implement a script to fetch tweets using Tweepy and store them in MongoDB.
    - Use Celery for task scheduling.

2. **Create `Dockerfile` for Data Extraction Service**:

    - Create a Dockerfile to build the Data Extraction service.

3. **Create `requirements.txt` for Data Extraction Service**:
    - List dependencies: tweepy, pymongo, celery, redis.

### Data Processing Microservice

1. **Create a Python Script for Data Processing**:

    - Implement a script to perform semantic analysis on tweets using spaCy and TextBlob.
    - Use Celery for task scheduling.

2. **Create `Dockerfile` for Data Processing Service**:

    - Create a Dockerfile to build the Data Processing service.

3. **Create `requirements.txt` for Data Processing Service**:
    - List dependencies: pymongo, celery, redis, textblob, spacy.

### Scheduling Tasks

1. **Update `celery.py` to Schedule Tasks**:

    - Configure periodic tasks for data extraction and processing.

2. **Run the Services**:
    - Start the Celery workers and beat scheduler for both data extraction and processing services.

### Docker Compose Configuration

-   Add services for MongoDB, Redis, API Gateway, Data Extraction, and Data Processing in `docker-compose.yml`.

## Summary

This setup ensures a modular, scalable, and maintainable system with the following components:

1. **Frontend Application**: (React/Vue.js) Communicates with the API Gateway.
2. **API Gateway**: (Django + DRF) Handles API requests and interacts with MongoDB.
3. **Data Extraction Service**: (Tweepy + Celery) Fetches tweets from Twitter and stores them in MongoDB.
4. **Data Processing Service**: (spaCy + TextBlob + Celery) Performs semantic analysis and scoring of tweets.
5. **Message Broker**: (Redis) Facilitates task scheduling and communication between services.
6. **Database**: (MongoDB) Stores tweets and user data.

## Author

👤 **Chouaib Boubekeur**

-   Website: thbob2.github.io/thbob2
-   Github: [@thbob2](https://github.com/thbob2)
-   LinkedIn: [@Chouaib-Boubekeur](https://linkedin.com/in/Chouaib-Boubekeur)

## Show your support

Give a ⭐️ if this project helped you!

---

_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_
