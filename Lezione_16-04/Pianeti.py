import matplotlib.pyplot as plt
import numpy as np
import vettori2d as vec
from astropy.constants import G, M_sun, au


def GetDistances(positions):
    dist = np.full((2, 2), fill_value=vec.vec2d())

    for i in range(2):
        for j in range(i+1, 2):

            dist[i, j] = positions[i] - positions[j]
            dist[j, i] = -dist[i, j]

    return dist


def GetAccelerations(dist):

    acc = np.full((2, 2), fill_value=vec.vec2d())

    for i in range(2):
        for j in range(i + 1, 2):

            dist_ij = dist[i, j]
            acc[i, j] = -G_value * M_body * Conv / dist_ij.mod()**2 * dist_ij.unit()
            acc[j, i] = -acc[i, j]

    return np.sum(acc, axis=1)


# old = timestep i,   new = timestep i+1
def DoVerlet(old_positions, old_velocities):
    
    old_distances = GetDistances(old_positions)
    old_accelerations = GetAccelerations(old_distances)

    new_positions = old_positions + old_velocities*Tau + 0.5*old_accelerations*Tau**2

    new_distances = GetDistances(new_positions)
    new_accelerations = GetAccelerations(new_distances)

    new_velocities = old_velocities + 0.5*(old_accelerations + new_accelerations)*Tau

    return new_positions, new_velocities




N_steps = 5000
N_cycles = 5
Period = 1  # anni
Tau = N_cycles * Period / N_steps  # anni
G_value = 6.6743e-11  # m^3 kg^-1 s^-2
M_body = 1.988e30  # kg
AU_value = 149597870700.0  # m
year2sec = np.pi * 1e7  # anni -> secondi
Conv = AU_value**-3 * year2sec**2



positions = np.full((2, N_steps), fill_value=vec.vec2d())
velocities = np.full((2, N_steps), fill_value=vec.vec2d())


Pos0_1 = vec.vec2d(-2, 0)               # A.U.
Pos0_2 = vec.vec2d(2, 0)                # A.U.
Vel0_1 = vec.vec2d(0, -1)               # A.U./years
Vel0_2 = vec.vec2d(0, 1)                # A.U./years

positions[:,0] = Pos0_1, Pos0_2
velocities[:,0] = Vel0_1, Vel0_2


for i in range(N_steps-1):

    positions[:,i+1], velocities[:,i+1] = DoVerlet(positions[:,i], velocities[:,i])



fig, ax = plt.subplots()

ax.plot([positions[0,i].x for i in range(N_steps)], [positions[0,i].y for i in range(N_steps)], label='Corpo 1')
ax.plot([positions[1,i].x for i in range(N_steps)], [positions[1,i].y for i in range(N_steps)], label='Corpo 1')
ax.set_xlabel('x [A.U.]')
ax.set_ylabel('y [A.U.]')
ax.set_title('Orbita di due corpi')
ax.legend()

fig.tight_layout()
plt.show()