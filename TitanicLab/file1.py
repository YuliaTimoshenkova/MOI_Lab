# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 16:11:45 2016

@author: Yulia PC
"""
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn import cross_validation
from sklearn.ensemble import RandomForestClassifier
from sklearn import tree
from sklearn.metrics import roc_curve, auc
import pylab as pl

DataTrain = pd.read_csv("train.csv",",")
test = pd.read_csv("test.csv",",")


DataTrain.Age = DataTrain.Age.median()
DataTrain[DataTrain.Embarked.isnull()]
MaxPassEmbarked = DataTrain.groupby('Embarked').count()['PassengerId']
DataTrain.Embarked[DataTrain.Embarked.isnull()] = MaxPassEmbarked[MaxPassEmbarked == MaxPassEmbarked.max()].index[0]
DataTrain = DataTrain.drop(['PassengerId','Name','Ticket','Cabin'],axis=1)
# заменяем на числовые значения
label = LabelEncoder()
dicts = {}

label.fit(DataTrain.Sex.drop_duplicates()) #задаем список значений для кодирования
dicts['Sex'] = list(label.classes_)
DataTrain.Sex = label.transform(DataTrain.Sex) #заменяем значения из списка кодами закодированных элементов 

label.fit(DataTrain.Embarked.drop_duplicates())
dicts['Embarked'] = list(label.classes_)
DataTrain.Embarked = label.transform(DataTrain.Embarked)
# Подготовка данных в тестовой выборке
test.Age[test.Age.isnull()] = test.Age.mean()
test.Fare[test.Fare.isnull()] = test.Fare.median() #заполняем пустые значения средней ценой билета
MaxPassEmbarked = test.groupby('Embarked').count()['PassengerId']
test.Embarked[test.Embarked.isnull()] = MaxPassEmbarked[MaxPassEmbarked == MaxPassEmbarked.max()].index[0]
result = pd.DataFrame(test.PassengerId)
test = test.drop(['Name','Ticket','Cabin','PassengerId'],axis=1)
label.fit(dicts['Sex'])
test.Sex = label.transform(test.Sex)
label.fit(dicts['Embarked'])
test.Embarked = label.transform(test.Embarked)
# выборки для моделей
# из исходных данных убираем Id пассажира и флаг спасся он или нет
train = DataTrain.drop(['Survived'], axis=1) 
target = DataTrain.Survived 
# кол-во деревьев 90
ModelRFC = RandomForestClassifier(n_estimators = 90) 
ModelTree = tree.DecisionTreeClassifier()
# данные для ROC кривой
# cross_validation.train_test_split позволяет выбрать из данных выборку размером 25%
ROCtrainTRN, ROCtestTRN, ROCtrainTRG, ROCtestTRG = cross_validation.train_test_split(train, target, test_size=0.25) 
pl.clf()
pl.figure()
probaRF = ModelRFC.fit(ROCtrainTRN, ROCtrainTRG).predict_proba(ROCtestTRN)
fprRF, tprRF, thresholds1 = roc_curve(ROCtestTRG, probaRF[:,1])
# ROC кривая для RandonForest
roc_aucRF  = auc(fprRF, tprRF)
probaTree = ModelTree.fit(ROCtrainTRN, ROCtrainTRG).predict(ROCtestTRN)
fprTree, tprTree, thresholds2 = roc_curve(ROCtestTRG, probaTree)
# ROC кривая для Tree
roc_aucTree  = auc(fprTree, tprTree)
# Строим ROC кривую
pl.plot(fprRF, tprRF, label='%s ROC (area = %0.2f)' % ('Random Forest Model',roc_aucRF))
pl.plot(fprTree, tprTree, label='%s ROC (area = %0.2f)' % ('Tree Model',roc_aucTree))
pl.plot([0, 1], [0, 1], 'k--')
# оформление
pl.xlabel('False Positive Rate')
pl.ylabel('True Positive Rate')
pl.legend(loc=0, fontsize='small')
pl.show()