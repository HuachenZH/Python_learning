
# =============================================================================
# an example of object's life cycle
# =============================================================================
class partyAnimal:
    x=0
    def __init__(self): # self is a reserved keyword, means the object itself
                        # __init__(self): as the underscore shows, it's Python's predifined function, the constructor
                        # we must put the "self" in the (), if not, traceback will be: error with an=partyAnimal(), TypeError: __init__() takes 0 positional arguments but 1 was given
        print("I am constructed")
    def party(self):
        self.x=self.x+1
        print("So far",self.x)
    def __del__(self):
        print('I am destructed at ',self.x)
print('\n1')
an=partyAnimal()
print('\n2')
an.party()
print('\n3')
partyAnimal.party(an) # this expression is the same as an.party()
print('\n4')
an.party()
an.party()
print('\n5')
an=42 # when an is affected to a integer, it is no longer an object, so it's destructed

# the output is:
# 1
# I am constructed

# 2
# So far 1

# 3
# So far 2

# 4
# So far 3
# So far 4

# 5
# I am destructed at  4



# =============================================================================
# instances with different instance variables
# =============================================================================
class AnimalFarm:
    x=0
    name=''
    def __init__(self,name):
        self.name=name
    def party(self,add):
        self.x=self.x+add
        print('There is/are ',self.x,' ',self.name,'(s) in the farm')
pigg=AnimalFarm('pig')
pigg.party(5)
pigg.party(-3)

dogg=AnimalFarm('dog')
AnimalFarm.party(dogg,10)



# =============================================================================
# Inheritance
# =============================================================================
# just an example
class Parents:
    blablabla...
class Children(Parents): # put Parents in the () shows inheritance
    blablabla...
# Children is an inheritance of Parents
# Children is an extend of Parents
# Children have all what Parents have, and something more









# there is no exercice about objects... so wait for a project to practise

