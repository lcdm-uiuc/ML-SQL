import pandas as pd
import seaborn as sns
from sklearn.preprocessing import Imputer
from sklearn.base import BaseEstimator, TransformerMixin

# Imputes Missing values
# Usage:
# imputer = ImputeColumns(impute_strategy, missing_vals)
# imputer.fit_transform(data)
# impute_strategy:
#   “mean”: replace missing values using the mean along the axis.
#   “median”: replace missing values using the median along the axis.
#   “most_frequent”: replace missing using the most frequent value along the axis.

class ImputeColumns(BaseEstimator, TransformerMixin):

  # Constructor: Makes an instance of the custom imputer
  # Columns: Columns to impute, if None, then impute all columns
  # impute_strategy: Can be "mean", "median" or "most frequent"
  #   Potentially, we can explore using EM to fill in missing values
  def __init__(self,columns=None, impute_strategy='most_frequent', missing_vals='NaN'):
      self.columns = columns
      self.impute_strategy = impute_strategy
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

# If the strategy is 
def impute_missing(data, columns, impute_strategy='most_frequent', missing_values='NaN'):
  if impute_strategy == 'most_frequent' or impute_strategy == 'median' or impute_strategy == 'mean':
    imputer = ImputeColumns(columns=columns, impute_strategy=impute_strategy, missing_vals=missing_values)
    return imputer.fit_transform(data)

def removeColumns(data, delete_list):
  for col in delete_list:
      del data[col]
  return data
