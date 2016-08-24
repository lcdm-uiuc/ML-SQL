import mlsql
from mlsql import execute

query = 'READ "data/train.csv" (separator = ",", header = 0) REPLACE ("NaN", "mode") SPLIT (train = .8, test = 0.2) CLASSIFY (predictors = [1,3,4,5,6,7,8,9,10,11,12], label = 2, algorithm = forest)'
execute(query)
