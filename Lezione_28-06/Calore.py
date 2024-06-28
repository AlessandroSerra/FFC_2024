import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

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


def fitAmplitudes(Temps):
    def func(x, A, B, C):
        return A*np.exp(-x/B) + C
    
    max_Ts = np.max(Temps, axis=0)
    times = np.arange(N_t) * dt

    popt, pcov = curve_fit(func, times, max_Ts, p0=[np.max(max_Ts), (N_t//2)*dt, np.min(max_Ts)])
    amps_fit = func(times, *popt)

    return times, max_Ts, amps_fit


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

times, max_Ts, amps_fit = fitAmplitudes(Temps)


fig, ax = plt.subplots()

for i in range(0, N_t, N_t//10):
    ax.plot(Temps[:, i], label=f'Timestep: {i}')

ax.set_xlabel('x [m]')
ax.set_ylabel('T [K]')
ax.legend()


fig1, ax1 = plt.subplots()

ax1.scatter(times, max_Ts, s=2, label='Ampiezze')
ax1.plot(times, amps_fit, label='Fit', color='red')
ax1.set_xlabel('t [s]')
ax1.set_ylabel('T [K]')
ax1.legend()

plt.show()