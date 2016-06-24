import grammer
from pyparsing import Literal, oneOf, Optional, Word, OneOrMore, MatchFirst

#Algorithm Definitions
simplePhrase = oneOf(["simple", "SIMPLE", "Simple"])
lassoPhrase = oneOf(["lasso", "Lasso", "LASSO"])
ridgePhrase = oneOf(["ridge", "Ridge", "RIDGE"])

#Options for classifiers

#Compositions
simple = simplePhrase + Optional(openParen + closeParen)
lasso = lassoPhrase + Optional(openParen + closeParen)
ridge = ridgePhrase + Optional(openParen + closeParen)
algo = algoPhrase + MatchFirst([simple, lasso, ridge]).setResultsName("algorithm")

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
