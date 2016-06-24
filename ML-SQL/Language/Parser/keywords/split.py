import grammer
from pyparsing import oneOf, Literal, Word, Optional, Combine

#define so that there can be multiple verisions of Split
splitKeyword = oneOf(["Split", "SPLIT"]).suppress()

#Phrases used to organize splits
trainPhrase = (Literal("train") + Literal("=")).suppress()
testPhrase = (Literal("test") + Literal("=")).suppress()
valPhrase = (Literal("validation") + Literal("=")).suppress()

#train, test, validation split values
trainS = Combine(Literal(".") + Word(numbers)).setResultsName("train_split")
testS = Combine(Literal(".") + Word(numbers)).setResultsName("test_split")
valS = Combine(Literal(".") + Word(numbers)).setResultsName("validation_split")

#Compose phrases and values together 
training = trainPhrase + trainS
testing = testPhrase + testS
val = valPhrase + valS

#Creating Optional Split phrase
ocomma = Optional(",").suppress()
split = Optional(splitKeyword + openParen + training + ocomma + testing + ocomma + val + closeParen)
