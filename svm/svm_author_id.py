#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
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
from sklearn import svm
from sklearn.metrics import accuracy_score
clf=svm.SVC(kernel="linear")

# clf=svm.SVC(C=10000, kernel="rbf")

# set time = 0
t0 = time()

#reduce number of the data set into 1%
# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]

clf.fit(features_train,labels_train)
pred=clf.predict(features_test)
# print time used
print "training time:", round(time()-t0, 3), "s"
#print accuracy score
print "accuracy:",accuracy_score(pred,labels_test)

#find answer at # of the data set
# print "prediction for the element 10 of the testing data "  ,  pred[10]
# print "prediction for the element 26 of the testing data "  ,  pred[26]
# print "prediction for the element 50 of the testing data "  ,  pred[50]

#find how many are predicted to be in the "Chris" (1) class
# num = 0

# for n in pred:
#     if n==1:
#         num +=1

# print "check 1: ",num

# n=[]
# [n.append(e) for e in pred if e==1]
# print "check 2: " ,  len(n)

#########################################################


