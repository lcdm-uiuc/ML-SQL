"""
Defines the parsing for the elastic net algorithm for intended use in regression
"""
from pyparsing import oneOf, Literal, Optional, Word
from ..grammer import numbers, openParen, closeParen, ocomma
from .._constants import decimal

def define_elastic():
    elasticPhrase = oneOf(["elastic", "Elastic", "ELASTIC"])

    #Definitions for options of elastic net (lambda and alpha)
    alpha_phrase = (Literal("alpha") + Literal("=")).suppress()
    alpha = Optional(alpha_phrase + decimal.setResultsName("alpha"), default = .5)

    lambda_phrase = (Literal("lambda") + Literal("=")).suppress()
    lam = Optional(lambda_phrase + decimal.setResultsName("lambda"), default = 1)

    #Compositions
    elastic = elasticPhrase + Optional(openParen + alpha + ocomma + lam + closeParen)

    return(elastic)