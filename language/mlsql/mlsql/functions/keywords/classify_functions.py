"""
Functions that do some basic model training and evaluation for classification problems
Maybe seperate each model into its own file 
"""



# do_SVM_default_cv
# Performs SVM on a given set of labels and features using the default hyperparameters
# Params: 
#   Features: dataframe of features to predict on
#   Labels: vector/dataframe of labels 
#   cv: Number of folds to do cross validation. If -1, then no cross validation
# Returns: Average Performance of the model (accuracy)
# Side Effects: None
def do_SVM_default_cv(features, labels, cv=10):
  from sklearn import cross_validation, metrics
  from sklearn.svm import SVC
  lin_svm = SVC()
  lin_svm_scores = cross_validation.cross_val_score(lin_svm, features, labels, cv=cv, scoring='accuracy')
  return lin_svm_scores.mean()


# Does SVM with splitting into training/validation sets no cross validation
# Params:
#   Features: dataframe of features to predict on
#   Labels: vectors/data frame on labels  
#   p: percentage of data used for training
# Returns: Performance of model(accuracy) 
def do_SVM_default(features, labels, p=0.8):
  from sklearn import cross_validation, metrics
  from sklearn.svm import SVC
  from sklearn.cross_validation import train_test_split
  from sklearn.metrics import accuracy_score
  import numpy as np
  lin_svm = SVC()
  X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=p, random_state=42)
  lin_svm.fit(X_train, y_train)
  pred = lin_svm.predict(X_test)
  return accuracy_score(preds, y_test)



# do_MNB_default_cv
# Performs MNB on a given set of labels and features using the default hyperparameters
# Params: 
#   Features: dataframe of features to train on
#   Labels: vector/dataframe of labels to train on 
#   cv: Number of folds to do cross validation
# Returns: Average Performance of the model (accuracy)
# Side Effects: None
def do_MNB_default_cv(features, labels, cv=10):
  from sklearn import cross_validation, metrics
  from sklearn.naive_bayes import MultinomialNB
  mNB =  MultinomialNB()
  mNB_scores = cross_validation.cross_val_score(mNB,cv=cv,  features, labels)
  return mNB_scores.mean()


# Does MNB with splitting into training/validation sets no cross validation
# Params:
#   Features: dataframe of features to predict on
#   Labels: vectors/data frame on labels  
#   p: percentage of data used for training
# Returns: Performance of model(accuracy) 
def do_MNB_default(features, labels, p=0.8):
  from sklearn import cross_validation, metrics
  from sklearn.naive_bayes import MultinomialNB
  from sklearn.cross_validation import train_test_split
  from sklearn.metrics import accuracy_score
  import numpy as np
  from sklearn import cross_validation, metrics
  mNB =  MultinomialNB()
  X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=p, random_state=42)
  mNB.fit(X_train, y_train)
  pred = mNB.predict(X_test)
  return accuracy_score(preds, y_test)

# do_rand_forest_default_cv
# Performs random forest classification on a given set of labels and features using the default hyperparameters
# Params: 
#   Features: dataframe of features to train on
#   Labels: vector/dataframe of labels to train on 
#   cv: Number of folds to do cross validation
# Returns: Average Performance of the model(accuracy)
# Side Effects: None
def do_rand_forest_default_cv(features, labels, cv=10):
  from sklearn import cross_validation, metrics
  from sklearn.ensemble import RandomForestClassifier
  rand_forest = RandomForestClassifier(n_estimators=100)
  rand_forest_scores = cross_validation.cross_val_score(rand_forest, features,labels,cv=cv,scoring='accuracy')
  return rand_forest_scores.mean()


# Does MNB with splitting into training/validation sets no cross validation
# Params:
#   Features: dataframe of features to predict on
#   Labels: vectors/data frame on labels  
#   p: percentage of data used for training
# Returns: Performance of model(accuracy) 
def do_rand_forest_default(features, labels, p=0.8):
  from sklearn import cross_validation, metrics
  from sklearn.ensemble import RandomForestClassifier
  from sklearn.cross_validation import train_test_split
  from sklearn.metrics import accuracy_score
  import numpy as np
  from sklearn import cross_validation, metrics
  rand_forest = RandomForestClassifier(n_estimators=100)
  X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=p, random_state=42)
  rand_forest.fit(X_train, y_train)
  pred = rand_forest.predict(X_test)
  return accuracy_score(preds, y_test)


# do_kMeans_default_cv
# Performs K Means classification on a given set of labels and features using the default hyperparameters
# Params: 
#   Features: dataframe of features to train on
#   Labels: vector/dataframe of labels to train on 
#   cv: Number of folds to do cross validation.
# Returns: Performance of the model
# Side Effects: None
def do_kMeans_default_cv(features, labels, cv=10):
  from sklearn import cross_validation, metrics
  from sklearn.cluster import KMeans
  kM = KMeans(n_clusters = 2)
  kM_scores = cross_validation.cross_val_score(kM,features,labels,cv=cv,scoring='accuracy')
  return kM_scores.mean()


# Does MNB with splitting into training/validation sets no cross validation
# Params:
#   Features: dataframe of features to predict on
#   Labels: vectors/data frame on labels  
#   p: percentage of data used for training
# Returns: Performance of model(accuracy) 
def do_kMeans_default(features, labels, p=0.8):
  from sklearn import cross_validation, metrics
  from sklearn.cluster import KMeans
  from sklearn.cross_validation import train_test_split
  from sklearn.metrics import accuracy_score
  import numpy as np
  from sklearn import cross_validation, metrics
  kM = KMeans(n_clusters = 2)
  X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=p, random_state=42)
  kM.fit(X_train, y_train)
  pred = kM.predict(X_test)
  return accuracy_score(preds, y_test)


