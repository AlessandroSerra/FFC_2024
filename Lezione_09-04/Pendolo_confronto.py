import numpy as np
import matplotlib.pyplot as plt
import scienceplots

plt.style.use(['science', 'notebook', 'grid'])

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

Theta0 = 5 * np.pi / 6
Vel0 = 0


theta_eul, vel_eul, k_eul, pot_eul, time = simulate(eulero)
theta_eulcr, vel_eulcr, k_eulcr, pot_eulcr, time = simulate(eulero_cromer)
theta_verl, vel_verl, k_verl, pot_verl, time = simulate(verlet)


fig0, ax0 = plt.subplots(3, figsize=(8,6), sharex=True)

ax0[0].plot(time, theta_eul, label='eulero')
ax0[0].set_ylabel('$\\theta(t)$')
ax0[0].legend(loc=1, fontsize=10, framealpha=0.7)

ax0[1].plot(time, theta_eulcr, color='orange', label='eulero-cromer')
ax0[1].set_ylabel('$\\theta(t)$')
ax0[1].legend(loc=1, fontsize=10, framealpha=0.7)

ax0[2].plot(time, theta_verl, color='green', label=' verlet')
ax0[2].set_xlabel('Time')
ax0[2].set_ylabel('$\\theta(t)$')
ax0[2].legend(loc=1, fontsize=10, framealpha=0.7)
fig0.tight_layout()


fig1, ax1 = plt.subplots(3, figsize=(8,6), sharex=True)

ax1[0].plot(time, k_eul, label='K eulero')
ax1[0].plot(time, pot_eul, label='V eulero')
ax1[0].plot(time, (k_eul + pot_eul), label='Etot eulero')
ax1[0].set_ylabel('Energy')
ax1[0].legend(loc=1, fontsize=10, framealpha=0.7)

ax1[1].plot(time, k_eulcr, label='K eulero-cromer')
ax1[1].plot(time, pot_eulcr, label='V eulero-cromer')
ax1[1].plot(time, (np.array(k_eulcr) + np.array(pot_eulcr)), label='Etot eulero-cromer')
ax1[1].set_ylabel('Energy')
ax1[1].legend(loc=1, fontsize=10, framealpha=0.7)

ax1[2].plot(time, k_verl, label='K verlet')
ax1[2].plot(time, pot_verl, label='V verlet')
ax1[2].plot(time, (np.array(k_verl) + np.array(pot_verl)), label='Etot verlet')
ax1[2].set_xlabel('Time [s]')
ax1[2].set_ylabel('Energy')
ax1[2].legend(loc=1, fontsize=10, framealpha=0.7)
fig1.tight_layout()

plt.show()

