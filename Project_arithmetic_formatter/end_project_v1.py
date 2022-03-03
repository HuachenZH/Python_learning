# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]




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
        else:
            print('Operator correct')
            

            
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

#-------------------main---------------------------

x=["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
x1=["32 + 698", "3801 - 2", "45 + 43", "123 + 49","1 + 1","2 + 3"]
x2=["32 + 698", "3801 * 2", "45 + 43", "123 + 49"]
x3=["32 + 698", "3801 + 2a", "45 + 43", "123 + 49"]
x23=["32 + 698", "3801 * 2a", "45 + 43", "123 + 49"]
x4=["32 + 698", "380121 + 2", "45 + 43", "123 + 49"]
arithmetic_arranger(x4)

# storming... possible to combine all the test into one for loop?

