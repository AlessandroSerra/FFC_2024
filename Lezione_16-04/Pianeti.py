import matplotlib.pyplot as plt
import numpy as np

import vettori2d as vec

## from astropy import G, M_sun, au



def GetDistances(positions):
    dist = np.full((2, 2), fill_value=vec.vec2d())

    for i in range(2):
        for j in range(i+1, 2):

            dist[i,j] = positions[i] - positions[j]
            dist[j,i] = -dist[i,j]

    return dist


def GetAccelerations(dist):

    acc = np.full((2, 2), fill_value=vec.vec2d())

    for i in range(2):
        for j in range(i+1, 2):

            dist_ij = dist[i,j]
            acc[i,j] = -G_value*M_body*Conv / dist_ij.mod()**2 * dist_ij.unit()
            acc[j,i] = acc[i,j]

    return np.sum(acc, axis=1)


def DoVerlet():
    pass





N_steps = 5000
N_cycles = 5
Period = 1                              # anni
Tau = N_cycles * Period / N_steps       # anni
G_value = 6.6743e-11                    # m^3 kg^-1 s^-2
M_body = 1.988409870698051e+30          # kg
AU_value = 149597870700.0               # m
year2sec = np.pi * 1e7                  # anni -> secondi
Conv = AU_value**-3 * year2sec**2


positions = np.full((2, N_steps), fill_value=vec.vec2d())


GetDistances(positions)
