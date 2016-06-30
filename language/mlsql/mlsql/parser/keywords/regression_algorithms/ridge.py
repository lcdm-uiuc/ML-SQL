from pyparsing import oneOf, Literal, Optional, Word
from ..grammer import numbers, openParen, closeParen

def define_lasso():
    ridgePhrase = oneOf(["ridge", "Ridge", "RIDGE"])

    #Options

    #Compositions
    ridge = ridgePhrase + Optional(openParen + closeParen)

    return ridge