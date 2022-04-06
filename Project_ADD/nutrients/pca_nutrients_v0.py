import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from os import chdir


chdir(r'D:\2018-2023\S8\Tronc commun\ADD\ADD_projet\nutrient')



# import csv into pandas
df=pd.read_csv('nndb_flat.csv')


def check_corr(df):
    '''
    Check highly correlated features of a dataframe
   
    Parameters
    ----------
    df : TYPE pandas.core.frame.DataFrame
        The dataframe to be checked

    Returns
    -------
    listnet : TYPE list
        The output list of tuples. Each tuple is a pair of two highly correlated features
    '''
    # check for high correlated features
    # we will browse every element of the correlation matrix: df.corr().  It's a matrix of 39*39 as there are 39 columns whose values are numeric. We will find those highly correlated columns.
    matcorr=df.corr() # if i don't save df.corr() into a variable, it will take 30s more each time i run the script
    #two steps, 1 get the index, 2 get the corresponding metadata
    # step 1: find the index
    listindex=list()
    for i in range(len(matcorr)):
        for j in range(len(matcorr)):
            if i!=j and matcorr.iloc[i,j]>0.9:
            #    |                       ^ coef correlation greater than 0.9, then it's considered highly correlated
            #    ^  if i==j, then it's the diagonal, the value will certainly be 1
                listindex.append((i,j)) # append the pair of index as tuple
    # step 2: find the metadata (colnames)
    # to get the colnames: matcorr.columns
    listnut=list() # list nutrients
    for tuples in listindex:
        listnut.append((matcorr.columns[tuples[0]],matcorr.columns[tuples[1]]))
    return listnut

