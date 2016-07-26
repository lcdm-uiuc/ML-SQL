def do_logReg_default(features, labels, p=0.8):
    from sklearn import cross_validation, metrics
    from sklearn.linear_model import LogisticRegression
    from sklearn.cross_validation import train_test_split
    from sklearn.metrics import accuracy_score
    import numpy as np
    logreg = LogisticRegression(C=1e5)
    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=p, random_state=42)
    logreg.fit(X_train, y_train)
    pred = logreg.predict(X_test)
    return logreg