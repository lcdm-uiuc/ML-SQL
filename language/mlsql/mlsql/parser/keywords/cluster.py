"""
Defines all parser functionality for the CLUSTER keyword
"""
from .grammer import *
from ._constants import choice_columns
from .cluster_algorithms import kmeans
from pyparsing import Literal, oneOf, Optional, Word, Keyword, MatchFirst, delimitedList

def define_cluster():
	#Algorithm Definitions
    algoPhrase = (Literal ("algorithm") + Literal("=")).suppress()

    kmeansd = kmeans.define_kmeans()
    algo = algoPhrase + MatchFirst([kmeansd]).setResultsName("algorithm")

    #define so that there can be multiple verisions of Classify
    clusterKeyword = Keyword("cluster", caseless=True).setResultsName("cluster")

    #define predictor word to specify column numbers
    predPhrase = (Literal("predictors") + Literal("=")).suppress()
    predictorsDef = choice_columns.setResultsName("predictors")
    preds = predPhrase + predictorsDef

    cluster = Optional(clusterKeyword + openParen + preds + ocomma + algo + closeParen)

    return cluster