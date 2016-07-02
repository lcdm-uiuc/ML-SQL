from pyparsing import oneOf, Literal, Optional, Word
from ..grammer import numbers, openParen, closeParen

def define_ridge():
    ridgePhrase = oneOf(["ridge", "Ridge", "RIDGE"])

    #Options

    #Compositions
    ridge = ridgePhrase + Optional(openParen + closeParen)

    return ridge