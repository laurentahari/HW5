import unittest
import requests
import re
from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error

r = urllib.urlopen('https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=All').read()
soup = BeautifulSoup(r)
print (soup)
