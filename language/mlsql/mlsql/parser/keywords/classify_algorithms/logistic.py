from pyparsing import oneOf, Literal, Optional, Word
from ..grammer import numbers, openParen, closeParen

logPhrase = oneOf(["logistic", "Logistic", "LOGISTIC"])

def define_logistic():
    logPhrase = oneOf(["logistic", "Logistic", "LOGISTIC"])

    #Definitions for options of svm
    lambda_phrase = (Literal("lambda") + Literal("=")).suppress()

    lam = Optional(lambda_phrase + Word(numbers).setResultsName("log_lambda"), default = 0)

    #Compositions
    log = logPhrase + Optional(openParen + lam + closeParen)

    return(log)