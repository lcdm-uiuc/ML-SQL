"""
Functions/objects to abstract some data cleaning procedures 
Maybe seperate encoding and imputing into own files 
"""
import pandas as pd
import seaborn as sns

def removeColumns(data, delete_list):
  for col in delete_list:
      del data[col]
  return data


from sklearn.preprocessing import LabelEncoder
from sklearn.base import BaseEstimator, TransformerMixin

# Encodes Categorical variables to be numerical values 
# Usage: 
# encoder = EncodeCategorical()
# encoder.fit_transform(data)

class EncodeCategorical(BaseEstimator, TransformerMixin):
  def __init__(self, columns=None):
      self.columns = columns
      self.encoders = None
  def fit(self, data, target=None):
      categorical_features = list();
      for col in data.columns:
          if data[col].dtype == 'object':
              categorical_features.append(col)
      self.columns = categorical_features;
      self.encoders = {
          column:LabelEncoder().fit(data[column])
          for column in self.columns
      }
      return self
  def transform(self, data):
      output = data.copy()
      for column, encoder in self.encoders.items():
          output[column] = encoder.transform(data[column])
      return output

# Makes an instance of the encoder class and returns an encoded version of the dataframe
def encode_categorical(data, columns=None):
  encoder=EncodeCategorical(columns=columns)
  return encoder.fit_transform(data)


# Imputes Missing values
# Usage:
# imputer = ImputeColumns(impute_strategy, missing_vals)
# imputer.fit_transform(data)
from sklearn.preprocessing import Imputer
from sklearn.base import BaseEstimator, TransformerMixin

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


