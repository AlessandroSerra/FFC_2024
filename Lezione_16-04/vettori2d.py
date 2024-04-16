import numpy as np

class vec2d:

    # ciao questi sono gli attributi fonamentali
    def __init__(self, x=0, y=0):

        self.x = x
        self.y = y


    def __str__(self):

        stringa = f"({self.x}, {self.y})"
        return stringa


    def __add__(self, other):

        somma_x = self.x + other.x
        somma_y = self.y + other.y
        somma = vec2d(somma_x, somma_y)
        return somma
    

    def __neg__(self):

        return vec2d(-self.x, -self.y)
    

    def __sub__(self, other):
        return self + (-other)
    

    def __mul__(self, other):

        if isinstance(other, vec2d):
            return self.x*other.x + self.y*other.y

        return vec2d(self.x*other, self.y*other)


    def __rmul__(self, other):
        return self*other


    def __truediv__(self, other): 
        return vec2d(self.x/other, self.y/other)


    def mod(self):
        return np.sqrt(self.x**2 + self.y**2)
    

    def unit(self):
        return self / self.mod()




if __name__ == '__main__':

    a = vec2d(1, 2)
    b = vec2d(3, 4)
    c = a+b

    print(b.unit())
    print(a*2 + c)

