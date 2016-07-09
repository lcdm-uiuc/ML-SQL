"""
Performs logic to handle the REGRESSION keyword from ML-SQL language
"""

def handle_regression(data, algorithm, preds, label, train = .8):
    """
    Performs logic to handle the regression keyword from ML-SQL language
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
    if algo_name.lower() == "simple":
        from sklearn import linear_model
        return linear_model.LinearRegression(fit_intercept = True)
    elif algo_name.lower() == "lasso":
        from sklearn import linear_model
        return linear_model.Lasso(alpha=0.1)
    elif algo_name.lower() == "ridge":
        #random forest
        from sklearn import linear_model
        return linear_model.Ridge(alpha=0.1)
    else:
        print("Error: algorithm '" + algo_name + "' is not available")
        return None