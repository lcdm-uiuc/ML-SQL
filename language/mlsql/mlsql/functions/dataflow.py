"""
Processes input after it has been parsed. Performs the dataflow for input. 
"""
from .keywords.read_functions import handle_read
from .keywords.classify_functions import handle_classify

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

    print(result)



def _save_model(filename, model):
    """
    Save a model that has already been trained into a .mlsql file
    The file is saved to the current working directory with the name of the file
    @TODO
    """
    relative_file = _get_relative_filename(filename)

    #ensure file does not already exist
    from os.path import isfile
    counter = 2
    if isfile(relative_file):
        relative_file  = relative_file + "_1"
        while(isfile(relative_file)):
            relative_file = relative_file[:-1] + str(counter)
            counter += 1

    #Open file for writing
    with open(relative_file, 'w') as f:
        read_data = f.read()

        #get relevant features
        name = _get_model_type(model)
        params = "coef_" + str(model.get_params())

        writing = name + ";" + params

        f.write(writing)


def _get_relative_filename(filename):
    """
    returns only the last part of a file (removes all subdirectories from filename)
    """
    slash_split = filename.split("/")
    return filename[-1]


def _get_model_type(model):
    """
    returns the name of a sklearn model (indentifies from string version of it)
    """
    stringm = str(model)
    splitParen = stringm.split("/")
    return splitParen[1]