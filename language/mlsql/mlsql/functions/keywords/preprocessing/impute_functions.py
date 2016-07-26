import pandas as pd
import seaborn as sns
from sklearn.preprocessing import Imputer
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.ensemble import RandomForestRegressor

"""
impute_missing()
Parameters:
  data: Dataframe to impute missing values on
  columns: Columns to impute. If None, impute all columns
  impute_strategy: What to replace missing values with
     Options: 
      Imputer Class
      'most frequent'
      'median'
      'mean'
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
  if columns == None:
    cols_to_impute = _find_cols_with_missing_vals(data, missing_values)
  else:
    cols_to_impute = columns
  if impute_strategy == 'mode':
    for col in cols_to_impute:
      modeVal = data[col].mode()
      datacopy[col] = data[col].fillna(modeVal[0])
    return datacopy
  elif impute_strategy == 'mean':
    for col in cols_to_impute:
      meanVal = data[col].mean()
      datacopy[col] = data[col].fillna(meanVal)
    return datacopy
  elif impute_strategy == 'median':
    for col in cols_to_impute:
      medianVal = data[col].median()
      datacopy[col] = data[col].fillna(medianVal)
    return datacopy
  elif impute_strategy == 'drop column':
    return _remove_columns(data, cols_to_impute)
  elif impute_strategy == 'maximum':
    for col in cols_to_impute:
      maxVal = max(data[col])
      datacopy[col] = data[col].fillna(maxVal)
    return data
  elif impute_strategy == 'minimum':
    for col in cols_to_impute:
      minVal = min(data[col])
      datacopy[col] = data[col].fillna(minVal)
    return data
  elif impute_strategy == 'dummy':
    return data.replace(missing_values, dummy_val) 
  # Do some more research on this before implementing
  elif impute_strategy == 'rand_forest_reg':
    print("RANDOM FOREST REGRESSOR NOT IMPLEMENTED NO IMPUTATION HAPPENED")
    return None
  else:
    print ("REPLACE COMMAND NOT RECOGNIZED")
    return None

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

def _find_cols_with_missing_vals(data= None, missing_values= 'NaN'):
  cols_to_impute = list()
  if missing_values == 'NaN':
    for col in f.columns:
      if(data[col].isnull().values.any()):
        cols_to_impute.append(col)
  else:
    for col in f.columns:
      if missing_values in data[col]:
        cols_to_impute.append(col)
  return cols_to_impute


