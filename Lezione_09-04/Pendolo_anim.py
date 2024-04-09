import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.animation import PillowWriter
import scienceplots

#plt.style.use(['science', 'notebook', 'grid'])

def acceleration(theta):
    return -G/L * np.sin(theta)


def eulero(theta, vel):
    new_theta = theta + vel*Tau
    new_vel = vel + acceleration(theta)*Tau

    return new_theta, new_vel


def eulero_cromer(theta, vel):
    new_vel = vel + acceleration(theta)*Tau
    new_theta = theta + new_vel*Tau

    return new_theta, new_vel


def verlet(theta, vel):
    new_theta = theta + vel*Tau + 0.5*acceleration(theta)*Tau**2
    new_vel = vel + 0.5*(acceleration(new_theta) + acceleration(theta))*Tau

    return new_theta, new_vel


def get_energy(theta, vel):
    cinetica = 0.5 * L**2 * vel**2
    potenziale = -G*L*np.cos(theta)

    return cinetica, potenziale


def simulate(method = verlet):
    theta_array, vel_array = np.zeros(N_steps), np.zeros(N_steps)
    k_array, pot_array = np.zeros(N_steps), np.zeros(N_steps)
    time_array = np.zeros(N_steps)

    theta_array[0] = Theta0
    vel_array[0] = Vel0
    time_array[0] = 0

    k_array[0], pot_array[0] = get_energy(theta_array[0], vel_array[0])

    for i in range(N_steps - 1):

        theta_array[i+1], vel_array[i+1] = method(theta_array[i], vel_array[i])
        k_array[i+1], pot_array[i+1] = get_energy(theta_array[i], vel_array[i])
        time_array[i+1] = time_array[i] + Tau


    return theta_array, vel_array, k_array, pot_array, time_array




G = 9.81
L = 0.2
N_steps = 1000
Ncycles = 10

omega = np.sqrt(G / L)
Period = 2 * np.pi / omega
Time = Ncycles * Period
Tau = Time / N_steps

Theta0 = 3 * np.pi / 6
Vel0 = 0


theta_eul, vel_eul, k_eul, pot_eul, time = simulate(eulero)
theta_eulcr, vel_eulcr, k_eulcr, pot_eulcr, time = simulate(eulero_cromer)
theta_verl, vel_verl, k_verl, pot_verl, time = simulate(verlet)



#-----------------------------------------------------------------------------
#                            PLOTTING
#-----------------------------------------------------------------------------

# per scegliere l'algoritmo cambiate l'array che c'è prima del metodo .copy()
theta_array = theta_eul.copy()

# funzione di animazione
def animate(i):

    palla.set_offsets(np.column_stack([theta_array[i], L]))
    sbarra.set_data([theta_array[i], theta_array[i]], [0, L])


fig2, ax2 = plt.subplots(figsize=(8,6), subplot_kw={'projection': 'polar'})


sbarra, = ax2.plot([0, 0], [0, L], color='red', linewidth=2)
palla = ax2.scatter(theta_array[0], L, s=100)

ax2.set_theta_offset(np.deg2rad(-90))
ax2.set_rlim([0, L+0.2*L])
ax2.set_rticks([])
anim = animation.FuncAnimation(fig2, animate, frames=len(theta_array), interval=30, repeat=False)


# se volete salvare l'animazione
#anim.save('ani.gif',writer='pillow',fps=60,dpi=200)
plt.show()