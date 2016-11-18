import sys
from time import time
sys.path.append("../tools/")
# from email_preprocess import preprocess
# features_train, features_test, labels_train, labels_test = preprocess()


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels


import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()

########################################################################
### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
# plt.xlim(0.0, 1.0)
# plt.ylim(0.0, 1.0)
# plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
# plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
# plt.legend()
# plt.xlabel("bumpiness")
# plt.ylabel("grade")
# plt.show()
###########################################################################
def show_graph():
        try:
            prettyPicture(clf, features_test, labels_test)
        except NameError:
            pass

###########################################################################
### find how many features in the data set?
print "#of features: ", len(features_train[0])

from sklearn import tree
from sklearn import naive_bayes #GaussianNB, MultinomialNB, BernoulliNB
from sklearn import svm #svm, NuSVC, LinearSVC
from sklearn import neighbors
from sklearn import ensemble #AdaBoost ,RandomForest

from sklearn.metrics import accuracy_score
#from sklearn.model_selection import cross_val_score #v0.18
from sklearn.cross_validation import cross_val_score

def fit_pred():
    # set time = 0
    t0 = time()
    clf.fit(features_train,labels_train)
    pred=clf.predict(features_test)

    # print time used
    print "training time:", round(time()-t0, 3), "s"
    #print accuracy score
    print "accuracy:",accuracy_score(pred,labels_test)
    show_graph()


# def fit_score():
#     t0 = time()
#     clf.fit(features_train,labels_train)
#     score=clf.score(features_test,labels_test)

#     print "training time:", round(time()-t0, 3), "s"
#     print "score:", score
#     print ""
#     show_graph()
#     return None

# def fit_cross_score():
#     from sklearn.cross_validation import cross_val_score
#     t0 = time()
#     clf.fit(features_train,labels_train)
#     score=clf.cross_val_score(features_test,labels_test)

#     print "training time:", round(time()-t0, 3), "s"
#     print "score:", score.mean()
#     print ""
#     show_graph()
#     return None


print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - "
print "Naive bayes"
clf = naive_bayes.GaussianNB()
fit_pred()



print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - "
print "SVM"
clf=svm.SVC(kernel="rbf")

# clf=svm.SVC(kernel="linear")
# clf=svm.SVC(C=10000, kernel="rbf")
fit_pred()

#reduce number of the data set into 1%
# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]


print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - "
print "Decision Tree"
clf=tree.DecisionTreeClassifier()
fit_pred()

print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - "
print "Nearest Neighbors"
from sklearn.neighbors.nearest_centroid import NearestCentroid
clf = NearestCentroid()
fit_pred()
print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - "
print "AdaBoost"
clf = ensemble.AdaBoostClassifier(n_estimators=100)
fit_pred()
print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - "
print "RandomForestClassifier"

clf = ensemble.RandomForestClassifier(n_estimators=10)
fit_pred()

print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - "




