import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from astropy.constants import G, M_sun, au
import VEC2D as vec
import scienceplots


#----------------------------------------------------------
#                   FUNZIONI
#----------------------------------------------------------

# def InitValues(orbit: str):
#     # inizializzazione di posizioni e velocità come array Nbody X Nsteps
#     # di vettori nulli (equivalente ad np.zeros() per scalari)
#     positions = np.full((2, N_steps), fill_value=vec.vec2d())
#     velocities = np.full((2, N_steps), fill_value=vec.vec2d())

#     # settaggio delle condizioni iniziali
#     positions[0, 0] = pos_A
#     positions[1,0] = pos_B

#     velocities[0,0] = Vel_A
#     velocities[1,0] = Vel_B

#     return positions, velocities


# funzione per calcolare le distanze tra corpi
def GetDistances(positions):
    # matrice quadrata simmetrica delle distanze
    dist = np.full((2, 2), fill_value=vec.vec2d())

    for i in range(2):
        for j in range(i+1, 2):
            dist[i,j] = positions[i] - positions[j]
            dist[j,i] = dist[i,j]

    return dist


# funzione per calcolare le accelerazioni tra corpi
def GetAccelerations(distances):
    # matrice quadrata anti-simmetrica delle accelerazioni
    acc = np.full((2, 2), fill_value=vec.vec2d())

    for i in range(2):
        for j in range(i+1, 2):
            dist_ij = distances[i,j]
            acc[i,j] = -G_const*M_body * Conv / dist_ij.mod()**2 * dist_ij.unit()
            acc[j,i] = -acc[i,j]

    # restituisce la somma vettoriale delle accelerazioni agenti su un corpo
    return np.sum(acc, axis=1)


# funzione per implementare il Verlet
def DoVerlet(old_positions, old_velocities):
    old_distances = GetDistances(old_positions)
    old_forces = GetAccelerations(old_distances)

    new_positions = old_positions + old_velocities*Tau + 0.5*old_forces*Tau**2
    new_distances = GetDistances(new_positions)
    new_forces = GetAccelerations(new_distances)
    new_velocities = old_velocities + 0.5*(old_forces + new_forces)*Tau

    return new_positions, new_velocities


# funzione di run della simulazione
# def RunSimulation():

#     positions = np.full((2, N_steps), fill_value=vec.vec2d())
#     velocities = np.full((2, N_steps), fill_value=vec.vec2d())
#     time_array = np.arange(0, N_steps*Tau, Tau)

#     for i in range(N_steps-1):

#         # passiamo al Verlet i vettori riga contenenti posizioni e velocità di tutti i corpi
#         positions[:,i+1], velocities[:,i+1] = DoVerlet(positions[:,i], velocities[:,i])

#     return positions, velocities, time_array




#----------------------------------------------------------
#                       MAIN
#----------------------------------------------------------

# Parametri di simulazione
N_steps = 5000
N_cycles = 5                        # quanti "periodi" simulare
Period = 1                          # anni (giusto per la scala del Tau)
omega = 2 * np.pi / Period          # rad/anni
Tau = N_cycles * Period / N_steps   # anni
M_body = M_sun.value                # kg
G_const = G.value                   # m^3 kg^-1 s^-2
year2sec = 3.156e+7                 # secondiàin un anno
Conv = au.value**-3 * year2sec**2   # conversione unità sec -> year, m -> A.U. 





# chiamata della funzione di run della simulazione
#positions, velocities, time_array = RunSimulation()

positions = np.full((2, N_steps), fill_value=vec.vec2d())
velocities = np.full((2, N_steps), fill_value=vec.vec2d())
time_array = np.arange(0, N_steps*Tau, Tau)

Pos0_A = vec.vec2d(2,0)
Pos0_B = vec.vec2d(-2,0)
Vel0_A = vec.vec2d(0,1)
Vel0_B = vec.vec2d(0,-1)

positions[:,0] = Pos0_A, Pos0_B
velocities[:,0] = Vel0_A, Vel0_B


for i in range(N_steps-1):

    # passiamo al Verlet i vettori riga contenenti posizioni e velocità di tutti i corpi
    positions[:,i+1], velocities[:,i+1] = DoVerlet(positions[:,i], velocities[:,i])




#----------------------------------------------------------
#                   PLOTTING
#----------------------------------------------------------

plt.style.use(['science', 'notebook', 'grid'])


# figura ed assi per l'animaizone
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(aspect='equal')


star_radius = 0.1                # raggio del ceerchio nell'animazione
lim = 2                          # limite della figura del plot  

# inizializzazione dei cerchi rappresentanti le stelle
star_A = ax.add_patch(plt.Circle((positions[0,0].x, positions[0,0].y), star_radius, fc='orange', label='#1 Body'))
star_B = ax.add_patch(plt.Circle((positions[1,0].x, positions[1,0].y), star_radius, fc='blue', label='#2 Body'))

# patch di testo per mostrare il tempo nell'animazione
time_text = ax.text(0.05, 0.93, s=f'{time_array[0]:.2f}',transform=ax.transAxes,
                    bbox=dict(facecolor='white', edgecolor='white'),
                        fontdict=dict(fontsize=12, fontweight='bold'))

# limiti del grafico dell'animazione
ax.set_ylim(-lim*2.5, lim*2.5)
ax.set_xlim(-lim*2.5, lim*2.5)

ax.set_xlabel('X (A.U.)')
ax.set_ylabel('Y (A.U.)')
ax.set_title('Astronomical 3 Body Problem Simulation', fontsize=16)
ax.legend(fontsize=12)

# funzione che gestisce l'update dell'animazione
def animate(i):
    star_A.set_center((positions[0,i].x, positions[0,i].y))
    star_B.set_center((positions[1,i].x, positions[1,i].y))

    time_text.set_text(f'Year: {time_array[i]:.2f}')

# funzione che gestisce l'animazione
anim = FuncAnimation(fig, animate, frames=N_steps, repeat=False, interval=1)

fig.tight_layout()
plt.show()



# figura ed assi per il grafico delle traiettorie
fig0, ax0 = plt.subplots()

# scatter plot delle posizioni iniziali
ax0.scatter(positions[0,0].x, positions[0,0].y, color='orange', label='#1 Body Initial Position')
ax0.scatter(positions[1,0].x, positions[1,0].y, color='blue', label='#2 Body Initial Position')

# line plot delle traiettorie
ax0.plot([positions[0,i].x for i in range(N_steps)], [positions[0,i].y for i in range(N_steps)], color='orange', label='#1 Body Trajectory')
ax0.plot([positions[1,i].x for i in range(N_steps)], [positions[1,i].y for i in range(N_steps)], color='blue', label='#2 Body Trajectory')

# personalizzazione assi
ax0.set_xlabel('X (A.U.)')
ax0.set_ylabel('Y (A.U.)')
ax0.set_title('Astronomical 3 Body Problem Orbits', fontsize=16)
ax0.legend(fontsize=10, ncols=2, frameon=True, loc='lower right', framealpha=0.7)

fig0.tight_layout()
plt.show()