# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 21:48:49 2022

@author: e^(j·2pi)
"""
#v0.2.1
# Now the code can work no matter it's addition or substraction


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



inp="9999 + 9998"
listt=inp.split(' ')
# check it's addition or substraction
operator=listt[1]
if operator=='+':
  res=int(listt[0])+int(listt[2])
if operator=='-':
    res=int(listt[0])-int(listt[2])
# compute the width of the arithmetic format
width=max(len(i) for i in listt)+2

out=''
if len(listt[0])>=len(listt[2]):    
    out+='  '+listt[0]+'\n' # first line
    
    out+=operator # second line, which starts from the operator    
    out=addSpaces(out,len(listt[0])-len(listt[2])+1) # second line, spaces between the operator and operand2
    out+=listt[2] # second line, add operand2
    
    out+='\n' # third line
    for i in range(width):
        out+='-'
    
    out+='\n' # forth line  
    out=addSpaces(out, width-len(str(res))) # forth line, spaces at the beginning
    out+=str(res) # forth line, the result
print(out)

# what i've learnt in this version:
  # to check the operator we need if, no doubt. But there are several ways to do so. Before start coding, think first, which is the easier and less lengthy

# for the next verison:
  # complete the other half of if, in case like 1 + 99, operand1 shorter than operand2

