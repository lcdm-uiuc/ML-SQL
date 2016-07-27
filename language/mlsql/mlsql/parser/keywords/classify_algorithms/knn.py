"""
Defines the parsing for the K nearest neighbors algorithm for intended use in classification
"""
from pyparsing import oneOf, Literal, Optional, Word
from ..grammer import numbers, openParen, closeParen
from .._constants import decimal

def define_knn():
    knnPhrase = oneOf(["knn", "Knn", "KNN"])

    #Definitions for options of svm
    neighbors_phrase = (Literal("neighbors") + Literal("=")).suppress()

    n = Optional(neighbors_phrase + decimal.setResultsName("neighbors"), default = 3)

    #Compositions
    knn = knnPhrase + Optional(openParen + n + closeParen)

    return(knn)