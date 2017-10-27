# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 20:07:43 2016

@author: Yulia PC
"""
import pandas as pd
from sklearn import tree
from sklearn import cross_validation
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import roc_curve, auc
import pylab as pl
"""
Поэкспериментировать с Decision Trees  и Ensemble methods 
Выполнить оценку качества классификации с использованием Cross-validation.

"""
DataSet = pd.read_csv("data.csv",",")
DataSet = DataSet.replace(to_replace=['M', 'B'], value=[1, 0])
del DataSet['Unnamed: 32']

train = DataSet.drop(['diagnosis'], axis=1) 
target = DataSet.diagnosis

ModelEM = AdaBoostClassifier(n_estimators=100)
ModelTree = tree.DecisionTreeClassifier()

ROCtrainTRN, ROCtestTRN, ROCtrainTRG, ROCtestTRG = cross_validation.train_test_split(train, target, test_size=0.25) 
pl.clf()
pl.figure()
predictRF = ModelEM.fit(ROCtrainTRN, ROCtrainTRG).predict_proba(ROCtestTRN)
fprEM, tprEM, thresholds = roc_curve(ROCtestTRG, predictRF[:,1])
# ROC кривая для RandonForest
roc_aucEM  = auc(fprEM, tprEM)
predictTree = ModelTree.fit(ROCtrainTRN, ROCtrainTRG).predict_proba(ROCtestTRN)
fprTree, tprTree, thresholds = roc_curve(ROCtestTRG, predictTree[:,1])
# ROC кривая для Tree
roc_aucTree  = auc(fprTree, tprTree)
# Строим ROC кривую
pl.plot(fprEM, tprEM, label='%s ROC (area = %0.2f)' % ('Ensemble Metod Model',roc_aucEM))
pl.plot(fprTree, tprTree, label='%s ROC (area = %0.2f)' % ('Tree Model',roc_aucTree))
pl.plot([0, 1], [0, 1], 'k--')
# оформление
pl.xlabel('False Positive Rate')
pl.ylabel('True Positive Rate')
pl.legend(loc=0, fontsize='small')
pl.show()
kfold = 5 #количество подвыборок для валидации
itog_val = {} #список для записи результатов кросс валидации разных алгоритмов
scores = cross_validation.cross_val_score(ModelEM, train, target, cv = kfold)
itog_val['Ensemble Metod Model'] = scores.mean()
scores = cross_validation.cross_val_score(ModelTree, train, target, cv = kfold)
itog_val['Tree Model'] = scores.mean()
pd.DataFrame.from_dict(data = itog_val, orient='index').plot(kind='bar', legend=False)