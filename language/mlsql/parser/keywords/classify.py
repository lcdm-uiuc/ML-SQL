from grammer import *
from pyparsing import Literal, oneOf, Optional, Word, OneOrMore, MatchFirst

def define_classify():
	#Algorithm Definitions
	algoPhrase = (Literal ("algorithm") + Literal("=")).suppress()
	svmPhrase = oneOf(["svm", "SVM"])
	logPhrase = oneOf(["logistic", "Logistic", "LOGISTIC"])

	#Options for classifiers

	#Compositions
	svm = svmPhrase + Optional(openParen + closeParen)
	log = logPhrase + Optional(openParen + closeParen)
	algo = algoPhrase + MatchFirst([svm, log]).setResultsName("algorithm")

	#define so that there can be multiple verisions of Classify
	classifyKeyword = oneOf(["Classify", "CLASSIFY"]).suppress()

	#Phrases to organize predictor and label column numbers
	predPhrase = (Literal("predictors") + Literal("=")).suppress()
	labelPhrase = (Literal("label") + Literal("=")).suppress()

	#define predictor and label column numbers
	predictorsDef = OneOrMore(Word(numbers) + ocomma).setResultsName("predictors")
	labelDef = Word(numbers).setResultsName("label")

	#combine phrases with found column numbers
	preds = predPhrase + openParen + predictorsDef + closeParen
	labels = labelPhrase + labelDef

	classify = Optional(classifyKeyword + openParen + preds + ocomma + labels + ocomma + algo + closeParen)

	return classify
