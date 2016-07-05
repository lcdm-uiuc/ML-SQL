import pandas as pd
import seaborn as sns
from sklearn.preprocessing import Imputer
from sklearn.base import BaseEstimator, TransformerMixin

# Imputes Missing values
# Usage:
# imputer = ImputeColumns(impute_strategy, missing_vals)
# imputer.fit_transform(data)
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

# Makes an instance of the imputer class and returns an imputed dataframe
def impute_missing(data, columns, impute_strategy='most_frequent', missing_values='NaN'):
  imputer = ImputeColumns(columns=columns, impute_strategy=impute_strategy, missing_vals=missing_values)
  return imputer.fit_transform(data)

def removeColumns(data, delete_list):
  for col in delete_list:
      del data[col]
  return data
