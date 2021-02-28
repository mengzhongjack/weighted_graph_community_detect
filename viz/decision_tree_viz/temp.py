# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""
import dtreeviz
import pandas as pd
import numpy as np
from sklearn.datasets import *
from sklearn import tree

iris = load_iris()
df_iris = pd.DataFrame(iris['data'],columns = iris['feature_names'])
df_iris['target'] = iris['target']

clf = tree.DecisionTreeClassifier()
clf.fit(iris.data,iris.target)

# 使用原生接口可视化数据集
import graphviz 
dot_data = tree.export_graphviz(clf, out_file=None, 
                     feature_names=iris.feature_names,  
                     class_names=iris.target_names,  
                     filled=True, rounded=True,  
                     special_characters=True)  

graph = graphviz.Source(dot_data)  
graph 




# 试试fancy的dtreeviz
from dtreeviz.trees import dtreeviz
viz = dtreeviz(clf,
               iris['data'],
               iris['target'],
               target_name='',
               feature_names=np.array(iris['feature_names']),
               class_names={0:'setosa',1:'versicolor',2:'virginica'},scale=2)
              
viz


regr = tree.DecisionTreeRegressor(max_depth=3)
boston = load_boston()

X_train = boston.data
y_train = boston.target
regr.fit(X_train, y_train)

viz = dtreeviz(regr,
               X_train,
               y_train,
               target_name='price',  # this name will be displayed at the leaf node
               feature_names=boston.feature_names,scale=2
              )
viz


