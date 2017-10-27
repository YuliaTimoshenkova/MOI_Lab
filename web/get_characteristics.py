# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 22:19:16 2016

@author: Yulia PC
"""

import requests
from bs4 import BeautifulSoup


def get_characteristics(url):
    article_url = url
    r = requests.get(article_url)
    soup = BeautifulSoup(r.text, 'html.parser')
    get_characteristics_list = list()
    # Слова в заголовке
    titleTag = soup.html.head.title.string
    WordsInTitle = len(titleTag.split())
    
    get_characteristics_list.append(WordsInTitle)
    # Слова в статье
    AllText = soup.html.body.get_text()
    WordsInArticle = len(AllText.split())
    
    # Слова в подзаглоовке 
    descriptionTag = soup.html.meta.get('content')
    WordsInDescription = len(descriptionTag.split())
    
    # Количество изображений в статье
    countImage = soup.html.body.find_all('img')
    ImagesNumber = len(countImage)
       
    # Количество ссылок на другие новости e1.ru
    countLink = soup.find_all('a', {"class":"news"})
    LinksNumber = len(countLink)
       
    # Количество просмотров
    ViewNumber = int(soup.find_all('strong', {"class":"small_black"})[1].string)
    # Выделение количества комментариев
    text = soup.get_text()
    i1 = text.find('просмотров:')
    i2 = text.find('версия для печати')
    fragment = text[i1:i2-3]
    # Выделение количества комментариев
    if (fragment.find('(') == -1):
        CommentsNumber = 0
    else:
        CommentsNumber = int(soup.find_all('strong', {"class":"small_black"})[2].string[:-1][2:])
 
    # Категория статьи 
    Categories = 12
    Categories12 = [WordsInTitle, WordsInArticle, WordsInDescription, 
           ImagesNumber, LinksNumber, ViewNumber, CommentsNumber, Categories]
    
    return(Categories12)
    