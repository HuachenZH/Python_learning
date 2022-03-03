# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 21:48:49 2022

@author: e^(j·2pi)
"""
#v1.4.2
# apply the solution of split by \n. Turn some of code to function


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
    
    # split them by \n
    arg1=arg1.split('\n')
    arg2=arg2.split('\n')
    
    # paste them, cbind
    line1=arg1[0]+'    '+arg2[0]+'\n'
    line2=arg1[1]+'    '+arg2[1]+'\n'
    line3=arg1[2]+'    '+arg2[2]+'\n'
    line4=arg1[3]+'    '+arg2[3]+'\n'
    out=line1+line2+line3+line4
    return out

arg1="5448 - 9998"
arg2="46 + 167"
print(cbind(arg1,arg2))

# what i've learnt in this version:
	# max(len(i) for i in listt) works without []
	# however when print([(i) for i in c]) , there will be error without []
# for the next version:
	# optimize the function cbind, use for loop


