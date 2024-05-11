import numpy as np
import matplotlib.pyplot as plt

# opzionale se installata
import scienceplots
plt.style.use(['science', 'notebook'])


def BoundaryConditions(T_old, T_new, condition):

    # primo ed ultimo delle nuove T siano uguali alle vecchie T
    if condition == 'dirichlet':
        return T_old[0], T_old[-1]

    elif condition == 'neumann':
        return T_new[1], T_new[-2]
    
    else:
        raise ValueError('La condizione deve essere o di dirichlet o di neumann')



def DoFTCS(T_old):

    T_new = T_old.copy()

    # loop nello spazio per aggiornare i valori di temperatura con l'FTCS
    for i in range(1, N_x-1):
        T_new[i] = T_old[i] + dt*k/h**2 * (T_old[i-1] + T_old[i+1] - 2*T_old[i])

    T_new[0], T_new[-1] = BoundaryConditions(T_old, T_new, condition='neumann')

    return T_new



def Solve():
    
    Temps = np.ones((N_x, N_t)) * T0

    A = int(1/3 * N_x)
    B = int(2/3 * N_x)

    Temps[A:B, 0] = T1

    for n in range(N_t-1):

        Temps[:, n+1] = DoFTCS(Temps[:,n])

    return Temps



# PARAMETRI DI SIMULAZIONE

L = 1                           # m
k = 1                           # m**2/s
h = 0.01                        # m
dt = 0.2 * h**2 / (2*k)         # s

N_x = int(L/h)
N_t = 10000

T0 = 300                        # K
T1 = 350                        # K

Temps = Solve()

# creaimo solo la figura
fig = plt.figure()

# creiamo gli assi in 3d
ax = fig.add_subplot(111, projection='3d')

# funzione necessaria per le x e le y del plot
gridx, gridy = np.meshgrid(range(N_t), range(N_x))

# plot in 3d della superficie della temperatura, restituiamo il grafico
# in una variabile per poter plottare una barra dei colori
img = ax.plot_surface(gridx, gridy, Temps, cmap=plt.cm.hot)   # aggiungiamo una mappa dei colori

##NOTE: aggiunte dopo per rendere migliore il grafico
# titoli degli assi
ax.set_xlabel('Tempo [s]')
ax.set_ylabel('Spazio [m]')
ax.set_zlabel('T [k]')
ax.set_title('Evoluzione del profilo di temperatura nel tempo', fontsize=20)

# colorbar per la temperatura
fig.colorbar(img, orientation = 'vertical', label = 'Temperatura [K]', shrink=0.9)

fig.tight_layout()
plt.show()