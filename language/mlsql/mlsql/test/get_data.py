import os
import requests

path  = 'data'

NAMES = {
    ''

}
DATASETS = (
    'https://raw.githubusercontent.com/mxhao2/MLSQL_DataSets/master/auto.csv',
    'https://raw.githubusercontent.com/mxhao2/MLSQL_DataSets/master/boston.csv',
    'https://raw.githubusercontent.com/mxhao2/MLSQL_DataSets/master/census.csv',
    'https://raw.githubusercontent.com/mxhao2/MLSQL_DataSets/master/chronic.csv',
    'https://raw.githubusercontent.com/mxhao2/MLSQL_DataSets/master/computer.csv',
    'https://raw.githubusercontent.com/mxhao2/MLSQL_DataSets/master/iris.csv',
    'https://raw.githubusercontent.com/mxhao2/MLSQL_DataSets/master/seeds.csv',
    'https://raw.githubusercontent.com/mxhao2/MLSQL_DataSets/master/spam.csv',
    'https://raw.githubusercontent.com/mxhao2/MLSQL_DataSets/master/train.csv',
    'https://raw.githubusercontent.com/mxhao2/MLSQL_DataSets/master/wine.csv',



)

def download_data(path , urls = DATASETS):
    if not os.path.exists(path):
        os.mkdir(path)

    for url in urls:
        response = requests.get(url)
        name = os.path.basename(url)
        with open(os.path.join(path, name), 'wb') as f:
            f.write(response.content)


download_data('data')
