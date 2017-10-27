# -*- coding: utf-8 -*-
import get_characteristics as gc 
import get_article_list as gal
import matplotlib.pyplot as plt



article_list = gal.get_article_list(180)
charcteristic_list = list()

#print(article_list)

#Получение всех характеристик для каждой статьи
i = 0
while i < len(article_list):
    statat=[article_list[i], gc.get_characteristics(article_list[i]) ]
    charcteristic_list.append(statat)
    i=i+1

#Обращение к характеристикам статьи, которая содержится в 1 записи 
#print(charcteristic_list[0][1])
#Обращение к определенной характеристике статьи статьи, которая содержится в 1 записи 

gv = list() #лист с колличеством просмотров
gc = list() #лист с колличеством коментариев 
i=0
while i < len(charcteristic_list):
    gv.append((charcteristic_list[i][1])[5])
    gc.append((charcteristic_list[i][1])[6])
    i = i + 1

#построение гистограмм
plt.hist(gv, 30) #просмотры

plt.hist(gc,30) #коментарии

















