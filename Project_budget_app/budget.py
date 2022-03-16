class Category:
	ledger=[] #instance variable=attribut. It's a list  
	name='' # name of the category
	def __init__(self,name): # constructor
		self.name=name
		self.ledger=[]
	def deposit(self,amount, *description):
		if not (isinstance(amount, int) or isinstance(amount, float)):
			print('Amount must be a number')
			return
		if description==None:
			description=''
		self.ledger.append({"amount":amount,"description":description})
    def get_balance(self):
        out=0
        for i in self.ledger:
            out+= float(i["amount"])     
        return out
    def withdraw(self,amount,*description):
        if self.get_balance()-amount<0:
            return False
        else:
            #the amount should be stored in the ledger as a negative number
            amount=-1*amount
            self.deposit(amount,description)
            return True
		
def create_spend_chart(categories):
