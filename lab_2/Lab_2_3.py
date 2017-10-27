# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 22:45:43 2016

@author: Yulia PC

Графики зависимостей уровня употребления 
алкогольных напитков на одном графике
в рабочие дни и выходные дни
для различных параметров
"""
# подключаем необходимые библиотки
import pandas as pd
import seaborn
# открываем файл с данными
df2 = pd.read_csv("student_alc.csv",";");
f2 = pd.read_csv("f2.csv",";");
# меняем значение колонки sex на бинарный формат
df2 = df2.replace(to_replace=['M', 'F'], value=[1, 0])
# строим графики
# по полу студента 
DW15 = df2['DW'][df2['age']==15].sum()/(df2['DW'].value_counts())
DW16 = df2['DW'][df2['age']==16].sum()
f3 = pd.read_csv("student_alc.csv",";");  
AgeAndSex = pd.crosstab(f3.age, f3.sex)
DW_Sex = pd.crosstab(f3.DW,f3.sex)
Dweek_Sex = pd.crosstab(f3.Dweek,f3.sex)
DW_Sex = pd.crosstab( f3.DW,f3.sex)
Hel_Sex = pd.crosstab(f3.Hel,f3.sex)
# график зависимости уровня здоровья для мальчиков и девочек
Hel_SexG = Hel_Sex.plot()
Hel_SexG.set_xlabel('level from1 to 5')
Hel_SexG.set_ylabel('number of people')
Hel_SexG.set_title('current health status for different sex ')

# график зависимости возраста для мальчиков и девочек
AgeAndSexG = AgeAndSex.plot()
AgeAndSexG.set_xlabel('Age')
AgeAndSexG.set_ylabel('number of people')
AgeAndSexG.set_title('number people for different age for different sex ')

# график уровня выпивания алкоголя в выходной день для мальчиков и девочек
Dweek_SexG = Dweek_Sex.plot()
Dweek_SexG.set_xlabel('level from1 to 5')
Dweek_SexG.set_ylabel('number of people')
Dweek_SexG.set_title('current drink in weekend for differen sex ')

# для рабочего дня
DW_SexG = DW_Sex.plot()
DW_SexG.set_xlabel('level from1 to 5')
DW_SexG.set_ylabel('number of people')
DW_SexG.set_title('current drink in work days for differen sex ')

# по возрасту
DW_Age = pd.crosstab(f3.DW,f3.age)
Dweek_Age = pd.crosstab(f3.Dweek,f3.age)
DW_Age = pd.crosstab( f3.DW,f3.age)
Hel_Age = pd.crosstab(f3.Hel,f3.age)

Hel_AgeG = Hel_Age.plot(kind='bar')
Hel_AgeG.set_xlabel('level from1 to 5')
Hel_AgeG.set_ylabel('number of people')
Hel_AgeG.set_title('current health status for differen age ')

Dweek_AgeG = Dweek_Age.plot(kind='bar')
Dweek_AgeG.set_xlabel('level from1 to 5')
Dweek_AgeG.set_ylabel('number of people')
Dweek_AgeG.set_title('current drink in weekend for differen age ')


DW_AgeG = DW_Age.plot(kind='bar')
DW_AgeG.set_xlabel('level from1 to 5')
DW_AgeG.set_ylabel('number of people')
DW_AgeG.set_title('current drink in work days for differen age ')

# по работе мамы
Dweek_M = pd.crosstab(f3.Dweek,f3.mw)
DW_M = pd.crosstab( f3.DW,f3.mw)

Dweek_MG = Dweek_M.plot(kind='bar')
Dweek_MG.set_xlabel('level from1 to 5')
Dweek_MG.set_ylabel('number of people')
Dweek_MG.set_title('current drink in weekend for differen work of mum')


DW_MG = DW_M.plot(kind='bar')
DW_MG.set_xlabel('level from1 to 5')
DW_MG.set_ylabel('number of people')
DW_MG.set_title('current drink in work days for differen work of mum ')

# по работе папы
Dweek_F = pd.crosstab(f3.Dweek,f3.fw)
DW_F = pd.crosstab( f3.DW,f3.fw)


Dweek_FG = Dweek_F.plot(kind='bar')
Dweek_FG.set_xlabel('level from1 to 5')
Dweek_FG.set_ylabel('number of people')
Dweek_FG.set_title('current drink in weekend for differen work of dad')

DW_FG = DW_F.plot(kind='bar')
DW_FG.set_xlabel('level from1 to 5')
DW_FG.set_ylabel('number of people')
DW_FG.set_title('current drink in work days for differen work of dad ')