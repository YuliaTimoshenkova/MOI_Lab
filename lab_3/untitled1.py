# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 23:04:58 2016

@author: Yulia PC
"""
import requests
from bs4 import BeautifulSoup
import datetime

period = 180
date_list = list()
base = datetime.datetime.today()
i=0
while i < period:
    a= (base - datetime.timedelta(days=i)).strftime("%Y/%m/%d")
    i=i+1
    date_list.append(a)    
    #print(date_list)
    
    #ЛИСТ СТРАНИЦ СО СТАТЬЯМИ ПО КАЛЕНДАРНЫМ ДНЯМ
url_list=list()
i = len(date_list)-1
while i >= 0:
    url_list.append('http://www.e1.ru/news/daily/' + date_list[i] +  '/list-section_id-5.html')
    i=i-1
    
        
    #print(url_list)
     #ВСЕ ССЫЛКИ НА СТАТЬИ ЗА ПОЛ ГОДА
    article_list=list()
    i=0
    while i<len(url_list):
        r = requests.get(url_list[i])
        soup = BeautifulSoup(r.text, 'html.parser')    
        href = (soup.find_all('a',attrs={"class":"news"}))
        i=i+1
        j=0
        while j<len(href):
            if "section_id-148" in href[j]['href']:
                article_list.append('http://www.e1.ru'+href[j]['href'])
            j=j+1  
