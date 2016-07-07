import pandas as pd
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.feature_extraction import DictVectorizer

# Encodes Categorical variables to be numerical values 
# Usage: 
# encoder = EncodeCategorical()
# encoder.fit_transform(data)
# For now, do not use since this does not work well with python3
# class EncodeCategorical(BaseEstimator, TransformerMixin):
#   def __init__(self, columns=None):
#       self.columns = columns
#       self.encoders = None
#   def fit(self, data, target=None):
#       categorical_features = list();
#       for col in data.columns:
#           if data[col].dtype == 'object':
#               categorical_features.append(col)
#       self.columns = categorical_features;
#       self.encoders = {
#           column:LabelEncoder().fit(data[column])
#           for column in self.columns
#       }
#       return self
#   def transform(self, data):
#       output = data.copy()
#       for column, encoder in self.encoders.items():
#           output[column] = encoder.transform(data[column])
#       return output


"""
encode_categorical()
  Encode categorical features using 1 dimensional encoding
  May need runtime improvements
Parameters:
  df: Dataframe to encode
  cols: Columns to encode. If None, then encode all object columns  
Returns:
  1 Dimensionally encoded dataframe
"""
def encode_categorical(df, cols=None):
  categorical = list()
  if cols is not None:
    categorical = cols
  else:
    for col in df.columns:
        if df[col].dtype == 'object':
            categorical.append(col)

  for feature in categorical:
      l = list(df[feature])
      s = set(l)
      l2 = list(s)
      numbers = list()
      for i in range(0,len(l2)):
          numbers.append(i)
      df[feature] = df[feature].replace(l2, numbers)
  return df

"""
encode_onehot()
  Encode categorical variables with one hot strategy
Taken from:
  https://gist.github.com/ramhiser/982ce339d5f8c9a769a0
Parameters:
  df: Dataframe to encode
  cols: Columns to encode. If None, then encode all object columns 
Returns:
  1 Hot encoded dataframe
"""
def encode_onehot(df, cols=None):
  categorical = list()
  if cols is not None:
    categorical = cols
  else:
    for feature in df.columns:
        if df[feature].dtype == 'object':
            categorical.append(feature)

  vec = DictVectorizer()
  vec_data = pd.DataFrame(vec.fit_transform(df[cols].to_dict(outtype='records')).toarray())
  vec_data.columns = vec.get_feature_names()
  vec_data.index = df.index

  df = df.drop(cols, axis=1)
  df = df.join(vec_data)
  return df



