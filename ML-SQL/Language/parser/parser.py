import sys

sys.path.insert(0, 'keywords/')

import read
import split
import regression
import classify

def parser():
	#Define all keywords
	READ = read.define_read()
	SPLIT = split.define_split()
	REGRESSION = regression.define_regression()
	CLASSIFY = classify.define_classify()

	#Combining READ and SPLIT keywords into one clause for combined use
	read_split = READ + SPLIT
	read_split_classify = READ + SPLIT + CLASSIFY
	read_split_classify_regression = READ + SPLIT + CLASSIFY + REGRESSION

	return read_split_classify_regression
