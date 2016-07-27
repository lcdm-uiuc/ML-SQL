from .grammer import *
from ._constants import choice_columns, column
from pyparsing import Literal, Keyword, Optional, Word, MatchFirst
from .regression_algorithms import simple, lasso, ridge, elastic

def define_regress():
    #Algorithm keyword definitions
    algoPhrase = (Literal ("algorithm") + Literal("=")).suppress()
    
    #Algorithms 
    simpled = simple.define_simple()
    lassod = lasso.define_lasso()
    ridged = ridge.define_ridge()
    elasticd = elastic.define_elastic()
    algo = algoPhrase + MatchFirst([simpled, lassod, ridged, elasticd]).setResultsName("algorithm")

    #define so that there can be multiple verisions of Regression
    regressKeyword = Keyword("regress", caseless = True).setResultsName("regress")

    #Phrases to organize predictor and label column numbers
    predPhrase = (Literal("predictors") + Literal("=")).suppress()
    labelPhrase = (Literal("label") + Literal("=")).suppress()

    #define predictor and label column numbers
    predictorsDef = choice_columns.setResultsName("predictors")
    labelDef = column.setResultsName("label")

    #combine phrases with found column numbers
    preds = predPhrase + predictorsDef
    labels = labelPhrase + labelDef

    regress = Optional(regressKeyword + openParen + preds + ocomma + labels + ocomma + algo + closeParen)

    return regress
