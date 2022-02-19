
# =============================================================================
# an example of object's life cycle
# =============================================================================
class partyAnimal:
    x=0
    def __init__(self): # self is a reserved keyword, means the object itself
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
partyAnimal.party(an)
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


