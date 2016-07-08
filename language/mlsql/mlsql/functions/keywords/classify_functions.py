"""
Performs logic to handle the CLASSIFY keyword from ML-SQL language
"""

def handle_classify(data, algorithm, preds, label, train = .8):
    """
    Performs logic to handle the classify keyword from ML-SQL language
    """
    model = _handle_algorithm(algorithm)
    if model is not None:
        pred_cols = map(int, preds)
        pred_cols = map(lambda x: x - 1, pred_cols)
        label_col = int(label1) - 1

        X = data.ix[:,pred_cols]
        y = data.ix[:,label_col]

        X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=train, test_size=(1-train))

        #Train model
        model.fit(X_train, y_train)

        #Performance on test data
        model.score(X_test, y_test)

        return model
    else:
        return None


def _handle_algorithm(algorithm):
    algo_name = str(algorithm)
    if algo_name.lower() == "svm":
        from sklearn import svm
        return svm.SVC()
    elif algo_name.lower() == "logistic":
        from sklearn.linear_model import LogisticRegression
        return LogisticRegression()
    elif algo_name.lower() == "forest":
        #random forest
        from sklearn.ensemble import RandomForestClassifier
        return RandomForestClassifier()
    else:
        print("Error: algorithm '" + algo_name + "' is not available")
        return None