"""
Performs logic to handle the CLUSTER keyword from ML-SQL language
"""
from ..utils import string_helpers
from ..utils.algorithms import handle_cluster_algorithm
from sklearn.cross_validation import train_test_split

def handle_cluster(data, algorithm, preds, label = None, clusters = 3, split = False, train = 1):
    """
    Performs logic to handle the CLUSTER keyword from ML-SQL language
    """
    model = handle_cluster_algorithm(algorithm)
    if model is not None:
        if clusters is '':
            clusters = '3'
        model.n_clusters = int(clusters)

        #convert list of columns to integers and covert columns to start at 0
        pred_cols = string_helpers.convert_ints(preds)
        pred_cols = list(map(lambda x: x - 1, pred_cols))
        X = data.ix[:,pred_cols]

        if string_helpers.check_exists(label):
            return _cluster_label(data, model, X, label, split, train)
        else:
            return _cluster_no_label(data, model, X, split, train)
    else:
        return None, None, None
        

def _cluster_label(data, model, X, label, split, train):
    """
    Dataflow for clustering when a label is specified
    """
    #Convert label from a string to an int
    label_col = string_helpers.convert_int(label) - 1
    y = data.ix[:,label_col]

    #items to return
    X_train, y_train, X_test, y_test = X, y, None, None

    if(split):
        train = float(train)
        X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=train, test_size=(1-train))
    
    #Train model
    model.fit(X_train, y_train)
    return model, X_test, y_test


def _cluster_no_label(data, model, X, split, train):
    """
    Dataflow for clustering when a label is not specified
    """
    #items to return
    X_train, X_test = X, None

    if(split):
        train = float(train)
        X_train, X_test = train_test_split(X, train_size=train, test_size=(1-train))

    #Train model
    model.fit(X_train)
    return model, X_test, None