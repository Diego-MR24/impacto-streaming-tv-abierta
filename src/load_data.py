import pandas as pd  

def load_data(url):
    data = pd.read_csv(url)
    return data

