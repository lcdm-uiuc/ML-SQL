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
___

## Language

### READ

(Model phase)
___

### REPLACE
(Model phase)
___

### CLASSIFY
(Model phase)
___

### REGRESS
(Model phase)
___

### CLUSTER
(Model phase)
___

### LOAD
(Model phase)
___

### SPLIT
(Apply phase)
___

### APPLY
(Apply phase)
___

### CALCULATE
(Metrics Phase)
___

### SAVE
(Model phase)