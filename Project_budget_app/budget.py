# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 19:29:10 2022

@author: e^(j·2pi)
"""
import math
from arith import cbind, rbind, tstring
class Category:
    ledger=[] #instance variable=attribut. It's a list  
    name='' # name of the category
    def __init__(self,name): # constructor
        '''
        The constructor. name is the name of the category (not the variable)    
        '''
        self.name=name
        self.ledger=[]
    def get_balance(self):
        '''
        Get the sum of all deposit and withdraw in the ledger.
        =the current balance of the budget cataegory
        
        Returns
        -------
        out : TYPE float
        '''
        out=0
        for i in self.ledger:
            out+= float(i["amount"])       
        return out
    def check_funds(self,amount):
        '''
        Check whether the amount (argument) is greater or smaller than the balance

        Parameters
        ----------
        amount : TYPE numeric
            The amount that user wants to compare with ledger

        Returns
        -------
        bool

        '''
        if amount>self.get_balance():
            return False
        else:
            return True
    
    def deposit(self,amount, *description):
        '''
        Deposit a certain amount of budget in the category. 
        The amount will be saved in the ledger (positive value).

        Parameters
        ----------
        amount : TYPE numeric
            The amount that user wants to deposit
        *description : TYPE str
            The description of the amount. Optional argument

        Returns
        -------
        None.

        '''
        if not (isinstance(amount, int) or isinstance(amount, float)):
            print('Amount must be a number')
            return
        if description==(): # when there is no argument description, desciption is not None but (), an empty tuple... creepy
            description=''
        else:
            description=description[0] # i don't know why but description is a tuple here. because of the *. Without *, it's a string
        self.ledger.append({"amount":amount,"description":description})        
    
    def withdraw(self,amount,*description):
        '''
        Withdraw a certain amount of budget in the category.
        There must be enough money. If not the withdraw wont be happened
        The amount will be saved in the ledger (negative value).

        Parameters
        ----------
        amount : TYPE numeric
            The amount that user wants to withdraw
        *description : TYPE str
            The description of the amount. Optional argument

        Returns
        -------
        bool

        '''
        if not self.check_funds(amount): # not enough funds, withdraw wont be taken place
            return False
        else: # enough fund. Withdraw will be taken place
            if description==(): # classic tuple stuff of *description
                description=''
            else:
                description=description[0]
            #the amount should be stored in the ledger as a negative number
            amount=-1*amount
            self.ledger.append({"amount":amount,"description":description})
            return True
    def transfer(self,amount,cat): # cat is the destinated category
        '''
        Withdraw a certain amount of budget from the category to another category.
        There must be enough money. If not the transfer wont be happened
        Ledgers of both categories will be changed (as they spend and receive money)

        Parameters
        ----------
        amount : TYPE numeric
            The amount that user wants to transfer
        cat : TYPE object
            The category that will receive money

        Returns
        ----------
        bool
            True if the transfer took place
            False if the transfer hasent taken place
        '''
        # self will loss money, cat will get money
        if not self.check_funds(amount): # if not enough money, nothing happens, return false
            return False
        else: # if enough money, the transfer will be taken place
            # those who lose money, withdraw
            self.withdraw(amount,'Transfer to '+cat.name)
            # those who receive money, deposit
            cat.deposit(amount,'Transfer from '+self.name)
            return True
    def __str__(self):
        out=''
        n1=math.floor((30-len(self.name))/2) # number of * at the beginning
        n2=30-len(self.name)-n1 # number of * at the end
        for i in range(n1):
            out+='*'
        out+=self.name
        for i in range(n2):
            out+='*'
        out+='\n' # first line finish, start the second line
        for i in self.ledger: # i is a dictionary
        # i is like {"amount":500,"description:":"depo"}
            out+=i["description"][:23] # description, # extract string
            num=format(i["amount"],'.2F') # the number at the right
            for j in range(30-len(i["description"][:23])-len(num)): # whitespaces
                out+=' '
            out+=num
            out+='\n'
        # the final line displaying the total
        out+='Total: '
        # calculate the total
        out+=format(self.get_balance(),'.2f')
        return out
    
def create_spend_chart(listcategories):
    '''
    Chart showing the percentage spent in each category

    Parameters
    ----------
    listcategories : TYPE list 
        A list of of categories.

    Returns
    -------
    A long string...

    '''
    # 1. get the percentage
    # 1.1 create a dictionary which holds values
    dictper={} #a dict of percentage
    for i in listcategories: # i will be a category like food, drink...
        dictper[i.name]=0
        for j in i.ledger: # j is a dictionary like {"amount":500,"description:":"depo"}
            if j["amount"]<0: # if it's withdraw
                dictper[i.name]+=j["amount"] # add to the dictionary
    # 1.2 calculate the total sum
    # dictper is like: {'Business': -10.99, 'Food': -105.55, 'Entertainment': -33.4}
    somme=sum(i for i in dictper.values()) # the total sum of spent
    # 1.3 calculate percentage
    for i in dictper:
        dictper[i]=math.floor(dictper[i]/somme*100/10)*10
        #                 |                         |---|
        #                 |                           |
        #            round down                 to the nearest 10
    # 2. print the chart
    out=''
    # i cut the chart into three parts, title, top and bot
    # title is 'Percentage spent by category'
    # top is the y axis and lots of 'o', and the    -----------
    # bot is the x axis (name of category)
    # --------- 
    # 2.1 title
    title='Percentage spent by category'
    # 2.2 top    
    # 2.2.1 y axis
    col1='100\n 90\n 80\n 70\n 60\n 50\n 40\n 30\n 20\n 10\n  0'
    col2='|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|'
    top=cbind(col1,col2)
    # 2.2.2 lots of 'o'
    tmp=''
    for v in dictper.values():
        tmp=''
        for i in range(int(10-v/10)): # print whitespaces
            tmp+='   \n' # 3 whitespaces
        for i in range(int(v/10+1)): # print o
            tmp+=' o \n'
        tmp=tmp[0:len(tmp)-1] # enlever le dernier \n
        top=cbind(top,tmp)
    top=cbind(top,' \n \n \n \n \n \n \n \n \n \n ') # the rightest column of whitespaces 
    # 2.2.3 the ---------- line
    line='    ' # always starts by four whitespaces
    for i in range(len(listcategories)):
        line+='---'
    line+='-'
    # paste line and chart
    top=rbind(top,line)
    # 2.3 bot
    # 2.3.1 the leftmost rectangle of whitespace
    height=max(len(k) for k in dictper.keys()) # the height of the bot
    bot=''
    for i in range(height):
        bot+='    \n' # always four whitespaces
    bot=bot[0:len(bot)-1] # enlever le dernier \n
    # 2.3.2 the x axis, name in vertical
    for k in dictper.keys():
        for j in range(height-len(k)):
            k+=' '
        bot=cbind(bot,tstring(k))
    # 2.3.3 the rightmost column of whitespace
    tmp=''
    for i in range(height):
        tmp+=' \n'
    tmp=tmp[0:len(tmp)-1] # enlever le dernier \n
    bot=cbind(bot,tmp)
    # 2.4 paste together
    out=rbind(title,top)
    out=rbind(out,bot)
    return out


