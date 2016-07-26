"""
Defines all parser functionality for the SAVE Keyword
"""
from .grammer import *
from pyparsing import Word, Keyword, Optional, MatchFirst, Literal

def define_save():
    filename = Word(everythingWOQuotes).setResultsName("savefile")

    #define so that there can be multiple verisions of SAVE
    saveKeyword = Keyword("save", caseless = True).setResultsName("save")

    save = Optional(saveKeyword + Quote + filename + Quote)
    
    return save