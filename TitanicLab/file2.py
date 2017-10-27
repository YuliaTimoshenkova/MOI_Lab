"""
Created on Sun Oct 30 16:11:45 2016
@author: Yulia PC
"""
import pandas as pd
import seaborn
from sklearn.ensemble import RandomForestClassifier
from sklearn import tree
from sklearn import cross_validation
from sklearn.metrics import roc_curve, auc
import pylab as pl
# загружаем данные
DataTrain = pd.read_csv("train.csv",",")
test = pd.read_csv("test.csv",",")
# подготовка набора данных
DataTrain.Age[DataTrain.Age.isnull()] = DataTrain.Age.mean()
DataTrain[DataTrain.Embarked.isnull()]
MaxPassEmbarked = DataTrain.groupby('Embarked').count()['PassengerId']
DataTrain.Embarked[DataTrain.Embarked.isnull()] = MaxPassEmbarked[MaxPassEmbarked == MaxPassEmbarked.max()].index[0]
DataTrain = DataTrain.drop(['PassengerId','Name','Ticket','Cabin'],axis=1)
# заменяем на числовые значения
DataTrain = DataTrain.replace(to_replace=['female', 'male'], value=[1, 0])
DataTrain = DataTrain.replace(to_replace=['C', 'Q', 'S'], value=[0, 1,2])
test = test.replace(to_replace=['female', 'male'], value=[1, 0])
test = test.replace(to_replace=['C', 'Q', 'S'], value=[0, 1,2])
# Подготовка данных в тестовой выборке
test.Age[test.Age.isnull()] = test.Age.mean()
test.Fare[test.Fare.isnull()] = test.Fare.median() #заполняем пустые значения средней ценой билета
MaxPassEmbarked = test.groupby('Embarked').count()['PassengerId']
test.Embarked[test.Embarked.isnull()] = MaxPassEmbarked[MaxPassEmbarked == MaxPassEmbarked.max()].index[0]
test = test.drop(['Name','Ticket','Cabin','PassengerId'],axis=1)
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
predictRF = ModelRFC.fit(ROCtrainTRN, ROCtrainTRG).predict_proba(ROCtestTRN)
fprRF, tprRF, thresholds = roc_curve(ROCtestTRG, predictRF[:,1])
# ROC кривая для RandonForest
roc_aucRF  = auc(fprRF, tprRF)
predictTree = ModelTree.fit(ROCtrainTRN, ROCtrainTRG).predict_proba(ROCtestTRN)
fprTree, tprTree, thresholds = roc_curve(ROCtestTRG, predictTree[:,1])
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