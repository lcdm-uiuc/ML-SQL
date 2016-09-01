import mlsql
from mlsql import execute

query = 'READ "data/auto.csv" (separator = "\s+", header = None)\
 REPLACE ("?", "mode") SPLIT (train = .8, test = .2, validation = .0)\
  REGRESS (predictors = [2,3,4,5,6,7,8], label = 1, algorithm = simple)'

execute(query, verbose=False)
