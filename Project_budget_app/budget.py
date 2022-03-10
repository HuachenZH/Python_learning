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
		
		
def create_spend_chart(categories):
