import sys

sys.path.insert(0, 'parser/')
sys.path.insert(0, 'functions/')

from parser import mlsqlparser
from dataflow import handle

def execute(command):
	"""
	Used to parse and execute an ML-SQL command supplied by the user. 
	This function is meant to exported for use in other modules.
	"""
	myparser = mlsqlparser()
	result = myparser.parseString(command)
	print(result)
	handle(result)



def repl():
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
			handle(result)

if __name__ == "__main__":
	repl()
