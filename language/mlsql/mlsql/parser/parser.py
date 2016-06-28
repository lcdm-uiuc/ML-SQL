from .keywords.read import define_read
from .keywords.split import define_split
from .keywords.regression import define_regression
from .keywords.classify import define_classify

def mlsqlparser():
	#Define all keywords
	READ = define_read()
	SPLIT = define_split()
	REGRESSION = define_regression()
	CLASSIFY = define_classify()

	#Combining READ and SPLIT keywords into one clause for combined use
	read_split = READ + SPLIT
	read_split_classify = READ + SPLIT + CLASSIFY
	read_split_classify_regression = READ + SPLIT + CLASSIFY + REGRESSION

	return read_split_classify_regression
