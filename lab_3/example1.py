
# coding: utf-8

import requests
from bs4 import BeautifulSoup



# Задаем ссылку на статью, которую нужно распарсить
article_url = 'http://www.e1.ru/news/spool/news_id-449429-section_id-162.html'
# article_url = 'http://www.e1.ru/news/spool/news_id-449488.html'
r = requests.get(article_url)
soup = BeautifulSoup(r.text, 'html.parser')
#for link in soup.findAll('a'):)
#    print (link.get('href'))
WordsInArticle = len(soup.find('div',{"id":"newscontent"}).get_text())
print(WordsInArticle)
# Выводим заголовок статьи
titleTag = soup.html.head.title
#print(titleTag)
#print(titleTag.string)
#
## Выводим содержимое статьи
#print(soup.get_text())
LinksNumber = len(soup.find_all('a', {"class":"news"}))  
print(LinksNumber)
ImagesNumbers = len(soup.html.body.find_all('img')) 
ImagesNumber = len(soup.find('div',{"id":"newscontent"}).find_all('img'))
print (str(ImagesNumbers) + '   '+ str(ImagesNumber))
# Выделяем фрагмент, в котором содержится информация о популярности статьи
#text = soup.get_text()
#
#i1 = text.find('просмотров')
#i2 = text.find('версия для печати')
#
#
## Выделение количества просмотров
#fragment = text[i1:i2-3]
#
#j1 = fragment.find('просмотров:')
#j2 = fragment.find('|')
#print(i1)
#print(i2)
#views = int(fragment[j1+12:j2])
#print(views)
#
## Выделение количества комментариев
#k1 = fragment.find('(')
#k2 = fragment.find(')')
#print(k1)
#print(k2)
#comments = int(fragment[k1+1:k2])

