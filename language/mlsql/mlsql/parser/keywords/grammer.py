"""
Defines lists of grammer constants to be used for language construction
"""

#Libraries
import string
from pyparsing import Literal, CaselessLiteral, Optional

#Define valid symbols and letters
letters = string.ascii_letters
punctuation = string.punctuation
numbers = string.digits
whitespace = string.whitespace

#combinations
everything = letters + punctuation + numbers
everythingWOQuotes = everything.replace("\"", "").replace("'", "")

#Booleans
bool_true = CaselessLiteral("True")
bool_false = CaselessLiteral("False")
bools = bool_true + bool_false

#Parenthesis and Quotes
openParen = Literal("(").suppress()
closeParen = Literal(")").suppress()
openBracket = Literal("[").suppress()
closeBracket = Literal("]").suppress()
Quote = Literal('"').suppress()

#Optional comma for some lists
ocomma = Optional(",").suppress()
