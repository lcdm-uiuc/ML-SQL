from .grammer import *
from .classify_algorithms import svm, logistic
from pyparsing import Literal, oneOf, Optional, Word, OneOrMore, MatchFirst

def define_classify():
	#Algorithm Definitions
	algoPhrase = (Literal ("algorithm") + Literal("=")).suppress()

	svmd = svm.define_svm()
	logd = logistic.define_logistic()
	algo = algoPhrase + MatchFirst([svmd, logd]).setResultsName("algorithm")

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
