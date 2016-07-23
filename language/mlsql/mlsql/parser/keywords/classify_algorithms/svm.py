from pyparsing import oneOf, Literal, Optional, Word
from ..grammer import numbers, openParen, closeParen
from .._constants import decimal

def define_svm():
    svmPhrase = oneOf(["svm", "SVM"])

    #Definitions for options of svm
    gamma_literal = (Literal("gamma") + Literal("=")).suppress()
    C_literal = (Literal("C") + Literal("=")).suppress()

    gamma = Optional(gamma_literal + decimal.setResultsName("svm_gamma"), default = 1)
    C = Optional(gamma_literal + decimal.setResultsName("svm_C"), default = 1)

    #Compositions 
    svm = svmPhrase + Optional(openParen + gamma + C + closeParen)

    return(svm)