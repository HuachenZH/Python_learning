import copy
import random
# Consider using the modules imported above.

class Hat:
    hat=dict()
    contents=list()
    def __init__(self,**args):
        # print(type(args)) # the type of args is dict
        # print(args) # returns {'yellow': 3, 'blue': 2, 'green': 6} (for example)
        self.hat=args # so hat is a dict like {'yellow': 3, 'blue': 2, 'green': 6}
        self.contents=list()
        for k,v in args.items():
            for i in range(v):
                self.contents.append(k)
    def __str__(self): 
        out='{'
        for k,v in self.hat.items():
            out+="'"+k+"'"+': '+"'"+str(v)+"'"+', '
        out+='}'
        return out
    def draw(self, num):
        '''
        Draw balls from the hat. (exhaustif)

        Parameters
        ----------
        num : TYPE int
            The number of balls to draw. If the number esceeds the available quantity, then draw all the balls.

        Returns
        -------
        Return the balls drawn as a list of str

        '''
        # check the input type
        if not isinstance(num,int):
            print('The number of balls to draw must be int')
            return
        out=list()
        if num>=len(self.contents): # if the number of balls to draw exceeds the available quantity
            out=self.contents # then draw all the balls
            self.contents=list() # so that there is nothing left in contents, contents is an empty list now
        else: # if there are enough balls to draw
            # then we need to draw balls... randomly
            for i in range(num):
                out.append(random.choice(self.contents)) # draw a ball randomly and keep it in the output list
                self.contents.remove(out[i]) # remove the drawn ball from self.contents
        return out
    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
