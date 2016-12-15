#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 
from sklearn import tree
from sklearn import cross_validation
from sklearn.metrics import accuracy_score , precision_score, recall_score
 

feature_train, feature_test, label_train, label_test = cross_validation.train_test_split(features, labels, test_size=.3, random_state=42)

clf = tree.DecisionTreeClassifier()
clf.fit(feature_train, label_train)
pred=clf.predict(feature_test)

#How many POIs in the test set
print "Number of POIs: " , sum(pred)

#How many people total in the test set
print "Number of people: " , len(pred)

#If your identifier predicted 0. (not POI) for everyone in the test set, what would its accuracy be?"
print "if all pred equal zero, the accuracy: " , pred.tolist().count(0) / float(len(pred))

#Do you get any true positives? (In this case, we define a true positive as a case where both the actual label and the predicted label are 1)
true_positive = 0
for i in range(len(pred)):
	if (pred[i] == label_test[i]) and label_test[i] == 1:
		true_positive += 1
print "True Positive: " , true_positive

#precision 
print "Precision: " , precision_score(label_test, pred)
#recall
print "Recall: " , recall_score(label_test,pred)
#print accuracy score

# print "accuracy:",accuracy_score(pred,label_test)

