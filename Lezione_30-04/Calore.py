import numpy as np
import matplotlib.pyplot as plt


def BoundaryConditions():
    pass



def DoFTCS(T_old):

    T_new = T_old.copy()

    # loop nello spazio per aggiornare i valori di temperatura con l'FTCS
    for i in range(1, N_x-1):
        T_new[i] = T_old[i] + dt*k/h**2(T_old[i-1] + T_old[i+1] - 2*T_old[i])

    

    return T_new



def Solve():
    pass



# PARAMETRI DI SIMULAZIONE

L = 1                           # m
k = 1                           # m**2/s
h = 0.01                        # m
dt = 0.2 * h**2 / (2*k)         # s

N_x = int(L/h)
N_t = 10000

T0 = 300                        # K
T1 = 350                        # K