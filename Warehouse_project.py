# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 10:03:14 2025

@author: Dinka.Buzuna
"""

# 1 remember to import the HTML into python

import requests
from bs4 import BeautifulSoup
urls='https://www.findawarehouse.org/SearchFAW'
p1=requests.get(urls)
s1=BeautifulSoup(p1.text,'lxml')
name=s1.find_all( class_='fw-bold')[1:]

name_list=[]
for i in name:
    j=i.text
    name_list.append(j)
# phone numbers

phone=s1.find_all('h5', class_='fw-samibold')[:10]
phone


phone_list=[]

for i in phone:
    j=i.text
    phone_list.append(j)
    
    
person=s1.find_all('h6', class_='mb-0')    

person

person_list=[]

for i in person:
    j=i.text
    person_list.append(j)
    
import pandas as pd

table=pd.DataFrame({'Company_name':name_list,'phone_numbers':phone_list,'Contact_person':person_list})    

table.head()
table.to_excel("warehose.xlsx")
