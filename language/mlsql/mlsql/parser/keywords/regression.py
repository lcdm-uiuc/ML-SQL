from .grammer import *
from pyparsing import Literal, oneOf, Optional, Word, OneOrMore, MatchFirst
from .regression_algorithms import simple, lasso, ridge

def define_regression():
    #Algorithm keyword definitions
    algoPhrase = (Literal ("algorithm") + Literal("=")).suppress()
    
    #Algorithms 
    simpled = simple.define_simple()
    lassod = lasso.define_lasso()
    ridged = ridge.define_ridge()
    algo = algoPhrase + MatchFirst([simpled, lassod, ridged]).setResultsName("algorithm")

    #define so that there can be multiple verisions of Regression
    regressionKeyword = oneOf(["Regression", "REGRESSION"]).suppress()

    #Phrases to organize predictor and label column numbers
    predPhrase = (Literal("predictors") + Literal("=")).suppress()
    labelPhrase = (Literal("label") + Literal("=")).suppress()

    #define predictor and label column numbers
    predictorsDef = OneOrMore(Word(numbers) + ocomma).setResultsName("predictors")
    labelDef = Word(numbers).setResultsName("label")

    #combine phrases with found column numbers
    preds = predPhrase + openParen + predictorsDef + closeParen
    labels = labelPhrase + labelDef

    regression = Optional(regressionKeyword + openParen + preds + ocomma + labels + ocomma + algo + closeParen)

    return regression
