from .keywords.read import define_read
from .keywords.split import define_split
from .keywords.regression import define_regression
from .keywords.classify import define_classify
from .keywords.replace import define_replace
from .keywords.load import define_load
from pyparsing import restOfLine, MatchFirst

def mlsqlparser():
    #Define all keywords
    LOAD = define_load()
    READ = define_read()
    SPLIT = define_split()
    REGRESSION = define_regression()
    CLASSIFY = define_classify()
    REPLACE = define_replace()

    #Define comment
    comment = _define_comment()

    #Combining READ and SPLIT keywords into one clause for combined use
    read_split = READ + SPLIT
    read_split_classify = READ + SPLIT + CLASSIFY
    read_split_classify_regression = READ + SPLIT + CLASSIFY + REGRESSION
    read_replace_split_classify_regression = READ + REPLACE + SPLIT + CLASSIFY + REGRESSION

    load_read_replace_split_classify_regression = MatchFirst([read_replace_split_classify_regression, LOAD])

    return load_read_replace_split_classify_regression.ignore(comment)



def _define_comment(comment = "--"):
    oracleSqlComment = comment + restOfLine
    return oracleSqlComment