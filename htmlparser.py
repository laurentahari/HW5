from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import requests
import unittest
import re

import urllib.request, urllib.parse, urllib.error
import re
base_url = 'https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=All'
requests.get(base_url, headers={'User-Agent': 'SI_CLASS'})
html = urllib.request.urlopen(base_url).read()
soup = BeautifulSoup(html, 'html.parser')
