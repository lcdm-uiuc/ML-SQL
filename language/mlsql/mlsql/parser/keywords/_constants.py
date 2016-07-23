from .grammer import *
from pyparsing import delimitedList, MatchFirst, Word, Regex

#Define list of column numbers in brackets or single column number
column = Word(numbers)
_columns = delimitedList(column, combine = True)
_list_columns = openBracket + _columns + closeBracket
choice_columns = MatchFirst([column,_list_columns])

#Define a numerical values
decimal = Regex(r'\d*\.?\d*')