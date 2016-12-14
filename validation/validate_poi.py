#!/usr/bin/python


"""
    Starter code for the validation mini-project.
    The first step toward building your POI identifier!

    Start by loading/formatting the data

    After that, it's not our code anymore--it's yours!
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### first element is our labels, any added elements are predictor
### features. Keep this the same for the mini-project, but you'll
### have a different feature list when you do the final project.
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)


### it's all yours from here forward!  
# using Decision tree for machine training
from sklearn import tree
clf = tree.DecisionTreeClassifier()

## using the same data to train and predict
# clf.fit(features, labels)
# pred1 = clf.predict(features)
# from sklearn.metrics import accuracy_score
# print "overfit: ", accuracy_score(pred1, labels)
# 0.989473684211


# using cross validation to split the data set 
from sklearn import cross_validation
feature_train, feature_test, label_train, label_test = cross_validation.train_test_split(features, labels, test_size=.3, random_state=42)


clf.fit(feature_train, label_train)
pred=clf.predict(feature_test)

#print accuracy score
from sklearn.metrics import accuracy_score
print "accuracy:",accuracy_score(pred,label_test)
#0.724137931034
