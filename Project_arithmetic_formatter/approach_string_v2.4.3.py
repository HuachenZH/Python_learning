# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 21:48:49 2022

@author: e^(j·2pi)
"""
# v2.4.3 two parts now have combined together.
# modification in function cbind: before, the input of cbind is two string like "3 + 1", now the input of cbind is already the vertical format, so no need to call singleFormatter().
# also in cbind, in the previous version, the output of cbind has a \n at the end, this causes problem. So i delete the \n at the end by extracting the remaining parts
# in singleFormatter, little problem with the if of res, with previous code, traceback will be like: UnboundLocalError: local variable referenced before assignment. Because i haven't defined the value of res when the operator is neither + nor -


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
    elif operator=='-':
        res=int(operand1)-int(operand2)
    else:
        res=0
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
    
    
    # they are already vertical
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
    out=out[0:len(out)-1]
    return out



def arithmetic_arranger(x):
    # x is a list like this: ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
    # there must be spaces between operator and operands (not requested, just easier for me)
    
    # check the number of problems: less than 5
    if len(x)>5:
        print('Error: Too many problems.')
        print('Current number of problems: ',len(x),'\n')
    
    # check the operators: only + and -
    for i in x: # ? can we make it a try except?
        i=i.split(' ')
        if i[1] != '+' and i[1] != '-':
            print('Error: Operator must be ''+'' or ''-''')
            return # if put break here, Python will stop this for but continue to the next for loop
        # else:
        #     print('Operator correct')
            
    # check the operands: each number should only contain digits
    for i in x:
        i=i.split(' ')
        try:
            int(i[0])
            int(i[2])
        except:
            print('Error: Numbers must only contain digits.')
    
    # check the operands: maximum four digits
        for ii in i:
            if len(ii)>4:
                print('Error: Numbers cannot be more than four digits.')
                return


            
    # check ends, conversion starts.
    # get all single vertical formats. Save them in a list
    tmp=list()
    for i in x:
        tmp.append(singleFormatter(i))   
    # bind them together
    out=tmp[0]
    for i in range(len(tmp)-1): # i=0 1 2
        out=cbind(out,tmp[i+1])
    return out

#-------------------main---------------------------

# x=["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
# x1=["32 + 698", "3801 - 2", "45 + 43", "123 + 49","1 + 1","2 + 3"]
# x2=["32 + 698", "3801 * 2", "45 + 43", "123 + 49"]
# x3=["32 + 698", "3801 + 2a", "45 + 43", "123 + 49"]
# x23=["32 + 698", "3801 * 2a", "45 + 43", "123 + 49"]
x4=["32 + 698", "380 + 2", "45 + 43", "123 - 49"]
check=arithmetic_arranger(x4)
print(check)


# what i've learnt from this version:
	# i wonder if it is a good idea to define so many functions, i spent on checking tracebacks, finding errors

# for the next version:
	# optimized the code and the logic






