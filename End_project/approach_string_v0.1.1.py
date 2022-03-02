# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 21:48:49 2022

@author: e^(j·2pi)
"""
#v0.1.1
# syntax upgrade, use less for loops, replaced by a self-defined function


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



inp="32 + 33"
listt=inp.split(' ')
res=int(listt[0])+int(listt[2])
larger=max(len(i) for i in listt)+2

out=''
if len(listt[0])>=len(listt[2]):
    out+='  '+listt[0]+'\n+'
    # for i in range(len(listt[0])-len(listt[2])+1):
    #     out+=' '
    out=addSpaces(out,len(listt[0])-len(listt[2])+1)
    out+=listt[2]
    out+='\n'
    for i in range(larger):
        out+='-'
    out+='\n'
    # for i in range(larger-len(str(res))):
    #     out+=' '
    out=addSpaces(out, larger-len(str(res)))
    out+=str(res)
print(out)

# what i've learnt from this version:
  # check the type in Python: isinstance(variable,type)
  # Python javadoc like: docstring

# for the next version:
  # this version is half-completed, in the input expression "nbr1 + nbr2", the code works only if nbr1 is bigger than nbr2
  # and it works only when the operator is +
