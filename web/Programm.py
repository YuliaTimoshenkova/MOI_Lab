# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 22:20:11 2016
@author: Yulia PC
Главная программа получения данных
"""
import ArticleList as al # Получаем список ссылок
import ParameterList as pl # Получаем список параметров для ссылок
import matplotlib.pyplot as plt
import seaborn
# Получаем список ссылок с помощью ренее написанной функции
# al.ArticleList(период, номер_категории)
PeriodNumber = int(input("Введите необходимый период: "))
CategoryId = int(input("Введите id категории: "))
ArticleList = al.ArticleList(PeriodNumber, CategoryId) 
ParameterList = list()
# Получаем все статьи за полгода и их характеристики
i = 0
while i < len(ArticleList):
    statat=[ArticleList[i], pl.ParameterList(ArticleList[i]) ]
    ParameterList.append(statat)
    i=i+1
# Получаем параметры для построения необходимых гистограмм
ViewList = list() #лист просмотров всех статей для гистограммы
ComentList = list() #лист комментариев всех статей для гистограммы
i=0
while i < len(ParameterList):
    ViewList.append((ParameterList[i][1])[5])
    ComentList.append((ParameterList[i][1])[6])
    i = i + 1
# Построение гистограмм
plt.figure()
seaborn.distplot(ViewList)
plt.xlabel('Значения')
plt.ylabel('Частота')
plt.title('Распределение просмотров')
plt.figure()
seaborn.distplot(ComentList)
plt.xlabel('Значения')
plt.ylabel('Частота')
plt.title('Распределение комментариев')