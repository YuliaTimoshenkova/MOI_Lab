# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 22:07:19 2016
@author: Yulia PC
Функция получения списка статей за пол года
"""
import requests
from bs4 import BeautifulSoup
import datetime

def ArticleList(data, id):
    DateList = list() # список дат за указанный период
    ArticleList = list() # итоговый список ссылок
    UrlList=list() # список ссылок на статьи категории на выбранные даты с указанием необходимых ссылок на статьи
    SecId = "section_id-" + str(id) # указание категории для ссылки   
    # Формируем список всех дат за пол года от текущего дня
    Base = datetime.datetime.today() # текущие дата и время
    i=0
    while i < data:
        Date = (Base - datetime.timedelta(days=i)).strftime("%Y/%m/%d")
        i=i+1
        DateList.append(Date) # Итоговый список дат за выбранный период   
    # Формируем список ссылок на статьи за этот период
    i = len(DateList)-1
    while i >= 0:
        UrlList.append('http://www.e1.ru/news/daily/' + DateList[i] +  '/list-' + SecId + '.html')
        i=i-1
    i=0
    while i < len(UrlList):
        r = requests.get( UrlList[i])
        soup = BeautifulSoup(r.text, 'html.parser')    
        href = (soup.find_all('a',attrs={"class":"news"}))
        i=i+1
        j=0
        while j < len(href):
            if SecId in href[j]['href']:
                ArticleList.append('http://www.e1.ru'+href[j]['href'])
            j=j+1  
    return(ArticleList)