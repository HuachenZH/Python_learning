# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 15:12:01 2022

@author: e^(j·2pi)
"""


def cbind(arg1,arg2):
    '''bind two string in column. Put two string next to each other then transform in to a new string.
    
    Parameters:
        argument1: the first string. After cbind, it will be on the left
        argument2: the second string. After cbind, it will be on the right
        
    Returns:
        A new string composed by the two input string'''
    
    
    # they are already vertical
    # we consider arg1 and arg2 have the same number of line
    
    # split them by \n
    arg1=arg1.split('\n')
    arg2=arg2.split('\n')
    nline=len(arg1) # number of lines
    
    # get each line of the new string (the output). Keep the lines in a list
    tmp=list()
    for i in range(nline): # i will be 0, 1, 2, 3
        tmp.append(arg1[i]+arg2[i]+'\n')
    
    # put all lines together into a new string
    out=''
    for i in tmp:
        out+=i
    out=out[0:len(out)-1] # enlever le dernier \n
    return out


def rbind(str1,str2):
    '''
    Bind two strings in row. = paste two strings together vertically.

    Parameters
    ----------
    str1 : TYPE str
        The first string, it will be on the top.
    str2 : TYPE str
        The second string, it will be on the bottum.

    Returns
    -------
    A new string composed by the two input string

    '''
    out=str1+'\n'+str2
    return out
    
def tstring(string): # entoure par une colonne d'espace en deux cote
    '''
    Transpose a string from horizontal to vertical

    Parameters
    ----------
    string : TYPE str
        The horizontal string.

    Returns
    -------
    The vertical string

    '''
    out=''
    for i in range(len(string)):
        out+=' '+string[i]+' \n'
    out=out[0:len(out)-1] # enlever le dernier \n
    return out
    
    
