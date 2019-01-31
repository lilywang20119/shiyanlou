from sklearn import datasets
from sklearn.svm import LinearSVR
from sklearn.cross_validation import cross_val_predict
import matplotlib.pyplot as plt

boston = datasets.load_boston()
feature = boston.data
target = boston.target

model = LinearSVR()
predictions = cross_val_predict(model,feature,target,cv=10)
#print(boston.DESCR)

plt.scatter(target,predictions)
plt.plot([target.min(),target.max()],[target.min(),target.max()],'k--',lw=4)
plt.xlabel('true_target')
plt.ylabel('prediction')

plt.show()