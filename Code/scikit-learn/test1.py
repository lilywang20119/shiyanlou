from sklearn.datasets import make_classification
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

x,y = make_classification(n_samples=300,n_features=2,n_informative=1,n_redundant=0,n_clusters_per_class=1)
plt.scatter(x[:,0],x[:,1],c=y,marker='o')

train_feature,test_feature,train_target,test_target = train_test_split(x,y,test_size=0.33,random_state=56)

model = LogisticRegression()
model.fit(train_feature,train_target)

results = model.predict(test_feature)
plt.scatter(test_feature[:,0],test_feature[:,1],marker=',')

for i,txt in enumerate(results):
    plt.annotate(txt,(test_feature[:,0][i],test_feature[:,1][i]))

plt.show()