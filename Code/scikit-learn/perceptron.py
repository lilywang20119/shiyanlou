from sklearn.datasets import make_classification
import matplotlib.pyplot as plt
from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split

X1,Y1 = make_classification(n_features=2,n_redundant=0,n_informative=1,n_clusters_per_class=1)
#plt.scatter(X1[:,0],X1[:,1],marker='o',c=Y1)


train_feature,test_feature,train_target,test_target = train_test_split(X1,Y1,test_size=0.33,random_state=56)
model = Perceptron()
model.fit(train_feature,train_target)

results = model.predict(test_feature)
plt.scatter(test_feature[:,0],test_feature[:,1],marker=',')

for i,txt in enumerate(results):
    plt.annotate(txt,(test_feature[:,0][i],test_feature[:,1][i]))

plt.show()