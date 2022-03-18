# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 19:29:10 2022

@author: e^(j·2pi)
"""


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
        if self.get_balance()-amount<0:
            return False
        else:
            if description==(): 
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
        if self.withdraw(amount,'Transfer to '+cat.name):
            # withdraw, already happened in if
            # deposit
            cat.deposit(amount,'Transfer from '+self.name)
            return True
        else:
            return False
    



def create_spend_chart(categories):




    
    
    
    
    
    
