# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 22:13:34 2016

@author: Yulia PC
Графики зависимостей уровня употребления 
алкогольных напитков для девушек и парней по возрасту
в рабочие дни 
"""
import pylab
pylab.xkcd()
import matplotlib.pyplot as plt
import seaborn
import pandas as pd

# открываем файл с данными
df2 = pd.read_csv("student_alc.csv",";");
f2 = pd.read_csv("f2.csv",";");
# меняем значение колонки sex на бинарный формат
df2 = df2.replace(to_replace=['M', 'F'], value=[1, 0])

""" 
средний уровень выпивания алкогольных напитков 
в рабочий день женщинами по возрасту"""
age = [15, 16, 17, 18, 19, 20, 21, 22]
DWF = []
a = 15;
while a < 23:
    average = df2['DW'][df2['age']==a][df2['sex']==1].mean();
    DWF.append(average);
    a = a + 1;
avgDWF1 = pd.DataFrame([[DWF[0]], [DWF[1]],[DWF[2]],[DWF[3]],[DWF[4]],[DWF[5]],[DWF[6]],[DWF[7]]], columns=["avg_DWF"])
ages = pd.DataFrame([[age[0]], [age[1]],[age[2]],[age[3]],[age[4]],[age[5]],[age[6]],[age[7]],], columns=["age"])
avgDWF = pd.DataFrame([[age[0],DWF[0]], [age[1],DWF[1]],[age[2],DWF[2]],[age[3],DWF[3]],[age[4],DWF[4]],[age[5],DWF[5]],[age[6],DWF[6]],[age[7],DWF[7]]], columns=["age","avg_DWF"])
DW_F = pd.crosstab(avgDWF1.avg_DWF,ages.age)
""" 
средний уровень выпивания алкогольных напитков 
в рабочий день мужчин по возрасту"""
DWM = []
a = 15;
while a < 23:
    averageM = df2['DW'][df2['age']==a][df2['sex']==0].mean();
    DWM.append(averageM);
    a = a + 1;
avgDWM1 = pd.DataFrame([[DWM[0]], [DWM[1]],[DWM[2]],[DWM[3]],[DWM[4]],[DWM[5]],[DWM[6]],[DWM[7]]], columns=["avg_DWM"])
avgDWM = pd.DataFrame([[age[0],DWM[0]], [age[1],DWM[1]],[age[2],DWM[2]],[age[3],DWM[3]],[age[4],DWM[4]],[age[5],DWM[5]],[age[6],DWM[6]],[age[7],DWM[7]]], columns=["age","avg_DWM"])
DW_F = pd.crosstab(avgDWM1.avg_DWM,ages.age)
# построение двух графиков

line_10, line_20 = plt.plot(avgDWM['age'], avgDWM['avg_DWM'], 'bD:', avgDWF['age'], avgDWF['avg_DWF'], 'r^:')
plt.xlabel('age')
plt.ylabel('average level of drink alc')
plt.title('average level of drink alc in work day') 
plt.legend( (line_10, line_20), (u'Male', u'Female'), loc = 'best')