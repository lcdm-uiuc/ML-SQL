from pyparsing import oneOf, Literal, Optional, Word
from ..grammer import numbers, openParen, closeParen

def define_lasso():
    lassoPhrase = oneOf(["lasso", "Lasso", "LASSO"])

    #Options

    #Compositions
    lasso = lassoPhrase + Optional(openParen + closeParen)

    return lasso