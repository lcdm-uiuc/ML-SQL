
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


