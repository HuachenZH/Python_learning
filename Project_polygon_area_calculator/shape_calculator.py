import math


class Rectangle:
    width=0
    height=0
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def __str__(self):
        out='Rectangle(width='+str(self.width)+', height='+str(self.height)+')'
        return out
    def set_width(self,width):
        self.width=width
    def set_height(self,height):
        self.height=height
    def get_area(self):
        return self.width*self.height
    def get_perimeter(self):
        return 2*(self.width+self.height)
    def get_diagonal(self):
        return (self.width**2+self.height**2)**.5
    def get_picture(self):
        out=''
        if self.width>50 or self.height>50:
            out='Too big for picture.'
        else:
            for i in range(self.height):
                for j in range(self.width):
                    out+='*'
                out+='\n'
        return out
    def get_amount_inside(self,shape):
        out=math.floor(self.get_area()/shape.get_area())
        return out


class Square(Rectangle):
    def __init__(self,side):
        self.width=side
        self.height=side
    def set_side(self,side):
        self.width=side
        self.height=side
    def __str__(self):
        out='Square(side='+str(self.width)+')'
        return out
    def set_width(self,side):
        self.width=side
        self.height=side
    def set_height(self, side):
        self.width=side
        self.height=side
