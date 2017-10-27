# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 20:07:43 2016

@author: Yulia PC
"""

from sklearn import tree
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import label_binarize
from sklearn.metrics import roc_curve, auc
import pylab as pl

from sklearn.datasets import load_iris
iris=load_iris()
X = iris.data
y = iris.target

y = label_binarize(y, classes=[0, 1, 2])
n_classes = y.shape[1]

classifier = tree.DecisionTreeClassifier()
X_train, X_test, y_train, y_test =  train_test_split(X, y, test_size=.5,random_state=0)

y_score = classifier.fit(X_train, y_train).predict( X_test)

fpr = dict()
tpr = dict()
roc_auc = dict()
for i in range(n_classes):
    fpr[i], tpr[i], _ = roc_curve(y_test[:, i], y_score[:, i])
    roc_auc[i] = auc(fpr[i], tpr[i])

fpr["micro"], tpr["micro"], _ = roc_curve(y_test.ravel(), y_score.ravel())
roc_auc["micro"] = auc(fpr["micro"], tpr["micro"])

pl.figure()
lw = 2
pl.plot(fpr[2], tpr[2], color='darkorange',
         lw=lw, label='ROC Decision Tree (area = %0.2f)' % roc_auc[2])
pl.plot([0, 1], [0, 1], 'k--')

pl.xlabel('False Positive Rate')
pl.ylabel('True Positive Rate')
pl.legend(loc=0, fontsize='small')
pl.show()