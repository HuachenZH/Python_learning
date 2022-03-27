import copy
import random
# Consider using the modules imported above.

class Hat:
    hat=dict()
    contents=list()
    def __init__(self,**args):
        # print(type(args)) # the type of args is dict
        # print(args) # returns {'yellow': 3, 'blue': 2, 'green': 6} (for example)
        hat=args
        for k,v in args.items():
            for i in range(v):
                self.contents.append(k)

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
