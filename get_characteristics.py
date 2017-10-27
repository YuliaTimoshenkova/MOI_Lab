
# coding: utf-8
#import datetime
import requests
from bs4 import BeautifulSoup


def get_characteristics(article_url):
    # Задаем ссылку на статью, которую нужно распарсить
    # article_url = 'http://www.e1.ru/news/spool/news_id-449488.html'
    r = requests.get(article_url)
    soup = BeautifulSoup(r.text, 'html.parser')
    
    # Выводим заголовок статьи
    titleTag = soup.html.head.title
    #print(titleTag)
   # print(titleTag.string)
    """
    """
    #ПЕРВОЕ ДЕЛО
    words_in_title=len([len(x) for x in titleTag.string.split()])
    #print(words_in_title);
    
    #ВТОРОЕ ДЕЛО
    articleTag=soup.find('div', {"id" : "newscontent"}).get_text() 
    words_in_article=len([len(x) for x in articleTag.split()])
   # print(words_in_article)
    
    #Третье ТЕЛО
    metaTag= (soup.find('meta',attrs={"name" : "description"}))['content']
    words_in_description = len([len(x) for x in metaTag.split()])
   # print(words_in_description)
    
    
    #Четвертое Тело
    images_number = (len(soup.find('div', {"id" : "newscontent"}).find_all('img')))
   # print(images_number)
    
    #Пятое Задание
    links_number = len(soup.find_all('a',{"class":"news"}))
   # print(links_number)
    
    # Выделяем фрагмент, в котором содержится информация о популярности статьи
    text = soup.get_text()
    i1 = text.find('просмотров:')
    i2 = text.find('версия для печати')
    
    # Выделение количества просмотров
    fragment = text[i1:i2-2]
    j1 = fragment.find('просмотров:')
    j2 = fragment.find('|')
    views_number = int(fragment[j1+12:j2])
   # print('views = ', views_number)
    
    # Выделение количества комментариев
    
    k1 = fragment.find('(')    
    k2 = fragment.find(')')
    
    if k1!=-1:
        comments_number = int(fragment[k1+1:k2])
    else:
        comments_number=0
  
    #print('comments = ', comments_number)
     
    
    characteristics = [ words_in_title, words_in_article, words_in_description, images_number, links_number, views_number, comments_number, 34 ]
    return characteristics


    
    
    
    
    
    