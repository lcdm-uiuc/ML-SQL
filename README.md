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

Columns can either be specified as a single column (an integer) or as a list of columns which is a comma separated list of integers enclosed within brackets (ex. [1,2,3,...]).

___

### READ

(Model phase)

#### Description

Used to read in a raw data file from memory in order to create a machine learning model. The file must be in a csv like format.

#### Usage
```
READ "*file*" (header = ..., separator = "...")
```
*file* - specifies a memory location on the user's machine that can be read to create a machine learning model. The head of the data is displayed if the file is successfully read in. The path must be a relative path from the user's current directory. 

*header* - user specified parameter which indicates if there is a header present in the data. Possible options for this parameter are "True" (indicating there is a header on the first row), "False" (indicating there is no header), or any *int* (indicating that there is a header specification on a specific row other than the first row). By default this value will be False if it is not specified by the user. 

*separtor* - user specified parameter which indicates if there is a different type of separator to properly read in the file. By default this value is "," if not specified by the user.
___

### REPLACE
(Model phase)

#### Description

#### Options
___

### CLASSIFY
(Model phase)

#### Description

#### Options
___

### REGRESS
(Model phase)

#### Description

#### Options
___

### CLUSTER
(Model phase)

#### Description

#### Options
___

### LOAD
(Model phase)

#### Description

#### Options
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

#### Options