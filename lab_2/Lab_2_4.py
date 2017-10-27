# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 23:45:19 2016

@author: Yulia PC
Графики зависимостей уровня употребления 
алкогольных напитков для девушек и парней по возрасту
в выходные дни 
"""
import pylab
pylab.xkcd()
import pylab
import matplotlib.pyplot as plt
import seaborn
import pandas as pd
from pandas import read_csv;
# открываем файл с данными
df2 = read_csv("student_alc.csv",";");
f2 = read_csv("f2.csv",";");
# меняем значение колонки sex на бинарный формат
df2 = df2.replace(to_replace=['M', 'F'], value=[1, 0])

""" 
средний уровень выпивания алкогольных напитков 
в выходной  день женщинами по возрасту"""
age = [15, 16, 17, 18, 19, 20, 21, 22]
DweekF = []
a = 15;
while a < 23:
    average = df2['Dweek'][df2['age']==a][df2['sex']==1].mean();
    DweekF.append(average);
    a = a + 1;
avgDweekF1 = pd.DataFrame([[DweekF[0]], [DweekF[1]],[DweekF[2]],[DweekF[3]],[DweekF[4]],[DweekF[5]],[DweekF[6]],[DweekF[7]]], columns=["avg_DweekF"])
ages = pd.DataFrame([[age[0]], [age[1]],[age[2]],[age[3]],[age[4]],[age[5]],[age[6]],[age[7]],], columns=["age"])
avgDweekF = pd.DataFrame([[age[0],DweekF[0]], [age[1],DweekF[1]],[age[2],DweekF[2]],[age[3],DweekF[3]],[age[4],DweekF[4]],[age[5],DweekF[5]],[age[6],DweekF[6]],[age[7],DweekF[7]]], columns=["age","avg_DweekF"])
Dweek_F = pd.crosstab(avgDweekF1.avg_DweekF,ages.age)
""" 
средний уровень выпивания алкогольных напитков 
в выходной день мужчин по возрасту"""
DweekM = []
a = 15;
while a < 23:
    averageM = df2['Dweek'][df2['age']==a][df2['sex']==0].mean();
    DweekM.append(averageM);
    a = a + 1;
avgDweekM1 = pd.DataFrame([[DweekM[0]], [DweekM[1]],[DweekM[2]],[DweekM[3]],[DweekM[4]],[DweekM[5]],[DweekM[6]],[DweekM[7]]], columns=["avg_DweekM"])
avgDweekM = pd.DataFrame([[age[0],DweekM[0]], [age[1],DweekM[1]],[age[2],DweekM[2]],[age[3],DweekM[3]],[age[4],DweekM[4]],[age[5],DweekM[5]],[age[6],DweekM[6]],[age[7],DweekM[7]]], columns=["age","avg_DweekM"])
Dweek_F = pd.crosstab(avgDweekM1.avg_DweekM,ages.age)
# построение двух графиков
plt.figure()
line_10, line_20 = plt.plot(avgDweekM['age'], avgDweekM['avg_DweekM'], 'bD:', avgDweekF['age'], avgDweekF['avg_DweekF'], 'r^:')
plt.xlabel('age')
plt.ylabel('average level of drink alc')
plt.title('average level of drink alc in weekend') 
plt.legend( (line_10, line_20), (u'Male', u'Female'), loc = 'best')