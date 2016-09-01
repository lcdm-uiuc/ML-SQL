import pandas as pd
import seaborn as sns
from sklearn.preprocessing import Imputer
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.ensemble import RandomForestRegressor
import re
"""
impute_missing()
Parameters:
  data: Dataframe to impute missing values on
  columns: Columns to impute. If None, impute all columns
  impute_strategy: What to replace missing values with
     Options:
      Imputer Class
      'mode'
      'median' - numerical
      'mean' - numerical
      Custom Functions
      'remove'
      'dummy'
      'rand_forest_reg'
Returns: Imputed dataframe
"""
def impute_missing(data, columns=None, impute_strategy='mode', missing_values='NaN'):
    datacopy = data
    dummy_val = 'U0'
    cols_to_impute = list()
    missing_values = re.escape(missing_values)
    if columns == None:
        cols_to_impute = _find_cols_with_missing_vals(data, missing_values)
    else:
        cols_to_impute = columns
    if not cols_to_impute:
        return datacopy
    if impute_strategy == 'mode':
        for col in cols_to_impute:
            modeVal = data[col].mode()
            datacopy[col] = _fill_col(data[col], missing_values, modeVal[0])
        return datacopy
    elif impute_strategy == 'mean':
        for col in cols_to_impute:
            if data[col].dtype != 'object':
                meanVal = data[col].mean()
                datacopy[col] = _fill_col(data[col], missing_values, meanVal)
            else:
                datacopy[col] = _fill_col(data[col], missing_values, dummy_val)
        return datacopy
    elif impute_strategy == 'median':
        for col in cols_to_impute:
            if data[col].dtype != 'object':
                medianVal = data[col].median()
                datacopy[col] = _fill_col(data[col], missing_values, medianVal)
            else:
                datacopy[col] = _fill_col(data[col], missing_values, dummy_val)
        return datacopy
    elif impute_strategy == 'drop column':
        return _remove_columns(data, cols_to_impute)
    elif impute_strategy == 'maximum':
        for col in cols_to_impute:
            if data[col].dtype != 'object':
                maxVal = max(data[col])
                datacopy[col] = _fill_col(data[col], missing_values, maxVal)
            else:
                datacopy[col] =  _fill_col(data[col], missing_values, dummy_val)
        return datacopy
    elif impute_strategy == 'minimum':
        for col in cols_to_impute:
            if data[col].dtype != 'object':
                minVal = min(data[col])
                datacopy[col] = _fill_col(data[col], missing_values, minVal)
            else:
                datacopy[col] = _fill_col(data[col], missing_values, dummy_val)
        return datacopy
    elif impute_strategy == 'dummy':
        for col in cols_to_impute:
            if data[col].dtype != 'object':
                datacopy[col] = _fill_col(data[col], missing_values, 0)
            else:
                datacopy[col] = _fill_col(data[col], missing_values, dummy_val)
        return datacopy
  # Do some more research on this before implementing
    elif impute_strategy == 'rand_forest_reg':
        print("RANDOM FOREST REGRESSOR NOT IMPLEMENTED NO IMPUTATION HAPPENED")
        return datacopy
    else:
        print ("REPLACE COMMAND NOT RECOGNIZED NO IMPUTATION HAPPENED")
        return datacopy

"""
remove_columns()
Parameters:
  data: dataframe to remove columns
  delete_list: list of names of columns to delete
Returns:
  Dataframe with deleted columns
"""
def _remove_columns(data, delete_list):
  for col in delete_list:
      del data[col]
  return data

def _find_cols_with_missing_vals(data=None, missing_values= 'NaN'):
    cols_to_impute = list()
    if missing_values == 'NaN':
        for col in data.columns:
            if data[col].isnull().values.any():
                cols_to_impute.append(col)
    else:
        for col in data.columns:
            if data[col].dtype == 'object':
                if data[col].str.contains(missing_values).any():
                    cols_to_impute.append(col)
    return cols_to_impute

def _fill_col(column, missing_values, replace_val):
    ret = column
    if missing_values == 'NaN':
        ret = column.fillna(replace_val)
    else:
        ret = column.replace(missing_values, replace_val, regex = True)
    return ret
