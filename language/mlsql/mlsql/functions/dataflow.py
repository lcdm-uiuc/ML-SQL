"""
Processes input after it has been parsed. Performs the dataflow for input. 
"""
from .utils.modelIO import save_model
from .utils.keywords import keyword_check
from .keywords.preprocessing.encode_functions import encode_categorical
import numpy as np


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
    replaceCols = parsing.replaceColumns
    replaceVal = parsing.replaceValue
    replaceIdent = parsing.replaceIdentifier
    clusters = parsing.clusters
    missingVal = parsing.replaceIdentifier
    replaceVal = parsing.replaceValue

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
    result += "replace columns: " + str(replaceCols) + "\n"
    result += "replace value: " + str(replaceVal) + "\n"
    result += "replace identifier: " + str(replaceIdent) + "\n"
    print(result)

    model, X_test, y_test = _model_phase(keywords_used, filename, header, sep, train, predictors, label, algo, (None, missingVal,replaceVal), clusters)

    if model is not None:
        _metrics_phase(model, X_test, y_test)

    #save model to file if save keyword is included
    if keywords_used["save"]:
        sfile = parsing.savefile
        print("something")
        print(model)
        save_model(sfile, model)


def _model_phase(keywords, filename, header, sep, train, predictors, label, algorithm, replace = None, clusters = None):
    """
    Model phase of ML-SQL used to create a model
    Uses ML-SQL keywords: READ, REPLACE, SPLIT, CLASSIFY, REGRESSION
    """
    #load keyword
    if keywords["load"]:
        from .keywords.load_functions import handle_load
        model = handle_load(filename)
        return model, None, None

    #read file
    df = None
    if keywords["read"]:
        from .keywords.read_functions import handle_read
        df = handle_read(filename, sep, header)
    if df is not None:
        #Data was read in properly
        print(df.head())

    #Replace
    if keywords["replace"]:
        from .keywords.replace_functions import handle_replace
        df = handle_replace(df, [replace])
        print(df.head())
        pass

    # Encode all categorical values
    df = encode_categorical(df)
    #Classification and Regression and Cluster
    if not keywords["classify"] and not keywords["regress"] and not keywords["cluster"]:
        print("Error: model cannot be built since CLASSIFY, REGRESS, or CLUSTER not specified")
        return None, None, None
    
    elif keywords["classify"] and not keywords["regress"] and not keywords["cluster"]:
        from .keywords.classify_functions import handle_classify
        mod, X_test, y_test = handle_classify(df, algorithm, predictors, label, keywords["split"], train)
        return mod, X_test, y_test
    
    elif not keywords["classify"] and keywords["regress"] and not keywords["cluster"]:
        from .keywords.regress_functions import handle_regress
        mod, X_test, y_test = handle_regress(df, algorithm, predictors, label, keywords["split"], train)
        return mod, X_test, y_test
    
    elif not keywords["classify"] and not keywords["regress"] and keywords["cluster"]:
        from .keywords.cluster_functions import handle_cluster
        mod, X_test, y_test = handle_cluster(df, algorithm, predictors, label, clusters, keywords["split"], train)
        return mod, X_test, y_test

    else:
        print("Error: two or more of the keywords cluster, classify, and regress are in the query")
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
    if X_test is not None and y_test is not None:
        print(model.score(X_test, y_test))
    else:
        return None
