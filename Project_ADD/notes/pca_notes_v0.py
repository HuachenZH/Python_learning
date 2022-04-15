# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 16:38:35 2022

@author: eziod
"""
# https://data.world/exercises/pca-exercise-1-solutions/workspace/file?filename=nutrition_pca_solution.ipynb
import numpy as np
from os import chdir

chdir(r'D:\2018-2023\S8\Tronc commun\ADD\ADD_projet\nutrient')


#%% import csv into pandas
import pandas as pd

dfNotes=pd.read_csv('Notes.csv')

#%% set name as index (put a column into metadata)
#= seting a new index from an existing column
dfNotes=dfNotes.set_index('NAME')

#%% standardize to mean=0, variance=1
from sklearn.preprocessing import StandardScaler

dfNotes_st=StandardScaler().fit_transform(dfNotes) # type of dfNotes_st: array of float64 38*5
print("mean of df_st: ",np.round(dfNotes_st.mean()))
print("stdev of df_st: ", round(dfNotes_st.std()))
print('\n\n')


#%% implement PCA
from sklearn.decomposition import PCA
fit=PCA()
# if we use the original dataframe, without standardizing:
pcaNotes2=fit.fit_transform(dfNotes) # pca: type : array of float64 38*5   # with non-standardized dataset
# and if we use the dataframe standardized:
pcaNotes=fit.fit_transform(dfNotes_st) # pca: type : array of float64 38*5   # with standardized dataset
# later in this script we will use pcaNotes

# check the eigenvalues to find most important components:
import matplotlib.pyplot as plt
plt.figure(1) # line plot of value of eigenvector
plt.plot(fit.explained_variance_ratio_) # something wierd: if i dont declare fit=PCA() before but to use PCA() instead, then this line will have error: AttributeError: 'PCA' object has no attribute 'explained_variance_ratio_'


print(fit.explained_variance_ratio_) # percentage of importance of each eigenvector (=of each component)
# make an accumulated one
accumulated=fit.explained_variance_ratio_
for i in range(1,len(fit.explained_variance_ratio_)): # i will be 1, 2, 3, 4. I mean, i, not me
# range(start, stop[, step])
    accumulated[i]=accumulated[i-1]+accumulated[i]
print(accumulated)

# eboulis, barplot (value of eigenvector) + lineplot (accumulated)
# https://matplotlib.org/3.5.0/gallery/subplots_axes_and_figures/two_scales.html
plt.figure(2)

fig, ax1=plt.subplots() # subplots but not subplot. Difference between the two: https://stackoverflow.com/questions/52214776/python-matplotlib-differences-between-subplot-and-subplots
# in one world, by using subplots, we create a figure and subplot at the same time
color='tab:red'
ax1.set_xlabel('Principal components')
ax1.set_ylabel('barplot, eigenvector values',color=color)
ax1.bar(np.arange(len(fit.explained_variance_ratio_)),fit.explained_variance_,color=color)
ax1.tick_params(axis='y', labelcolor=color) # change the color of y axis values

ax2=ax1.twinx() # instantiate a second axes that shares the same x-axis
color='tab:blue'
ax2.set_ylabel('lineplot, accumulated values',color=color)
ax2.plot(accumulated,color=color,linewidth=5)
ax2.tick_params(axis='y', labelcolor=color) #♣ change the color of y axis values
fig.tight_layout()  # otherwise the right y-label is slightly clipped # in fact nothing changes...
plt.show() # the right y axis scale can still be optimized 

#%% in this case (Notes), we will keep all the eigenvectors
pcaNotes=pd.DataFrame(pcaNotes[:,:4], index=dfNotes.index,columns=dfNotes.columns[:4]) # .index is like rownames
# the type of pcaNotes is now DataFrame, before it was array of float64
    # pd.DataFrame: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html
        # parameter index: set rownames
        # parameter columns: set colnames
# something wierd about this line: with F5 it will run succesfully. With ctrl enter, there will be traceback: InvalidIndexError: (slice(None, None, None), slice(None, 4, None))

# source code of data.world, In[39]
# pca = pca.join(df_desc)  
    # pca is type DataFrame
    # df_desc: In[6]: df_desc = df.iloc[:, :6]
    # about .join(): https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.join.html
        # join columns of another DataFrame. The parameter index is not mentioned in the official documentation
# pca.drop(['CommonName','MfgName','ScientificName'], axis=1, inplace=True)
    # about drop: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop.html
        # drop specified labels from rows or columns  (labels = index or column labels.. or colnames stv)
        # remove rows or columns by specifying label names
# pca.rename(columns={0:'c1',1:'c2',2:'c3',3:'c4',4:'c5'}, inplace=True)


# np.round(pcaNotes.corr(),5)
pcaNotes.corr()






