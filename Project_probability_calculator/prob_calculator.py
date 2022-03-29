import copy
import random
# Consider using the modules imported above.

class Hat:
    hat=dict()
    contents=list()
    def __init__(self,**args):
        # print(type(args)) # the type of args is dict
        # print(args) # returns {'yellow': 3, 'blue': 2, 'green': 6} (for example)
        self.hat=args
        self.contents=list()
        for k,v in args.items():
            for i in range(v):
                self.contents.append(k)
    def __str__(self): # i think it's useless to build this method. However i fixed a bug while building it
        out='{'
        for k,v in self.hat.items():
            out+="'"+k+"'"+': '+"'"+str(v)+"'"+', '
        out+='}'
        return out
    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
