# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 14:09:10 2016

@author: Yulia PC
"""

import ArticleList as al 
import AnalisList as AnL
import pandas as pd
Cat = 19
# Получаем список ссылок с помощью ренее написанной функции
# al.ArticleList(период, номер_категории)
PeriodNumber = int(input("Введите необходимый период: "))
CategoryId = int(input("Введите id категории: "))
ArticleList = al.ArticleList(PeriodNumber, CategoryId) 

AnalisList = list()
i = 0
while i < len(ArticleList):
    statat=[ArticleList[i],AnL.AnalisList(ArticleList[i]) ]
    AnalisList.append(statat)
    i=i+1
WordsInTitl =list()
WordsInArticle =  list()
WordsInDescription = list()
ImagesNumber = list()
LinksNumber = list()
ViewList = list() #лист просмотров всех статей для гистограммы
ComentList = list() #лист комментариев всех статей для гистограммы
N = len(AnalisList)
i=0
while i < N:
    WordsInTitl.append((AnalisList[i][1])[0])
    WordsInArticle.append((AnalisList[i][1])[1])
    WordsInDescription.append((AnalisList[i][1])[2])
    ImagesNumber.append((AnalisList[i][1])[3])
    LinksNumber.append((AnalisList[i][1])[4])
    ViewList.append((AnalisList[i][1])[5])
    ComentList.append((AnalisList[i][1])[6])
    i = i + 1
i=0
WT = WA = WD = IN =  LN = VN = CN = 0
while i < N:
    WT = WT + ((AnalisList[i][1])[0])   
    WA = WA + ((AnalisList[i][1])[1])
    WD = WD + ((AnalisList[i][1])[2])
    IN = IN + ((AnalisList[i][1])[3])
    LN = LN + ((AnalisList[i][1])[4])
    VN = VN + ((AnalisList[i][1])[5])
    CN = CN + ((AnalisList[i][1])[6])
    i = i + 1
WordsInTitlAvg = WT/ N
WordsInArticleAvg = WA / N
WordsInDescriptionAvg = WD / N
ImagesNumberAvg = IN / N
LinksNumberAvg = LN / N
ViewListAvg = VN / N
ComentListAvg = CN / N
#f1 = pd.read_csv("avg.csv");
#f1.insert(1,'Категория',((AnalisList[1][1])[7]) )
avg = [{'CAT': Cat, 'WTA': WordsInTitlAvg, 'WAA': WordsInArticleAvg , 'WDA': WordsInDescriptionAvg,
'INA' : ImagesNumberAvg, 'LNA' : LinksNumberAvg, 'VNA' : ViewListAvg, 'CNA' : ComentListAvg}]
dfavg = pd.DataFrame(avg)

Vldf = pd.DataFrame(ViewList,columns=["1"])
Vldf.to_csv('AllView.csv', ';')
Cldf = pd.DataFrame(ComentList,columns=["1"])
Cldf.to_csv('AllCom.csv', ';')
dfavg.to_csv('AvgData.csv', ';')