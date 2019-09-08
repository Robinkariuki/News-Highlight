# from app import app c
import urllib.request,json

# import json c
from .models import Source
from .models import Article

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# getting api key c
api_key = None

# getting the news based url c
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
