import sys

sys.path.insert(0, 'parser/')

from parser import parser

def repl(parser):
	while True:
		command = input(">")
		if command.lower() == "exit":
			print("exiting")
		else:
			result = parser.parseString(command)
			print(result)

if __name__ == "__main__":
	#initialize the parser
	print("Initializing Parser...")
	myparser = parser()
	
	print("ML-SQL Parser is ready for use")
	repl(parser)
