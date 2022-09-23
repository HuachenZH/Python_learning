# ******************* default value of a fct *************************
def iden(prenom, nom, pays="France"):
  pass
# if the third argument pays is not given, its value will automatically be "France"

# ******************** global variable in a function **************************
x=2
def rien():
  global x
  x=5
  porint(x)
print(x) # gives 2
rien() # gives 5
print(x) # gives 5
