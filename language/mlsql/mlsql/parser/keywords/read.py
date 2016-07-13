from .grammer import *
from pyparsing import Word, oneOf, Optional, Or, Literal

def define_read():
	filename = Word(everything).setResultsName("filename")

	#define so that there can be multiple verisions of READ
	readKeyword = oneOf(["Read", "READ"]).setResultsName("read")

	#Define Read Optionals
	#header
	headerLiteral = (Literal("header") + Literal("=")).suppress()
	header = Optional(headerLiteral + Or(bools).setResultsName("header"), default = "False" )

	#separator
	separatorLiteral = (Or([Literal("sep"), Literal("separator")]) + Literal("=")).suppress()
	definesep = Quote + Word(everythingWOQuotes + whitespace).setResultsName("sep") + Quote
	separator = Optional(separatorLiteral + definesep, default = ",")

	#Compose Read Optionals
	readOptions = Optional(openParen + separator + header + closeParen)

	read = readKeyword + filename + readOptions
	
	return read
