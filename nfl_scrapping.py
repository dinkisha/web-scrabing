# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 16:41:24 2025

@author: Dinka.Buzuna
"""




import requests

from bs4 import BeautifulSoup

import pandas as pd

urlnfl='https://www.nfl.com/standings/league/2019/REG'

pnfl=requests.get(urlnfl, verify=False)
 
soupnfl=BeautifulSoup(pnfl.text, 'lxml')
tablenfl=soupnfl.find('table', {'summary':'Standings - Detailed View'})


headersnfl=[]

for i in tablenfl.find_all('th'):
    title=i.text.strip()
    headersnfl.append(title)
    
dfnfl=pd.DataFrame(columns = headersnfl)   

for j in tablenfl.find_all('tr')[1:]:
    first_td=j.find_all('td')[0].find('div', class_='d3-o-club-fullname').text.strip()
    row_data=j.find_all('td')[1:]
    rownfl=[nfl.text.strip("" ) for nfl in row_data]
    rownfl.insert(0,first_td)    
    lennfl=len(dfnfl)
    dfnfl.loc[lennfl]=rownfl



    