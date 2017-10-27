
# coding: utf-8

import requests
from bs4 import BeautifulSoup



# Задаем ссылку на статью, которую нужно распарсить
article_url = 'http://www.e1.ru/news/spool/news_id-440825-section_id-148.html'
# article_url = 'http://www.e1.ru/news/spool/news_id-449488.html'
r = requests.get(article_url)
soup = BeautifulSoup(r.text, 'html.parser')
i=0
C=list()
for link in soup.findAll('a'):
    i=i+1
    C.append(link.get('href'))   
href =list()

j=63    
while  j<93:
    href.append(C[j])
    j=j+1

div = soup.findAll("div",{"class" : "news"})



"""
# Выводим заголовок статьи
titleTag = soup.html.head.title
print(titleTag.string);
"""

#bodyTag = soup.html.body.table[3]#.tbody.tr.td[2].div[1].table[3]


#print(bodyTag.string);


"""
# Выводим содержимое статьи
print(soup.get_text())

# Выделяем фрагмент, в котором содержится информация о популярности статьи
text = soup.get_text()
print(type(text))
i1 = text.find('просмотров')
i2 = text.find('версия для печати')
print(text[i1:i2-3])

# Выделение количества просмотров
fragment = text[i1:i2-3]
print(fragment)
j1 = fragment.find('просмотров:')
j2 = fragment.find('|')
print(i1)
print(i2)
views = fragment[j1+12:j2]
print('views = ', views)

# Выделение количества комментариев
k1 = fragment.find('(')
k2 = fragment.find(')')
print(k1)
print(k2)
comments = fragment[k1+1:k2]
print('comments = ', comments)
"""