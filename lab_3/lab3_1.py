# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 21:27:25 2016

@author: Yulia PC

Раздел - Эксклюзив (12)
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Задаем ссылку на статью, которую нужно распарсить
article_url = 'http://www.e1.ru/news/spool/news_id-453561-section_id-1.html'
# article_url = 'http://www.e1.ru/news/spool/news_id-449488.html'
r = requests.get(article_url)
soup = BeautifulSoup(r.text, 'html.parser')

# Задание 1 расчет параметров статьи
# Слова в заголовке
titleTag = soup.html.head.title.string
WordsInTitle = len(titleTag.split())
print('Количество слов в загловке: ', WordsInTitle)  

# Слова в статье
AllText = soup.html.body.get_text()
WordsInArticle = len(AllText.split())
print('Количество слов в статье: ', WordsInArticle)

# Слова в подзаглоовке 
descriptionTag = soup.html.meta.get('content')
WordsInDescription = len(descriptionTag.split())
print('Количество слов в теге description: ', WordsInDescription)

# Количество изображений в статье
countImage = soup.html.body.find_all('img')
ImagesNumber = len(countImage)
print('Количество изображений в статье: ',ImagesNumber)

# Количество ссылок на другие новости e1.ru
countLink = soup.find_all('a', {"class":"news"})
LinksNumber = len(countLink)
print('Количество ссылок на другие новости e1.ru: ',LinksNumber)

# Количество просмотров
ViewNumber = soup.find_all('strong', {"class":"small_black"})[1].string
print('Количество просмотров: ', ViewNumber)
# Выделение количества комментариев
ViewNumber = soup.find_all('strong', {"class":"small_black"})[2].string[:-1][2:]
print('Количество коментариев: ', CommentsNumber)
# Категория статьи 
Categories = 12
Categories12 = [Categories, WordsInTitle, WordsInArticle, WordsInDescription, 
       ImagesNumber, LinksNumber, ViewNumber, CommentsNumber]