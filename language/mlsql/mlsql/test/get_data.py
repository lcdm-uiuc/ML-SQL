import os
import requests

path = 'data'
base_url = 'https://raw.githubusercontent.com/mxhao2/MLSQL_DataSets/master/'

DATASETS = (
    base_url + 'auto.csv',
    base_url + 'boston.csv',
    base_url + 'census.csv',
    base_url + 'chronic.csv',
    base_url + 'computer.csv',
    base_url + 'iris.csv',
    base_url + 'seeds.csv',
    base_url + 'spam.csv',
    base_url + 'train.csv',
    base_url + 'wine.csv',
)

def download_data(path , urls=DATASETS):
    if not os.path.exists(path):
        os.mkdir(path)

    for url in urls:
        response = requests.get(url)
        name = os.path.basename(url)
        with open(os.path.join(path, name), 'wb') as f:
            f.write(response.content)


download_data('path')
