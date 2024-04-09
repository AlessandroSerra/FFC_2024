import numpy as np
import matplotlib.pyplot as plt
import scienceplots

plt.style.use(['science', 'notebook', 'grid'])


def accelerazione(theta):
    return -G/L * np.sin(theta)


def eulero(old_theta, old_omega):
    new_theta = old_theta + old_omega*dT
    new_omega = old_omega + accelerazione(old_theta)*dT

    return new_theta, new_omega



def eulcr(old_theta, old_omega):
    new_omega = old_omega + accelerazione(old_theta)*dT
    new_theta = old_theta + new_omega*dT

    return new_theta, new_omega


def verlet(old_theta, old_omega):
    new_theta = old_theta + old_omega*dT + 0.5*accelerazione(old_theta)*dT**2
    new_omega = old_omega + 0.5*(accelerazione(old_theta) + accelerazione(new_theta))*dT

    return new_theta, new_omega


def get_energy(theta, omega):
    cinetica = 0.5 * L**2 * omega**2
    potenziale = - G*L*np.cos(theta)

    return cinetica, potenziale




G = 9.81                            # m/s^2
L = 0.2                             # m
N_steps = 1000

Omega = np.sqrt(G/L)                # rad/s
N_cicli = 10
Periodo = 2*np.pi / Omega           # s      
dT = N_cicli * Periodo / N_steps    # s

Theta0 = 5 * np.pi / 6              # rad
Omega0 = 0                          # rad/s


theta_array = np.zeros(N_steps)
omega_array = np.zeros(N_steps)
cinetica_array = np.zeros(N_steps)
potenziale_array = np.zeros(N_steps)

## NOTE: in classe ho chiamato get_energy PRIMA di mettere i valori iniziali di posizione e velocità
## NOTE: nei relativi array, quindi calcolava l'energia potenziale di 0 e non di Pos0

time_array = [0]

theta_array[0] = Theta0
omega_array[0] = Omega0

Cin0, Pot0 = get_energy(theta_array[0], omega_array[0])

cinetica_array[0] = Cin0
potenziale_array[0] = Pot0



for i in range(N_steps-1):

    ## NOTE: per cambiare algoritmo modificate la funzione qua sotto in: eulero, eulcr o verlet
    theta_array[i+1], omega_array[i+1] = eulcr(theta_array[i], omega_array[i])

    cinetica_array[i+1], potenziale_array[i+1] = get_energy(theta_array[i+1], omega_array[i+1])

    time_array.append((i+1)*dT)




fig, ax = plt.subplots(figsize=(10,8))

ax.plot(time_array, theta_array, label='$\\theta (t)$')
ax.axhline(y=Theta0, color='r', linestyle='--')
ax.axhline(y=-Theta0, color='r', linestyle='--')
ax.set_xlabel('Time [s]')
ax.set_ylabel('$\\theta [rad]$')
ax.set_title('Posizione in funzione del tempo')
ax.legend()



fig1, ax1 = plt.subplots(figsize=(10,8))

ax1.plot(time_array, cinetica_array, label='Cinetica')
ax1.plot(time_array, potenziale_array, label='Potenziale')
ax1.plot(time_array, cinetica_array + potenziale_array, label='Etot')
ax1.set_title('Energia cinetica, potenziale e totale in funzione del tempo')
ax1.legend()

plt.show()