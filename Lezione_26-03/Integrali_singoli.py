import numpy as np
import matplotlib.pyplot as plt


def funzione(x):

    return x**4 -2*x + 1


def trapezoidi(x, y):

    h = np.abs(x[1] - x[0])
    integrale = h/2 * (y[0] + y[-1]) + h * np.sum(y[1:-1])
    return integrale


def simpson(x, y):

    h = np.abs(x[1] - x[0])
    integrale = h/3 * ((y[0] + y[-1]) + 4*np.sum(y[1:-1:2]) + 2*np.sum(y[2:-1:2]))
    return integrale



def calcola_errore(integrale, valore_esatto):

    relative_err = np.abs((integrale - valore_esatto) / valore_esatto)
    return relative_err



# provate a cambiare l'intervallo
N_interv = 10
A = 0
B = 2

x_list = np.linspace(A, B, N_interv+1)
y_list = funzione(x_list)
N = len(x_list)
valore_esatto = 4.4


integrale_trap = trapezoidi(x_list, y_list)
integrale_simps = simpson(x_list, y_list)


errore_trapezi = calcola_errore(integrale_trap, valore_esatto)
errore_simpson = calcola_errore(integrale_simps, valore_esatto)


# invece di plottare gli integrali, che sarebbero solo dei punti dato che consideriamo
# un solo intervallo, stampiamoli a schermo in una tabellina ordinata

print('-'*73)
print('|\tEsatto\t |\t Trapezoidi\t |\t Simpson\t\t|')
print('-'*73)
print(f'|\t{valore_esatto:.2f}\t |\t {integrale_trap:.6f}\t |\t {integrale_simps:.6f}\t\t|')
print('-'*73)
print(f'|    Err. rel.\t |\t {errore_trapezi:.6f}\t |\t {errore_simpson:.6f}\t\t|')
print('-'*73)
