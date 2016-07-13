from .grammer import *
from pyparsing import delimitedList, MatchFirst, Word

def _convert_int(tokens):
    """
    Converts a string valued integer to a simple integer so that it does not
    manually have to be preformed on the function side. 
    """
    val = int(tokens[0])
    return val

#Define list of column numbers in brackets or single column number
column = Word(numbers).setParseAction(_convert_int)
_columns = delimitedList(column, delim = ",")
_list_columns = openBracket + _columns + closeBracket
choice_columns = MatchFirst([column,_list_columns]).setResultsName("replaceColumns")