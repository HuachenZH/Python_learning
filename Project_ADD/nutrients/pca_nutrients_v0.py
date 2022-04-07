
import numpy as np
import matplotlib.pyplot as plt
from os import chdir


chdir(r'D:\2018-2023\S8\Tronc commun\ADD\ADD_projet\nutrient')



#%% import csv into pandas
import pandas as pd

df=pd.read_csv('nndb_flat.csv')


#%% check highly correlated features

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

print("List of highly correlated features:")
print(check_corr(df))
print('\nIt s up to you to check which features should be removed :)\n\n') # in order to save some times, i'm not going to write a function which sorts the highly correlated features automatically. Although this sounds interesting



#%% remove highly correlated features and non-numeric features

# we will remove all those who contains _USRDA
df.drop(df.columns[df.columns.str.contains('_USRDA')].values, inplace=True, axis=1)
#                   ^-------^ Index(['ID', 'FoodGroup', 'ShortDescrip', 'Descrip', 'CommonName', 'MfgName',.....dtype='object')   type:<class 'pandas.core.indexes.base.Index'>
#                   ^-----------^   <pandas.core.strings.accessor.StringMethods object at 0x00000283F1A8DCA0>     type: <class 'pandas.core.strings.accessor.StringMethods'>
#                   ^------------------------------^ [False False False False False False False False False False ...... True]    type: list
#       ^------------------------------------------^ Index(['VitA_USRDA', 'VitB6_USRDA', 'VitB12_USRDA', 'VitC_USRDA',.... dtype='object')    type:<class 'pandas.core.indexes.base.Index'>
#       ^--------------------------------------------------^  ['VitA_USRDA' 'VitB6_USRDA' .... 'Zinc_USRDA']    type: list

# inplace=True : default False. If false, return a copy of dataframe. If true, replace de original dataframe
# axis=1 : default 0. If 0, drop labels from index. If 1, drop labels from columns

# set the column ID as index. Cf tictac.py
df.set_index('ID', inplace=True)

# find non numeric features
df_desc=df.select_dtypes(include='object') # if use 'str': TypeError: string dtypes are not allowed, use 'object' instead
df.drop(df.select_dtypes(include='object'),axis=1,inplace=True) # now df is 8618*23

# ax = df.hist(bins=50, xlabelsize=-1, ylabelsize=-1, figsize=(11,11))
ax = df.hist(bins=50, figsize=(11,11))

#%% standardize to mean=0, variance=1
from sklearn.preprocessing import StandardScaler

df_st=StandardScaler().fit_transform(df) # type of df_st: array of float64 8618*23
print("mean of df_st: ",np.round(df_st.mean()))
print("stdev of df_st: ", round(df_st.std()))
print('\n\n')


#%% implement PCA
from sklearn.decomposition import PCA

pca=PCA().fit_transform(df_st) # type : array of float64 8618*23
# in machine learning, people normally use fit_transform() for training data, transform() for test data (also called validate data).
# cf  https://towardsdatascience.com/what-and-why-behind-fit-transform-vs-transform-in-scikit-learn-78f915cf96fe












