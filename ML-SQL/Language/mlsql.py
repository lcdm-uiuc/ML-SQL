import sys

sys.path.insert(0, 'parser/')

from parser import parser

def repl(parser):
	#initialize the parser
	print("Initializing Parser...")
	myparser = parser()
	
	print("ML-SQL Parser is ready for use")

	while True:
		command = input(">")
		if command.lower() == "exit":
			print("Exiting ML-SQL")
			break
		else:
			result = myparser.parseString(command)
			print(result)

if __name__ == "__main__":
	repl(parser)
