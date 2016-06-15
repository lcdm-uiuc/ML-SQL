# ML-SQL Language Structures

___

This document specifies a preliminary set of keywords that we can use to create a SQL like language for machine learning. There are a few keywords that are used for all machine learning tasks, however, some there is a slight difference between supervised (classification and regression) and unsupervised algorithms (clustering, etc.) which can be seen below. 

These keywords were formed based off examples dataflows included in this repository as well as prior machine learning projects. 

At the bottom I also include a few examples of regression and clustering tasks written in this language. 

### Assumptions

I will assume we start with a datafile (ex. already have the .csv, .txt, .data, etc.) downloaded locally on our computer. From here our language will be able to perform machine learning tasks on these datasets.

___
___

## Universal

### READ (*file*, *separator*, *header*, *column_names*)

Reads *file* into a matrix to be operated on. The file should be in some CSV like format with values separated by the *separtor*. Additionally the presence of a *header* can be specified along with names for *column_names*.

### REPLACE ([*column_name*, method=*{mean, NaN, nearest_neighbor, etc.}*])

Changes missing or NaN values in specified columns by column mean, 0, NaN, etc. Specified as a list of tuples with the *column_name* and the method*.

### TRANSFORM (*mean_scale*, *variance_scale*, *PCA*=?, *combine*, etc.)

Used to scale, combine, or modify the data that is read in.

### SPLIT (*train*, *test*, *validation*)

Splits the data into training, testing, and validation sets for model building. *train*, *test*, and *validation* can either be percentages that sum to 1 or hard coded values that specify the relative sizes of each of the sets.

### EVALUATE (*deviance*, *r-squared*, *residuals*, etc.)

Defines the metrics that the user wants to see to evaluate their machine learning model.

### VISUALIZE (*scatter_plot*, *diagnostics*, etc)

Visualizations or graphs the user wants to see to evaluate model performance.

___

## Classification/Regression

### CLASSIFY (predictors, labels, algorithm={*svm*, *regression*, *lasso*, *ridge*, etc.})

Specifies the supervised machine learning *algorithm* being used to classify data. The *predictors* and *labels* are also specified using column names or indices.

### USING (*lambda*, *c*, etc.)

Used to specify hyperparameters or values for some machine learning algorithms.
    
___

## Clustering

### CLUSTER (columns, algorithm={*k-means*, *nonparametric*})

Specifies the unsupervised machine learning *algorithm* being used to cluster data. The *columns* are specified using column names or indices.

### USING (*number_clusters*, *lambda*, etc.)

Used to specify hyperparameters or values for some machine learning algorithms.
