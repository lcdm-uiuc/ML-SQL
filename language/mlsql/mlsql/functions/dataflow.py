"""
Processes input after it has been parsed. Performs the dataflow for input. 
"""
from .keywords.read_functions import handle_read
from .utils.modelIO import save_model
from .utils.keywords import keyword_check

def handle(parsing):
    #Extract relevant features from the query
    filename = parsing.filename
    header = parsing.header
    sep = parsing.sep
    train = parsing.train_split
    test = parsing.test_split
    predictors = parsing.predictors
    label = parsing.label
    algo = parsing.algorithm

    #create a dictionary with all keywords
    keywords_used = keyword_check(parsing)

    result = "filename: " + filename + "\n"
    result += "header: " + header + "\n"
    result += "separator: " + sep + "\n"
    result += "train size: " + train + "\n"
    result += "test size: " + test + "\n"
    result += "predictors: " + str(predictors) + "\n"
    result += "label: " + str(label) + "\n"
    result += "algorithm: " + str(algo) + "\n"

    print(result)

    model, X_test, y_test = _model_phase(keywords_used, filename, header, sep, train, predictors, label, algo)

    if model and model is not None:
        _metrics_phase(model, X_test, y_test)

    #regression
    #classify = handle_regression(data, algo, predictors, label)


def _model_phase(keywords, filename, header, sep, train, predictors, label, algorithm):
    """
    Model phase of ML-SQL used to create a model
    Uses ML-SQL keywords: READ, REPLACE, SPLIT, CLASSIFY, REGRESSION
    """
    #read file
    df = handle_read(filename, sep, header)
    if df and df is not None:
        #Data was read in properly
        print(data.head() + "\n")

    if keywords["replace"]:
        pass

    #Classification and Regression
    if not keywords["classify"] and not keywords["regression"]:
        return None, None, None
    
    elif keywords["classify"] and not keywords["regression"]:
        from .keywords.classify_functions import handle_classify
        mod, X_test, y_test = handle_classify(df, algorithm, preds, label, keywords["split"], train)
        return mod, X_test, y_test
    
    elif not keywords["classify"] and keywords["regression"]:
        from .keywords.regression_functions import handle_regression
        mod = handle_regression(df, algorithm, preds, label, keywords["split"], train)
        return mod, None, None
    
    else:
        print("Error: both classify and regression keywords present")
        return None, None, None


def _apply_phase(keywords):
    """
    Apply phase of ML-SQL used to label new data with the trained model
    Uses ML-SQL keywords: SPLIT, APPLY
    """
    #classify = handle_classify(data, algo, predictors, label)
    pass


def _metrics_phase(model, X_test, y_test):
    """
    Metrics phase of ML-SQL used to calculate or plot results
    Uses ML-SQL keywords: PLOT, CALCULATE, GRAPH
    """
    #Performance on test data
    model.score(X_test, y_test)
