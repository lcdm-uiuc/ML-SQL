import sys

sys.path.insert(0, 'keywords/')

import read
import split
import regression
import classify

#Combining READ and SPLIT keywords into one clause for combined use
read_split = read + split
read_split_classify = read + split + classify
read_split_classify_regression = read + split + classify + regression
