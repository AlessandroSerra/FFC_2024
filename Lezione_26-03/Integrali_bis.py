import numpy as np
import matplotlib.pyplot as plt


# funzione che d=svolge il ruolo della f(x)
def funzione(x):

    return x**4 - 2*x + 1


# funzione per implementare il metodo dei trapezoidi
def trapezoidi(x, y):

    h = np.abs(x[1] - x[0])
    integrale = h/2 * (y[0] + y[-1]) + h * np.sum(y[1:-1])
    return integrale


# funzione per implementare il metodo di sim
def simpson(x, y):

    h = np.abs(x[1] - x[0])
    integrale = h/3 * ((y[0] + y[-1]) + 4*np.sum(y[1:-1:2]) + 2*np.sum(y[2:-1:2]))
    return integrale


# funzione per calcolare l'errore dei due metodi
def calcola_errore(integrale, valore_esatto):

    errore_relativo = np.abs((integrale - valore_esatto) / valore_esatto)
    return errore_relativo





# estremi dell'intervallo
A = 0
B = 2


N_list = np.arange(10, 1000, 10)
valore_esatto = 4.4

integrali_trapezi = []
integrali_simpson = []

errori_trapezi = []
errori_simpson = []


for N in N_list:

    x = np.linspace(A, B, N+1)
    y = funzione(x)

    trap = trapezoidi(x, y)
    simps = simpson(x, y)

    errori_trap = calcola_errore(trap, valore_esatto)
    errori_simps = calcola_errore(simps, valore_esatto)

    integrali_trapezi.append(trap)
    integrali_simpson.append(simps)
    errori_trapezi.append(errori_trap)
    errori_simpson.append(errori_simps)



fig, ax = plt.subplots()

ax.plot(N_list, integrali_trapezi, label='Trapezoidi')
ax.plot(N_list, integrali_simpson, label='Simpson')
ax.set_xlabel('Numero di Intervallini')
ax.set_ylabel('Valore dell\'integrale')

plt.show()
