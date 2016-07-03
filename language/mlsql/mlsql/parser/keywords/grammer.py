"""
Defines lists of grammer constants to be used for language construction
"""

#Libraries
import string
from pyparsing import Literal, Optional

#Define valid symbols and letters
letters = string.ascii_letters
punctuation = string.punctuation
numbers = string.digits
whitespace = string.whitespace

#combinations
everything = letters + punctuation + numbers
everythingWOQuotes = everything.replace("\"", "").replace("'", "")

#Booleans
bools = Literal("True") + Literal("False")

#Parenthesis and Quotes
openParen = Literal("(").suppress()
closeParen = Literal(")").suppress()
openBracket = Literal("[").suppress()
closeBracket = Literal("]").suppress()
Quote = Literal('"').suppress()

#Optional comma for some lists
ocomma = Optional(",").suppress()
