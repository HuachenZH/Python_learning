# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 21:48:49 2022

@author: e^(j·2pi)
"""
#v1.4.3
# It's now a for loop inside the function cbind


def addSpaces(string,nbr):
    '''Add spaces to a string variable
    
    Parameters:
        argument1: the string to which you want to add spaces
        argument2: number of spaces you want to add
        
    Returns:
        new string with spaces added'''
    # argument1 must be a string
    if not isinstance(string,str):
        print('Error: argument1 must be a string')
        return
    # argument2 must be an integer
    if not isinstance(nbr,int):
        print('Error: argument2 must be an integer')
        return
    # all check, start work, add spaces
    for i in range(nbr):
        string+=' '
    return string




def singleFormatter(inp):
    '''Arrange arithmetic problems vertically. Transform only one expression.
    
    Parameters:
        argument1: the arithmetic problem expression. String. There must be one space betweeen each operand and operator
        
    Returns:
        new string with the arithmetic expression arranged vertically'''

    listt=inp.split(' ')
    try:    
        operand1=listt[0] # type: str
        operand2=listt[2] # type: str
    except:
        print('Error: there must be one space betweeen each operand and operator. For example "1 + 12"')
        return
    # check it's addition or substraction
    operator=listt[1]
    if operator=='+':
        res=int(operand1)+int(operand2)
    if operator=='-':
        res=int(operand1)-int(operand2)
    # compute the width of the arithmetic format
    width=max(len(i) for i in listt)+2
    
    out=''
    
        
    out=addSpaces(out,width-len(operand1))+operand1 # first line
    
    out+='\n' # second line
    out+=operator # second line, which starts from the operator    
    out=addSpaces(out,width-len(operand2)-1) # second line, spaces between the operator and operand2
    out+=operand2 # second line, add operand2
    
    out+='\n' # third line
    for i in range(width):
        out+='-'
    
    out+='\n' # forth line  
    out=addSpaces(out, width-len(str(res))) # forth line, spaces at the beginning
    out+=str(res) # forth line, the result
    
        
    return out

def cbind(arg1,arg2):
    '''bind two string in column. Put two string next to each other then transform in to a new string.
    
    Parameters:
        argument1: the first string. After cbind, it will be on the left
        argument2: the second string. After cbind, it will be on the right
        
    Returns:
        A new string composed by the two input string'''
    
    
    # arrange them in vertical
    arg1=singleFormatter(arg1)
    arg2=singleFormatter(arg2)
    # we consider arg1 and arg2 have the same number of line
    
    # split them by \n
    arg1=arg1.split('\n')
    arg2=arg2.split('\n')
    nline=len(arg1) # number of lines
    
    # get each line of the new string (the output). Keep the lines in a list
    tmp=list()
    for i in range(nline): # i will be 0, 1, 2, 3
        tmp.append(arg1[i]+'    '+arg2[i]+'\n')
    
    # put all lines together into a new string
    out=''
    for i in tmp:
        out+=i
    return out

arg1="5448 - 998"
arg2="46 + 167"
print(cbind(arg1,arg2))

# what i've learnt from this version:
	# i nearly forgot to use list when i construct the for loop of cbind. Not cool with a fully string way
# next version: 
	# time to put the two parts together


