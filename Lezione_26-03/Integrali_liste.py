import numpy as np
import matplotlib.pyplot as plt


# funzione che d=svolge il ruolo della f(x)
def funzione(x):

    return x**4 -2*x + 1


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

# lista di x che contenga intervalli con numero variabile di punti: x[0] ha 10 intervalli, x[1] ne ha 20, etc.
x_list = [np.linspace(A, B, 10*i+1) for i in range(1, 10)]
y_list = [funzione(x) for x in x_list]      # lista di valori di y relativi alle x

N = len(x_list)                             # lunghezza della liste delle x

valore_esatto = np.array([4.4] * N)         # lista contenente N volte il valore esatto per poterlo plottare


# chiamata delle funzioni a cui passiamo gli un elemento di x_list per volta
integrale_trap = [trapezoidi(x_list[i], y_list[i]) for i in range(N)]
integrale_simps = [simpson(x_list[i], y_list[i]) for i in range(N)]


# chiamata delle funzioni per farci restituire gli errore
errore_trapezi = calcola_errore(integrale_trap, valore_esatto)
errore_simpson = calcola_errore(integrale_simps, valore_esatto)

# lista contenente il numero di punti relativi a ciascun intervallo in x_list
points = [len(element) for element in x_list]


# prima figura che contiene il plot dei due metodi al variare del numero di punti di integrazione
fig, ax = plt.subplots()

ax.plot(points, integrale_trap, marker='+', label='Trapezoidi')
ax.plot(points, integrale_simps, marker='+', label='Simpson')
ax.plot(points, valore_esatto, marker='+', label='Valore esatto')
ax.set_xlabel('Punti')
ax.set_ylabel('Valore Integrale')
ax.legend()


# seconda figura che contenga gli errori in funzione del numero di punti di integrazione
fig2, ax2 = plt.subplots()

ax2.loglog(points, errore_trapezi, marker='+', label='errore trapezi')      # grafico log-log
ax2.loglog(points, errore_simpson, marker='+', label='errore simpson')      # grafico log-log
ax2.set_xlabel('Punti')
ax2.set_ylabel('Errore')
ax2.legend()

# importante per mostrare i grafici a schermo
plt.show()