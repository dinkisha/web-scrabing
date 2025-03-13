# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 15:56:40 2025

@author: Dinka.Buzuna
"""

import requests

from bs4 import BeautifulSoup

url='https://www.amazon.com/s?k=seller&crid=OZR43049XKSH&sprefix=seller%2Caps%2C1203&ref=nb_sb_noss_1'

r=requests.get(url)

pg=BeautifulSoup(r.text,'lxml')

import re

price=pg.find_all('span',class_ =re.compile('a-size-base a-color-base a-text-bold'))

pg