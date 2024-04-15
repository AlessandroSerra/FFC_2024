import numpy as np


class vec2d:

    # attributi della classe
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


    #------------------------------------------------------------
    #                        OPERATORI
    #------------------------------------------------------------

    # stringa
    def __str__(self):
        return f'({self.x}, {self.y})'
    
    # inverso
    def __neg__(self):
        return vec2d(- self.x, - self.y)

    # somma
    def __add__(self, other):
        return vec2d(self.x+other.x, self.y+other.y)

    # sottrazione
    def __sub__(self, other):
        return self + (-other)

    # prodotto con primo elemento vettore
    def __mul__(self, other):

        # scalare tra vettori
        if isinstance(other, vec2d):
            return self.x*other.x + self.y*other.y

        # tra scalare e vettore
        return vec2d(self.x*other, self.y*other)

    # prodotto con primo elemento scalare
    def __rmul__(self, other):
        return self*other
    
    # divisione per scalare   
    def __truediv__(self, other):
        return vec2d(self.x/other, self.y/other)
    
    # resto della divisione
    def __mod__(self, other):
        return vec2d(self.x%other, self.y%other)

    # potenza intesa come modulo elevato numero
    def __pow__(self, other):
        return self.mod()**other

    #------------------------------------------------------------
    #                       METODI
    #------------------------------------------------------------

    # metodo per ottenere il modulo
    def mod(self):
        return np.sqrt(self.x**2 + self.y**2)

    # metodo per ottenere un versore
    def unit(self):
        return self / self.mod()

    # metodo per ottenere l'angolo tra vettori
    def GetAngle(self, other):
        return np.arccos(self * other / (self.mod() * other.mod()))



#------------------------------------------------------------
#                       TESTING
#------------------------------------------------------------


# test delle funzioni, viene eseguito solo se si runna il programma direttamente
# e non se viene importato come libreria in un altro codice
if __name__ == '__main__':

    a = vec2d(2, 1)

    print(a)