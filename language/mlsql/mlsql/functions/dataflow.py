"""
Processes input after it has been parsed. Performs the dataflow for input. 
"""
from .keywords.read_functions import handle_read

def handle(parsing):
    #Extract relevant features from the query
    filename = parsing.filename
    header = parsing.header
    sep = parsing.sep
    train = parsing.train_split
    test = parsing.test_split
    predictors = parsing.predictors
    label = parsing.label
    algo = str(parsing.algorithm)

    data = handle_read(filename, sep, header)
    print(data.head())