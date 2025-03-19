# -*- coding: utf-8 -*-
"""
Created on Fri Mar 14 14:02:39 2025

@author: Dinka.Buzuna
"""

import requests

from bs4 import BeautifulSoup

import pandas as pd


arib_url='https://www.airbnb.com/s/Hull--Massachusetts--United-States/homes?refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&price_filter_input_type=0&channel=EXPLORE&place_id=ChIJcc-mjOFl44kRu7ipItTGkxY&acp_id=7c43c235-27ff-41c3-8b9e-5f627b26b100&date_picker_type=calendar&checkin=2025-03-18&checkout=2025-03-19&source=structured_search_input_header&search_type=autocomplete_click&query=Hull%2C%20Massachusetts%2C%20United%20States&monthly_start_date=2025-04-01&monthly_length=3&monthly_end_date=2025-07-01&search_mode=regular_search&price_filter_num_nights=1&federated_search_session_id=8f8fbf36-36c2-4796-a9d0-afcfd39fb832'

arib_p=requests.get(arib_url)

arib_soup=BeautifulSoup(arib_p.text, 'lxml')

df_arib=pd.DataFrame(columns={'Link':[''],'Hotel_Name':[''],'Price':[''],'Rating':[''],'Details':['']})


while True:
    try:
        posting=arib_soup.find_all('div', class_='_is5jnq')
        for i in posting:
            data=i.find_all('a',{'data-testid':'card-container'}).get(href)
            link='https://www.airbnb.com/'+ data
            
            
            name=i.find_all({'data-testid':'listing-card-name'}).text
            price=i.find_all(class_='_tt122m').text
            rating=i.find_all('div', class_='t1a9j9y7 atm_da_1ko3t4y atm_dm_kb7nvz atm_fg_h9n0ih dir dir-ltr').text
            detalis=i.find_all({'data-testid':'listing-card-subtitle'}).text
            
            df_arib=df_arib.append({'Link':link,'Hotel_Name':name,'Price':price,'Details':detalis,'Rating':rating}, ingore_index=True)
        
        
    except:
         pass
    
    next_page=arib_soup.find('a',{'aaria-label':'Next page'}).get(href)
    next_page_full_url='https://www.airbnb.com/'+ next_page
    
    arib_p=requests.get(next_page_full_url)

    arib_soup=BeautifulSoup(arib_p.text, 'lxml')

