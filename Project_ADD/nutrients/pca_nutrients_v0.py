import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from os import chdir


chdir(r'D:\2018-2023\S8\Tronc commun\ADD\ADD_projet\nutrient')



# import csv into pandas
df=pd.read_csv('nndb_flat.csv')


