from .grammer import *
from ._constants import choice_columns, column
from pyparsing import CaselessLiteral, Literal, oneOf, Optional, Word, OneOrMore, MatchFirst, Group, delimitedList

def define_replace():
    #define so that there can be multiple verisions of Replace
    replaceKeyword = oneOf(["Replace", "REPLACE"]).setResultsName("replace")

    #Define the columns that need to be replaced
    replace_cols = choice_columns.setResultsName("replaceColumns")

    #Define value that needs replacing
    replace_missing = Quote + Word(everythingWOQuotes).setResultsName("replaceIdentifier") + Quote

    #defines possible values or optional replacement words 
    value = Quote + Word(everythingWOQuotes) + Quote
    options = _replace_options()
    replacements = MatchFirst(options + [value]).setResultsName("replaceValue")

    #single group for column replace
    single_replacement = openParen + replace_cols + ocomma + replace_missing + ocomma + replacements + closeParen
    group_replacements = delimitedList(single_replacement)

    #temporary for a single demo (please remove later)
    temp_replacement = openParen + replace_missing + ocomma + replacements + closeParen

    #putting it all together to create replacement
    replace = Optional(replaceKeyword + temp_replacement)

    return replace



def _replace_options():
    """
    Defines different word replacement strategies for missing values
    - mean, max, min, median, mode
    - drop column
    - drop row
    """
    mean = CaselessLiteral("mean")
    median = CaselessLiteral("median")
    mode = CaselessLiteral("mode")
    maximum = CaselessLiteral("maximum")
    minimum = CaselessLiteral("minimum")
    dropC = CaselessLiteral("drop column")
    dropR = CaselessLiteral("drop row")

    #Combine all possible options
    options = [mean, median, mode, maximum, minimum, dropC,dropR]

    return options