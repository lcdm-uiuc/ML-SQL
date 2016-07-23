from .grammer import *
from ._constants import decimal
from pyparsing import oneOf, Literal, Word, Optional, Combine

def define_split():
	#define so that there can be multiple verisions of Split
	splitKeyword = oneOf(["Split", "SPLIT"]).setResultsName("split")

	#Phrases used to organize splits
	trainPhrase = (Literal("train") + Literal("=")).suppress()
	testPhrase = (Literal("test") + Literal("=")).suppress()
	valPhrase = (Literal("validation") + Literal("=")).suppress()

	#train, test, validation split values
	trainS = decimal.setResultsName("train_split")
	testS = decimal.setResultsName("test_split")
	valS = Optional(decimal, default = 0).setResultsName("validation_split")

	#Compose phrases and values together 
	training = trainPhrase + trainS
	testing = testPhrase + testS
	val = valPhrase + valS

	#Creating Optional Split phrases
	split = Optional(splitKeyword + openParen + training + ocomma + testing + ocomma + val + closeParen)

	return split
