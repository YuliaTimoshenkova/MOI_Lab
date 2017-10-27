# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 23:22:16 2016

@author: Yulia PC

простые графики
"""
# подключаем необходимые библиотки
import seaborn
import pandas as pd

# l1
f2 = pd.read_csv("f2.csv",";");
# открываем файл с данными
df2 = pd.read_csv("student_alc.csv",";");
df1 = pd.read_csv("student_alc.csv",";");
# меняем значение колонки sex на бинарный формат
df2 = df2.replace(to_replace=['M', 'F'], value=[1, 0])
# ищем максимальный возраст
MaxAge = df2['age'].max()
# строим гистограмму
DWH = df2.DW.hist(bins=395)
DWH.set_xlabel('level from1 to 5')
DWH.set_ylabel('number of people')
DWH.set_title('distribution workday alcohol consumption')
#l2
# убераем повторяющийся возраст
name = df1.groupby('age')
df1 = name.sum() 
# возраст, которого меньше всего среди опрошенных
Sorted = df2.sort_values(['age'], ascending=False)
z = Sorted.head(1)
# L3
print(df2['age'].unique())
# L4
del df2['internet']
df2['number'] = df2['DW'] + df2['Dweek']
# L5
stack = df2.stack()
transpose = df2.T
# L6
"""-"""
# L7
df2 = pd.read_csv("student_alc.csv",";");
df2['x-Mean'] = abs(df2['DW'] - df2['DW'].mean())
df2['std'] = df2['Dweek'].std()  
df = df2.copy()
State = df.groupby('age')
df['DWR'] = State['DW'].transform( lambda x: x.quantile(q=.25) - (1.5*(x.quantile(q=.75)-x.quantile(q=.25))) )
df['DWL'] = State['Dweek'].transform( lambda x: x.quantile(q=.75) + (1.5*(x.quantile(q=.75)-x.quantile(q=.25))) )
df['DWOutlier'] = (df['DWR'] < df['DWL']) | (df['DWR'] > df['DWL']) 
# L8
"""-"""
# L9
""" из кода про статьи """
# L10
df2 = pd.read_csv("student_alc.csv",";");
df2.to_json('FirstDataJson')
df3 = pd.read_json('FirstDataJson')
# L11
