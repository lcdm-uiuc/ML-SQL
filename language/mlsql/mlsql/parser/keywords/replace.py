from .grammer import *
from ._constants import choice_columns, column
from pyparsing import CaselessLiteral, Literal, oneOf, Optional, Word, OneOrMore, MatchFirst, Group, delimitedList

def define_replace():
    #define so that there can be multiple verisions of Replace
    replaceKeyword = oneOf(["Replace", "REPLACE"]).setResultsName("replace")

    #Define the columns that need to be replaced
    replace_cols = choice_columns.setResultsName("replaceColumns")

    #defines possible values or optional replacement words 
    value = Quote + Word(everythingWOQuotes) + Quote
    options = _replace_options()
    replacements = MatchFirst(options + [value]).setResultsName("replaceValue")

    #single group for column replace
    single_replacement = openParen + replace_cols + ocomma + replacements + closeParen
    group_replacements = delimitedList(single_replacement, delim = ",")

    #putting it all together to create replacement
    replace = Optional(replaceKeyword + group_replacements)

    return replace



def _replace_options():
    """
    Defines different word replacement strategies for missing values
    - mean, max, min, median
    - drop column
    - drop row
    """
    mean = CaselessLiteral("mean")
    median = CaselessLiteral("median")
    maximum = CaselessLiteral("maximum")
    minimum = CaselessLiteral("minimum")
    dropC = CaselessLiteral("drop column")
    dropR = CaselessLiteral("drop row")

    #Combine all possible options
    options = [mean, median, maximum, minimum, dropC,dropR]

    return options