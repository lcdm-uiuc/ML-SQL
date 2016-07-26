"""
Performs logic to handle the CLASSIFY keyword from ML-SQL language
"""
from ..utils import string_helpers
from sklearn.cross_validation import train_test_split
from ..utils.algorithms import handle_classify_algorithm

def handle_classify(data, algorithm, preds, label, split = False, train = 1):
    """
    Performs logic to handle the classify keyword from ML-SQL language
    """
    model = handle_classify_algorithm(algorithm)
    if model is not None:

        #convert list of columns to integers and covert columns to start at 0
        pred_cols = string_helpers.convert_ints(preds)
        pred_cols = list(map(lambda x: x - 1, pred_cols))

        #Convert label from a string to an int
        label_col = string_helpers.convert_int(label) - 1

        X = data.ix[:,pred_cols]
        y = data.ix[:,label_col]

        #items to return
        X_train, X_test, y_train, y_test = X, None, y, None

        if(split):
            train = float(train)
            X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=train, test_size=(1-train))

        #Train model
        model.fit(X_train, y_train)

        return model, X_test, y_test
    else:
        return None