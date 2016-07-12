"""
Handles persisting models by saving and loading them into files
"""

from .filepath import get_model_type, get_relative_filename
import json

# Constant defining how a file is split into separate components
SEP = ";"

def save_model(filename, model):
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
        params = jason.dumps(model.get_params())

        f.write(name)
        f.write(params)


def load_model(filename):
	text = None
	model = None
	with open(relative_file, 'r') as f:
		model = f.readLine()
		text = f.readLine()
	
	dictionary = json.loads(text)

	fit = model_from_name(model)

	fit.set_params(**dictionary)

	return fit


def model_from_name(name):
	if name == "SVC":
		from sklearn import svm
		return svm.SVC()
	else:
		print("No match in file")
		return None