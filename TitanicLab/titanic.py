# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 14:51:31 2016

@author: Alex
"""
from sklearn import tree
import pandas as pd
from sklearn.metrics import roc_curve, auc
from sklearn import cross_validation
import pylab as pl
from sklearn.ensemble import RandomForestClassifier

# Открытие и корректировка обучающей выборки
passengersP = pd.read_csv('train.csv',",") 
passengersS = pd.read_csv('train.csv',",")
# Замена на числовой формат Тетенька - 1 Дяденька - 0
passengersP = passengersP.replace(to_replace=['male', 'female'], value=[0, 1])
i=0
while i < len(passengersP):
    if pd.isnull(passengersP['Age'][i]):
        passengersP['Age'][i]=passengersP.Age.median()  
    i=i+1
passengersP = passengersP.drop(['Survived','Embarked','Cabin','Name','Ticket'],axis=1)
passengersS = passengersS['Survived']

# Формирование тестовой и тренеровочной выборок
trainP, testP, trainS, real   = cross_validation.train_test_split(passengersP,passengersS, test_size=0.75)

# дерево решений 
TreeModel = tree.DecisionTreeClassifier() 
TreeModel.fit(trainP,trainS)
PredictedTree=TreeModel.predict_proba(testP)
fpr1, tpr1, thresholds = roc_curve(real,PredictedTree[:, 1])
roc_auc1  = auc(fpr1, tpr1)
 
# Построение рок кривой для дерева решений
pl.plot(fpr1, tpr1, label='%s (area = %0.2f)' % ('DTC_TreeModel', roc_auc1))

# случайный лес 
ModelRFC = RandomForestClassifier(n_estimators = 90)
ModelRFC.fit(trainP,trainS)
PredictedRFC=ModelRFC.predict_proba(testP)
fpr, tpr, thresholds = roc_curve(real,PredictedRFC[:, 1])
roc_auc  = auc(fpr, tpr)

# Построение рок кривой для случайного леса
pl.plot(fpr, tpr, label='%s (area = %0.2f)' % ('DTC_ModelRFC', roc_auc))
pl.legend(loc=0, fontsize='small')
pl.plot([0, 1], [0, 1], 'k--')





## Открыетие и корректировка тестовой выборки с кагла
#passengersT=pd.read_csv('test.csv',",")
#passengersT = passengersT.drop(['Embarked','Cabin','Name','Ticket'],axis=1)
#passengersT = passengersT.replace(to_replace=['male', 'female'], value=[0, 1])
#i=0
#while i < len(passengersT):
#    if pd.isnull(passengersT['Age'][i]):
#        passengersT['Age'][i]=passengersT.Age.median() 
#    if pd.isnull(passengersT['Fare'][i]):
#        passengersT['Fare'][i]=passengersT.Age.median()  
#    i=i+1
## Make a tree model









