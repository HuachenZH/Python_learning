# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 21:48:49 2022

@author: e^(j·2pi)
"""
#v0.3.1
# no need of if. Comparing to the previous version, greatest change is at line 51. I found a new way to compute the number of spaces in the first line. With this new way, i no longer need an if to distinguish 1 + 10 or 10 + 1
# also, i gave name to two new variables, operand1 and operand2 (they are string)

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



inp="3 - 9998"
listt=inp.split(' ')
operand1=listt[0] # type: str
operand2=listt[2] # type: string
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

    
print(out)

# what i've learnt from this version:
  # a good maths approach can help reduce lenghty if and for
  # in spyder, line 38, it can get the error of syntax of type in the comment
# for the next version:
  # print several formats in parallel.   solutions like cbind in R aren't feasible in this case (at least, with my level).    Roughly thinking, the solution will still be pur string. Whether i enlarge this script, whether i make this code into a function, then write another function to call this function.
  # and still need to implement this into end_project_v1.py, where there is the code for checking arguments.






