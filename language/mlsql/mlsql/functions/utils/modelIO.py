"""
Handles persisting models by saving and loading them into files
"""

from .filepath import get_model_type, get_relative_filename, file_exists
import json

# Constant defining how a file is split into separate components
SEP = ";"
EXTENSION = ".mlsql"

def save_model(filename, model):
    """
    Save a model that has already been trained into a .mlsql file
    The file is saved to the current working directory with the name of the file
    """

    relative_file = get_relative_filename(filename)

    #ensure file does not already exist, if it does, program will add _ INTEGER to the 
    #end of the file to create a unique file
    from os.path import isfile
    counter = 2
    if isfile(relative_file + EXTENSION):
        relative_file  = relative_file + "_1"
        while isfile(relative_file + EXTENSION):
            relative_file = relative_file[:-1] + str(counter)
            counter += 1

    relative_file = relative_file + EXTENSION

    #Open file for writing
    with open(relative_file, 'w') as f:
        #get relevant features
        name = get_model_type(model)
        params = json.dumps(model.get_params())

        f.write(name + "\n")
        f.write(params)


def load_model(filename):
    """
    Reads a model from a .mlsql file that has already been trained
    @return: the model
    """
    if !file_exists(filename):
        return None


    text = None
    model = None
    with open(filename, 'r') as f:
        model = f.readline()
        text = f.readline()
    
    dictionary = json.loads(text)
    fit = model_from_name(model)
    fit.set_params(**dictionary)

    return fit


def model_from_name(name):
    name = name.strip()
    print(name)
    if name == "SVC":
        from sklearn import svm
        return svm.SVC()
    else:
        print("No match in file")
        return None