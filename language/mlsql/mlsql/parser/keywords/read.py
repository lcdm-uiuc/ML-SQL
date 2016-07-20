from .grammer import *
from pyparsing import Word, Keyword, Optional, MatchFirst, Literal

def define_read():
    filename = Word(everything).setResultsName("filename")

    #define so that there can be multiple verisions of READ
    readKeyword = Keyword("read", caseless = True).setResultsName("read")

    #Define Read Optionals
    #header
    headerLiteral = (Literal("header") + Literal("=")).suppress()
    header_choices = MatchFirst([Word(numbers), bool_true, bool_false]).setResultsName("header")
    header = Optional(headerLiteral + header_choices)

    #separator
    separatorLiteral = (Literal("separator") + Literal("=")).suppress()
    definesep = Quote + Word(everythingWOQuotes + whitespace).setResultsName("sep") + Quote
    separator = Optional(separatorLiteral + definesep, default = ",")

    #Compose Read Optionals
    readOptions = Optional(openParen + separator + header + closeParen)

    read = readKeyword + filename + readOptions
    
    return read
