from .grammer import *
from pyparsing import delimitedList, MatchFirst, Word

#Define list of column numbers in brackets or single column number
column = Word(numbers)
_columns = delimitedList(column, delim = ",")
_list_columns = openBracket + _columns + closeBracket
choice_columns = MatchFirst([column,_list_columns]).setResultsName("replaceColumns")