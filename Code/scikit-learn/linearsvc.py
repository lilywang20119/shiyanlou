import pandas as pd
from sklearn.linear_model import Perceptron
from sklearn.datasets import make_classification
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split


df = pd.read_csv('data.csv',header=0)
feature = df[['x','y']]
target = df['class']

train_feature,test_feature,train_target,test_target = train_test_split(feature,target,test_size=0.33,random_state=56)

model = Perceptron()
model.fit(train_feature,train_target)

model2 = LinearSVC()
model2.fit(train_feature,train_target)

print(model.score(test_feature,test_target))
print(model2.score(test_feature,test_target))
