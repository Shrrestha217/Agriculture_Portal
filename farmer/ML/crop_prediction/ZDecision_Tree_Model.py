import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

data = pd.read_csv('C:\\Users\\SHRRESTHA\\OneDrive\\Desktop\\Major Project\\Agriculture Portal\\farmer\\ML\\crop_prediction\\preprocessed2.csv')
data.head()

data['Season'] = data['Season'].str.rstrip()

for i in data['Season']:
    print(len(i))

list(data)

del data['Unnamed: 0']

trainig_data = list(np.array(data))

testing_data = trainig_data[100:120]

header = ['State_name', 'District_name', 'Season', 'Crop']

def unique_val(Data, col):
    return set([row[col] for row in Data])

def class_counts(Data):
    counts = {}
    for row in Data:
        label = row[-1]
        if label not in counts:
            counts[label] = 0
        counts[label] += 1
    return counts

class_counts(trainig_data)

class Question:
    def __init__(self, column, value):