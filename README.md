# ML-SQL

The ML-SQL repository was created to explore and research a SQL-like language for Machine Learning.

This repository was created by Neeraj Asthana and Michael Hao under Professor Robert J. Brunner at the University of Illinois at Urbana-Champaign. 

___

# ML-SQL Documentation

## Setup

Begin by cloning this repository using the following command:
```
git clone https://github.com/UI-DataScience/ML-SQL.git
```

Ensure that your machine is running Python 3 and that it contains the following requirements described in "requirements.txt". These requirements can be satisfied by running the following command after navigating to the "./language/mlsql":
```
pip install -r requirements.txt
```

Afterwards, navigate to the "./language/mlsql" directory and run the following command: 
```
sudo python3 setup.py develop
```
After running this command, the "mlsql" library will be accessible anywhere on your machine via Python.


## Access

Start a Python 3 shell by typing "python3" into the terminal. The name of the ML-SQL library is "mlsql" and can be imported by the simple command:
```
>>> import mlsql
```

ML-SQL has 2 important interfaces known as the repl and execute.
- execute: is a function that one can pass a valid ML-SQL string into. Execute is initialized and used in the following manner:
```
from mlsql import execute
execute(*some mlsql string*)
```
- repl: is a SQL-like SQL where one continually execute ML-SQL commands. Repl is initialized and used in the following manner:
```
from mlsql import repl
repl()
```

___
___

## ML-SQL Steps

The MLSQL language is broken down into 3 major steps (keywords specified below):

1. **Model Phase** - To build a machine learning model from a dataset or load/save a perviously built model from memory
	- LOAD, SAVE, READ, REPLACE, CLASSIFY, REGRESS, CLUSTER
1. **Apply Phase** - To apply a model to unknown data
	- APPLY, SPLIT
1. **Metrics Phase** - To get a numerical and graphical understanding of your data
	- CALCUATE, PLOT

The Apply and Metrics pahses build upon the Model phase to supply the user with useful results.

___

## Language

All strings (including all filepaths) must be placed in quotations ("..."). All integers must not be placed in quotes (including column numbers).

Commas are generally optionally in this language and for the most part can be omitted if the user chooses.

All columns are addressed by their column number (starting at 1) instead of by their names. Columns can either be specified as a single column (ex. an integer) or as a list of columns which is a comma separated list of integers enclosed within brackets (ex. [1,2,3,...]).

___

### READ

(Model phase)

#### Description

Used to read a raw data file from memory in order to create a machine learning model. The file must be in a csv like format.

#### Usage
```
READ "file" (header = ..., separator = "...")
```
*file* (required) - specifies a memory location on the user's machine that can be read to create a machine learning model. The head of the data is displayed if the file is successfully read in. The path must be a relative path from the user's current directory. 

*header* - user specified parameter which indicates if there is a header present in the data. Possible options for this parameter are "True" (indicating there is a header on the first row), "False" (indicating there is no header), or any *int* (indicating that there is a header specification on a specific row other than the first row). By default this value will be False if it is not specified by the user. 

*separator* - user specified parameter which indicates if there is a different type of separator to properly read in the file. By default this value is "," if not specified by the user.
___

### REPLACE
(Model phase)

#### Description

#### Options
___

### CLASSIFY
(Model phase)

Used to run a classification machine learning task on a set of data that has already been read in using the READ keyword. The user must specify which column(s) they want to use as predictors and which column they want as the label (only a single column). The user must also specify an algorithm that they want to use and optionally their hyperparamters. The following classification algorithms have been implemented and are available for use: SVM, Naive Bayes, Logistic Regression, Random Forest, and K-Nearest Neighbors (KNN). This keyword cannot be used with the CLUSTER and REGRESS keywords.

#### Usage
```
CLASSIFY (predictors = ..., label = ..., algorithm = ... (*options*))
```
*predictors* (required) - specifies the column numbers that will be used to generate a label. Generally they will be a list of column numbers in brackets. 

*label* (required) - specifies the column number that specifies the label or the item that is looking to be predicted. Generally this will be a single column number (integer). 

*algorithm* (required) - specifies the algorithm to be used in the classification task. Options for these algorithms can be specified inside of parenthesis after the algorithm declaration. A list of algorithms and their options can be found below. 

#### Algorithms

1. SVM (gamma = ..., C = ...) - **Support Vector machine** where *gamma* and *C* are optional integer parameters.
1. Logistic (lambda = ...) - **Logistic Regression** where *lambda* is an optional decimal parameter specifying reguarlization (0 as default).
1. Forest (trees = ...) - **Random Forest** where *trees* is an optional integer parameter specifying the number of trees to generate.
1. KNN (neighbors = ...) - **K-Nearest Neighbors** where *neighbors* is an optional integer parameter specifying the number of nearest neighbors to use in the classification.

___

### REGRESS
(Model phase)

Used to run a regression machine learning task on a set of data that has already been read in using the READ keyword. The user must specify which column(s) they want to use as predictors and which column they want as the label (only a single column). The user must also specify an algorithm that they want to use and optionally their hyperparamters. The following regression algorithms have been implemented and are available for use: Simple Linear Regression, Lasso, Ridge, and Elastic Net. This keyword cannot be used with the CLASSIFY and CLUSTER keywords.

#### Usage
```
REGRESS (predictors = ..., label = ..., algorithm = ... (*options*))
```
*predictors* (required) - specifies the column numbers that will be used to generate a label. Generally they will be a list of column numbers in brackets. 

*label* (required) - specifies the column number that specifies the label or the item that is looking to be predicted. Generally this will be a single column number (integer). 

*algorithm* (required) - specifies the algorithm to be used in the regression task. Options for these algorithms can be specified inside of parenthesis after the algorithm declaration. A list of algorithms and their options can be found below. 

#### Algorithms

1. Simple - **Simple Linear Regression**
1. Lasso (lambda = ...) - **Lasso Regression**  where *lambda* is an optional decimal parameter specifying reguarlization (1 as default).
1. Ridge (lambda = ...) - **Ridge Regression**  where *lambda* is an optional decimal parameter specifying reguarlization (1 as default).
1. Elastic (alpha = ..., lambda = ...) - **Elastic Net Regression** where *alpha* is a required decimal parameter specifying the the percentage allocated towards the lasso (must be between 0 and 1). *lambda* is an optional decimal parameter specifying reguarlization (1 as default).

___

### CLUSTER
(Model phase)

Used to run a clustering machine learning task on a set of data that has already been read in using the READ keyword. The user must specify which column(s) they want to use as predictors. Optionally, a user can also specify the column they want as the label (only a single column) if this is available in the dataset. The user must also specify an algorithm that they want to use and optionally their hyperparamters. The following clustering algorithms have been implemented and are available for use: K-Means. This keyword cannot be used with the CLASSIFY and REGRESS keywords.

#### Usage
```
CLUSTER (predictors = ..., label = ..., algorithm = ... (*options*))
```
*predictors* (required) - specifies the column numbers that will be used to generate a label. Generally they will be a list of column numbers in brackets. 

*label* - specifies the column number that specifies the label or the item that is looking to be predicted. Generally this will be a single column number (integer). For clustering tasks this parameter does not have to be specified as it may not be included in the dataset. If it is available, the label can be used to help score the test data if the data is split at all.

*algorithm* (required) - specifies the algorithm to be used in the clustering task. Options for these algorithms can be specified inside of parenthesis after the algorithm declaration. A list of algorithms and their options can be found below. 

#### Algorithms

1. KMeans (clusters = ...) - **K-Nearest Neighbors** where *clusters* is an optional integer parameter specifying the number of clusters to use (will default to 3).

___

### LOAD
(Model phase)

#### Description

Used to read a machine learning model from a file with a ".mlsql" extension. This file must contained a model that has already been created using ML-SQL and has been saved. This keyword cannot be used with any other keyword in the model phase (will cause errors). 

#### Usage
```
LOAD "file"
```
*file* (required) - specifies a memory location of a ".mlsql" file on the user's machine that contains a pretrained machine learning model. The path must be a relative path from the user's current directory. 

___

### SPLIT
(Apply phase)

#### Description

#### Options
___

### APPLY
(Apply phase)

#### Description

#### Options
___

### CALCULATE
(Metrics Phase)

#### Description

#### Options
___

### SAVE
(Model phase)

#### Description

Used to save a machine learning model to a ".mlsql" file. This keyword must be used with either the CLASSIFY, REGRESS, or CLUSTER keywords and should be placed at the end of a query.

#### Usage
```
SAVE "file"
```
*file* (required) - specifies a memory location for a ".mlsql" file on the user's machine. The current model will be saved to this location for future use or portability. The path must be a relative path from the user's current directory. 