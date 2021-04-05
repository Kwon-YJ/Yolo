# coding: utf-8

from sklearn.datasets import load_iris

iris_dataset = load_iris()



print("iris_dataset의 키: \n{}".format(iris_dataset.keys()))

# dict_keys(['data', 'target', 'target_names', 'DESCR', 'feature_names'])



# target_names의 값은 붓꽃 품종의 이름을 문자열 배열로 가지고 있다

print("타깃의 이름 : {}".format(iris_dataset['target_names']))

# 타깃의 이름 : ['setosa' 'versicolor' 'virginica']



# feature_names 값은 각 특성을 설명하는 문자열 리스트

print("특성의 이름 : \n{}".format(iris_dataset['feature_names']))

# ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']



# DESCR 키에는 데이터셋에 대한 간략한 설명이 있다.

print(iris_dataset['DESCR'][:193]+"\n...")



# target, data에는 실제 데이터가 있따.

# data : 꽃잎의 길이와 폭, 꽃받침의 길이와 폭을 수치값으로 가지고 있는 numpy 배열

print("data의 타입: {}".format(type(iris_dataset['data'])))

print("data의  크기: {}".format(iris_dataset['data'].shape))

# data의  크기: (150, 4)

# 이배열은 150개의 붓꽃 데이터를 가지고 있다.



# target : 샘플 붓꽃의 품종을  가지고 있는 numpy 배열

print("target의 타입: {}".format(type(iris_dataset['target'])))

print("target의  크기: {}".format(iris_dataset['target'].shape))
