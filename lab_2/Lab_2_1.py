# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 23:22:16 2016

@author: Yulia PC

простые графики
"""
# подключаем необходимые библиотки
import seaborn
import pandas as pd
import pylab
pylab.xkcd()
# открываем файл с данными
df2 = pd.read_csv("student_alc.csv",";");
f2 = pd.read_csv("f2.csv",";");
# меняем значение колонки sex на бинарный формат
df2 = df2.replace(to_replace=['M', 'F'], value=[1, 0])
# строим графики

sexG = df2['sex'].plot()
sexG.set_xlabel('index')
sexG.set_ylabel('sex')
sexG.set_title('распределение sex опрошеных студентов')


ages = df2['age'].value_counts().plot(kind='bar')
ages.set_xlabel('age')
ages.set_ylabel('number of people')
ages.set_title('distribution age') 

# гистограммы распределения уровня потребления алкоголя
DWH = df2.DW.hist(bins=395)
DWH.set_xlabel('level from1 to 5')
DWH.set_ylabel('number of people')
DWH.set_title('distribution workday alcohol consumption')

DweekH = df2.Dweek.hist(bins=395)
DweekH.set_xlabel('level from1 to 5')
DweekH.set_ylabel('number of people')
DweekH.set_title('distribution weekend alcohol consumption ')

# гистограмма определения уровня здоровья среди опрошенных студентов
hellH = df2['Hel'].value_counts().plot(kind='bar')
hellH.set_xlabel('level from1 to 5')
hellH.set_ylabel('number of people')
hellH.set_title('current health status ')

# подсчет количества опрошеных по возрасту и полу
ages = df2['sex'].value_counts().plot(kind='bar')
ages.set_xlabel('sex')
ages.set_ylabel('number of people')
ages.set_title('distribution sex') 