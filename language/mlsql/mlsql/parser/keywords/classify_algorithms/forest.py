"""
Defines the parsing for the random forest algorithm for intended use in classification
"""
from pyparsing import oneOf, Literal, Optional, Word
from ..grammer import numbers, openParen, closeParen
from .._constants import decimal

def define_forest():
    forestPhrase = oneOf(["forest", "Forest", "FOREST"])

    #Definitions for options of random forest (# of trees)
    trees_phrase = (Literal("trees") + Literal("=")).suppress()

    trees = Optional(trees_phrase + decimal.setResultsName("trees"), default = 5)

    #Compositions
    forest = forestPhrase + Optional(openParen + trees + closeParen)

    return(forest)