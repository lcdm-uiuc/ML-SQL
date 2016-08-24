import mlsql
from mlsql import execute

query = 'READ "data/census.csv" (separator = ",", header = 0) REPLACE ("NaN", "mode") SPLIT (train = .8, test = 0.2) CLASSIFY (predictors = [1,2,3,4,5,6,7,8,9,10,11,12,13,14], label = 15, algorithm = logistic)'
execute(query)
