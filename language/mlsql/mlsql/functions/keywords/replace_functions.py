"""
imputes missing values in a dataframe

Parameters:
    dataframe: pandas dataframe to do imputation on
    list_replaces: list of doubles
        index 0: index of column to do imputation
        index 1: missing value
        index 2: imputation strategy
"""
import .preprocessing.impute_functions 
def handle_replace(dataframe, list_replaces):
    for item in list_replaces:
        colNum = item[0]
        misingVal = item[1]
        strategy = item[2]

        return 0
