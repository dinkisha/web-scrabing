# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 14:06:49 2025

@author: Dinka.Buzuna
"""

import requests
import pandas as pd

from bs4 import BeautifulSoup

urlc='https://www.carpages.ca/used-cars/search/?fueltype_id%5B0%5D=3&fueltype_id%5B1%5D=7'

pc=requests.get(urlc, verify=False)

sc=BeautifulSoup(pc.text, 'lxml')

# link, name, price, and color of each car
dfc=pd.DataFrame({'Link':[],'Name':[],'Price':[],'Color':[]})
counter=0
while counter<10:
    posting=sc.find_all('div', class_="t-flex t-gap-6 t-items-start t-p-6")
    for i in posting:
        link=i.find('a', class_='t-flex t-items-start t-w-[130px] t-shrink-0').get('href')
        full_link='https://www.carpages.ca' + link
        name=i.find('h4', class_='hN').text.strip()
        price=i.find('div',class_='t-col-span-full mobile-lg:t-col-span-4').text.strip()
        color=i.find('span',class_='t-text-sm t-font-bold').text
        new_row = pd.DataFrame({'Link': [full_link], 'Name': [name], 'Price': [price], 'Color': [color]})
        dfc = pd.concat([dfc, new_row], ignore_index=True)
    
    next_page=sc.find('a', class_='nextprev').get('href')
    urlc='https://www.carpages.ca'+ next_page
    pc=requests.get(urlc, verify=False)
    
    sc=BeautifulSoup(pc.text, 'lxml')
    counter +=1
