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
  # Use the Imputer class to impute if the strategy is most_frequent, median or mean 
  if impute_strategy == 'mode' or impute_strategy == 'median' or impute_strategy == 'mean':
    imputer = ImputeColumns(columns=columns, impute_strategy=impute_strategy, missing_vals=missing_values)
    return imputer.fit_transform(data)
  
  # Use custom functions
  else:
    if impute_strategy == 'drop column':
      if columns == None:
        cols_to_impute= list()
        for col in data.columns:
          if missing_values in data[col]:
            cols_to_impute.append(col)
      else:
        cols_to_impute = columns
      return _remove_columns(data, cols_to_remove)

    if impute_strategy == 'maximum':
      if columns == None:
        cols_to_impute= list()
        for col in data.columns:
          if missing_values in data[col]:
            cols_to_impute.append(col)
      else:
        cols_to_impute = columns

      return 0
    if impute_strategy == 'minimum':
      return 0
    if impute_strategy == 'dummy':
      return data.replace(missing_values, dummy_val) 

    # Do some more research on this before implementing
    if impute_strategy == 'rand_forest_reg':
      print("RANDOM FOREST REGRESSOR NOT IMPLEMENTED NO IMPUTATION HAPPENED")
      return None

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


def _find_cols_with_missing_vals(df, missing_vals):
  return list()
