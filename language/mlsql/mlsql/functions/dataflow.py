"""
Processes input after it has been parsed. Performs the dataflow for input. 
"""
from .keywords.read_functions import handle_read
from .keywords.classify_functions import handle_classify
from .utils.modelIO import save_model

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

    result = "filename: " + filename + "\n"
    result += "header: " + header + "\n"
    result += "separator: " + sep + "\n"
    result += "train size: " + train + "\n"
    result += "test size: " + test + "\n"
    result += "predictors: " + str(predictors) + "\n"
    result += "label: " + str(label) + "\n"
    result += "algorithm: " + str(algo) + "\n"

    print(result)

    #read file
    data = handle_read(filename, sep, header)
    if data is not None:
        #Data was read in properly
        print(data.head() + "\n")

    #split

    #classify
    classify = handle_classify(data, algo, predictors, label)

    _save_model(classify)

    #regression
    #classify = handle_regression(data, algo, predictors, label)