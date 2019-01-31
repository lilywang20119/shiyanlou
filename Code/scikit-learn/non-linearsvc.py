from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

digits = datasets.load_digits()

for index,image in enumerate(digits.images[:5]):
    plt.subplot(2,5,index+1)
    plt.imshow(image,cmap=plt.cm.gray_r,interpolation='nearest')

feature = digits.data
target = digits.target

train_feature,test_feature,train_target,test_target = train_test_split(feature,target,test_size=0.33)

model = SVC(gamma=0.001)
model.fit(train_feature,train_target)

results = model.predict(test_feature)
scores = accuracy_score(test_target,results)
print(scores)
#plt.show()
#print(digits.target[:5])
#print(digits.images[1])
#print(digits.data[1])
