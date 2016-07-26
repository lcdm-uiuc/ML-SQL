from .keywords.read import define_read
from .keywords.split import define_split
from .keywords.regress import define_regress
from .keywords.classify import define_classify
from .keywords.replace import define_replace
from .keywords.load import define_load
from .keywords.cluster import define_cluster
from .keywords.save import define_save
from pyparsing import restOfLine, MatchFirst

def mlsqlparser():
    #Define all keywords
    LOAD = define_load()
    READ = define_read()
    SPLIT = define_split()
    REGRESS = define_regress()
    CLASSIFY = define_classify()
    CLUSTER = define_cluster()
    REPLACE = define_replace()
    SAVE = define_save()

    #Define comment
    comment = _define_comment()

    #Combining READ and SPLIT keywords into one clause for combined use
    read_split = READ + SPLIT
    read_split_classify = READ + SPLIT + CLASSIFY
    read_split_classify_regress = READ + SPLIT + CLASSIFY + REGRESS
    read_replace_split_classify_regress = READ + REPLACE + SPLIT + CLASSIFY + REGRESS
    read_replace_split_classify_regress_cluster = READ + REPLACE + SPLIT + CLASSIFY + REGRESS + CLUSTER
    read_replace_split_classify_regress_cluster_save = READ + REPLACE + SPLIT + CLASSIFY + REGRESS + CLUSTER + SAVE

    load_read_replace_split_classify_regress_cluster_save = MatchFirst([read_replace_split_classify_regress_cluster_save, LOAD])

    return load_read_replace_split_classify_regress_cluster_save.ignore(comment)



def _define_comment(comment = "--"):
    oracleSqlComment = comment + restOfLine
    return oracleSqlComment
