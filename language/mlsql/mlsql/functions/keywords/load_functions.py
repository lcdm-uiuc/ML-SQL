"""
Performs logic to handle the load keyword from ML-SQL language
"""
from ..utils.modelIO import load_model
from ..utils.filepath import is_mlsql_file
from os.path import is_file

def handle_load(filename):
	#Check if the file exists
	if 

	if is_mlsql_file(filename):
		print("Loading model from: '" + filename + "'")
		model = load_model(filename)
	else:
		print("Filename: '" + filename + "' does not have a .mlsql extension")
		return None
