<h1 align="center">Welcome to tweet-extractor-2 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0-blue.svg?cacheSeconds=2592000" />
</p>

> A FULL STACK web application that gather data from twitter and produce lead data

## OverHall Architecture

```sh
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

## Folder structure

```sh


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

## Author

👤 **Chouaib Boubekeur**

-   Website: thbob2.github.io/thbob2
-   Github: [@thbob2](https://github.com/thbob2)
-   LinkedIn: [@Chouaib-Boubekeur](https://linkedin.com/in/Chouaib-Boubekeur)

## Show your support

Give a ⭐️ if this project helped you!

---

_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_
