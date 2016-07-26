import pandas as pd
import seaborn as sns
from sklearn.preprocessing import Imputer
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.ensemble import RandomForestRegressor


"""
Imputer Class
Usage:
imputer = ImputeColumns(impute_strategy, missing_vals)
imputer.fit_transform(data)
Parameters:
  impute_strategy:
    “mean”: replace missing values using the mean along the axis.
    “median”: replace missing values using the median along the axis.
    “most_frequent”: replace missing using the most frequent value along the axis.
  missing_vals: Typically for Pandas, NaN is used for missing values

"""
class ImputeColumns(BaseEstimator, TransformerMixin):

  # Constructor: Makes an instance of the custom imputer
  # Columns: Columns to impute, if None, then impute all columns
  # impute_strategy: Can be "mean", "median" or "most frequent"
  def __init__(self,columns=None, impute_strategy='mode', missing_vals='NaN'):
      self.columns = columns
      self.impute_strategy = impute_strategy
      if self.impute_strategy == 'mode':
        self.impute_strategy = 'most_frequent'
      self.missing_vals = missing_vals
      self.imputer = None
  def fit(self, data, target=None):
      if self.columns is None:
          self.columns = data.columns
      self.imputer = Imputer(missing_values= self.missing_vals, strategy=self.impute_strategy)
      self.imputer.fit(data[self.columns])
      return self

  def transform(self, data):
      output = data.copy()
      output[self.columns] = self.imputer.transform(output[self.columns])
      return output

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
def impute_missing(data, columns, impute_strategy='mode', missing_values='NaN'):
  dummy_val = 'U0'
  cols_to_impute = list()
  if columns == None:
    cols_to_impute = _find_cols_with_missing_vals(data)
  else:
    cols_to_impute = columns
  if impute_strategy == 'mode':
    for col in cols_to_impute:
      modeVal = data[col].mode()
      data[col].fillna(modeVal)
    return data
  elif impute_strategy == 'mean':
    for col in cols_to_impute:
      meanVal = data[col].mean()
      data[col].fillna(meanVal)
    return data
  elif impute_strategy == 'median':
    for col in cols_to_impute:
      medianVal = data[col].median()
      data[col].fillna(medianVal)
    return data
  elif impute_strategy == 'drop column':
    return _remove_columns(data, cols_to_impute)
  elif impute_strategy == 'maximum':
    for col in cols_to_impute:
      maxVal = max(data[col])
      data[col].fillna(maxVal)
    return data
  elif impute_strategy == 'minimum':
    for col in cols_to_impute:
      minVal = min(data[col])
      data[col].fillna(minVal)
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

