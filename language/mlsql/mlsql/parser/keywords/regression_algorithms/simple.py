from pyparsing import oneOf, Literal, Optional, Word
from ..grammer import numbers, openParen, closeParen

def define_simple():
    simplePhrase = oneOf(["simple", "SIMPLE", "Simple"])

    #Compositions
    simple = simplePhrase + Optional(openParen + closeParen)

    return simple