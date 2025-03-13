# -*- coding: utf-8 -*-
"""
Created on Thu Mar  6 15:22:06 2025

@author: Dinka.Buzuna
"""

import requests
from bs4 import BeautifulSoup

url = 'https://webscraper.io/test-sites/e-commerce/allinone/phones/touch'

requests.get(url)

page=requests.get(url)

soup=BeautifulSoup(page.text, 'lxml')


#find() function

soup.find('header')

soup.find('div',{'class':'container test-site'})

soup.find('h4', {'class':'price float-end pull-right'})

soup.find_all('h4', {'class':'price float-end card-title pull-right'})



soup.find_all('a', class_='title')

# find_all part2

soup.find_all(['h4','p'])

soup.find_all(id=True)

soup.find_all(string='Iphone')

import re

soup.find_all(string=re.compile('Iph'))

soup.find_all(string=re.compile('Nok'))

soup.find_all(class_ =re.compile('pull'))

soup.find_all('p', class_ =re.compile('pull'))

soup.find_all(class_ =re.compile('pull'), limit=3)


# find_all part 3

product_name=soup.find_all('a',class_ =('title'))

product_name

price=soup.find_all('h4',class_=re.compile('pull'))

price

review=soup.find_all('p', class_=re.compile('review-count'))

review

description= soup.find_all('p', class_= re.compile('description'))
description


soup.find('h4', {'class':'price float-end card-title pull-right'}).text

product_list=[]

for i in product_name:
    
    name=i.text
    product_list.append(name)

price_list=[]

for i in price:
    
    name=i.text
    price_list.append(name)

review_list=[]

for i in review:
    
    name=i.text
    review_list.append(name)
    
description_list=[]

for i in description:
    
    name=i.text
    description_list.append(name)    
    
    
import pandas as pd

table=pd.DataFrame({'Product_Name':product_list,'Description':description_list,'Price':price_list,'Reviews':review_list})    
    


# Extracting data from nested html tags
boxes=soup.find_all('div', class_='col-md-4 col-xl-4 col-lg-4')[6]

boxes.find('a').text
boxes.find('p', class_='description').text

box2= soup.find_all('ul', class_='nav',id='side_menu')[0]
box2.find_all('li')

# save it to csv file
table.to_csv("extracted_data.csv")