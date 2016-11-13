#!/usr/bin/python

"""
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn import tree
from sklearn.metrics import accuracy_score
clf=tree.DecisionTreeClassifier(min_samples_split=40)




# clf=tree.DecisionTreeClassifier()
t0 = time()
clf=clf.fit(features_train,labels_train)
pred=clf.predict(features_test)
print "training time:", round(time()-t0, 3), "s"
print "accuracy:",accuracy_score(pred,labels_test)

### find how many features in the data set?

print "#of features: ", len(features_train[0])

# go into ../tools/email_preprocess.py, and find the line of code that looks like this:
# selector = SelectPercentile(f_classif, percentile=10)
# Change percentile from 10 to 1, and rerun dt_author_id.py.

#########################################################


