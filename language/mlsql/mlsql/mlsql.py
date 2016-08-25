import sys

from .parser.parser import mlsqlparser
from .functions.dataflow import handle

def execute(command, verbose=False):
	"""
	Used to parse and execute an ML-SQL command supplied by the user. 
	This function is meant to exported for use in other modules.
	"""
	myparser = mlsqlparser()
	result = myparser.parseString(command)
	#print(result)
	handle(result, verbose)



def repl(verbose=False):
	"""
	Used to create a read-evaluate-print-loop sequence for the ML-SQL langauge.
	This function will continually parse and execute user input from command
	line until the word exit is typed. 
	"""
	print("Initializing Parser...")
	myparser = mlsqlparser()
	
	print("ML-SQL Parser is ready for use")

	while True:
		command = input(">")
		if command.lower() == "exit":
			print("Exiting ML-SQL")
			break
		else:
			result = myparser.parseString(command)
			print(result)
			handle(result, verbose)

if __name__ == "__main__":
	repl()
