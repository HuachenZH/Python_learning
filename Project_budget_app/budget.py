class Category:
    ledger=[] #instance variable=attribut. It's a list  
    name='' # name of the category
    def __init__(self,name): # constructor
        self.name=name
        self.ledger=[]
    def get_balance(self):
        out=0
        for i in self.ledger:
            out+= float(i["amount"])     
        return out    
    def deposit(self,amount, *description):
        if not (isinstance(amount, int) or isinstance(amount, float)):
            print('Amount must be a number')
            return
        if description==(): # when there is no argument description, desciption is not None but (), an empty tuple... creepy
            description=''
        else:
            description=description[0] # i don't know why but description is a tuple here. because of the *. Without *, it's a string
        self.ledger.append({"amount":amount,"description":description}) 
    def withdraw(self,amount,*description):
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
    # self will loss money, cat will get money
        if self.withdraw(amount,'Transfer to '+cat.name):
            # withdraw, already happened in if
            # deposit
            cat.deposit(amount,'Transfer from '+self.name)
            return True
        else:
            return False	
def create_spend_chart(categories):
