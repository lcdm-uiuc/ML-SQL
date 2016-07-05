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