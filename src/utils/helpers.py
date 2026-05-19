import os
import pickle
import pandas as pd
import yaml

def load_config(path='config.yaml'):
    with open(path,'r') as f:
        return yaml.safe_load(f)

def save_pickle(obj,path):
    os.makedirs(os.path.dirname(path),exist_ok=True)
    pickle.dump(obj,open(path,'wb'))
    print(f'Saved to {path}')

def load_pickle(path):
    return pickle.load(open(path,'rb'))

def load_data(path):
    return pd.read_csv(path,encoding='latin-1')

