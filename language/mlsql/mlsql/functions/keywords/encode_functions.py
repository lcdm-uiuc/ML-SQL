import pandas as pd
import seaborn as sns
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

