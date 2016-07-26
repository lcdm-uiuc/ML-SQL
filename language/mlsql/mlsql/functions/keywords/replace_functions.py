"""
imputes missing values in a dataframe

Parameters:
    dataframe: pandas dataframe to do imputation on
    list_replaces: list of doubles
        index 0: index of column to do imputation
        index 1: missing value
        index 2: imputation strategy
"""
from .preprocessing.impute_functions import impute_missing
def handle_replace(dataframe, list_replaces):
    ret = dataframe
    for item in list_replaces:
        colName = dataframe.columns[item[0]]
        missingVal = item[1]
        strategy = item[2]
        ret = impute_missing(data=dataframe, columns = [colName], impute_strategy=strategy, missing_values = missingVal)

    return ret