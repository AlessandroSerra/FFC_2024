import numpy as np
import matplotlib.pyplot as plt

import scienceplots
plt.style.use(['science', 'notebook'])

def FourierT(y, t):
    
    tau = np.abs(t[1] - t[0])
    nu = np.arange(-N/2, N/2) / T
    ft = []

    for i in range(N):

        ft.append(np.sum(y * np.exp(2j * np.pi * nu[i] * t)))

    F = np.array(ft) * tau

    return nu, F



def AntiFourier(f, nu):
    
    nu_max = N / T
    t = np.arange(1, N+1) / nu_max
    delta_nu = np.abs(nu[1] - nu[0])
    invft = []

    for i in range(N):

        invft.append(np.sum(f * np.exp(-2j * np.pi * nu * t[i])))

    inv_FT = np.array(invft) * delta_nu


    f1 = f.copy()

    # mandiamo a zero i coefficienti relativi a frequenze che stanno
    # dopo un certo valore di frequenza, come fosse un cut-off
    for k in range(N):
        if np.abs(nu[k]) > 0.02 * nu_max:
            f1[k] = 0

    invft2 = []

    for i in range(N):

        invft2.append(np.sum(f1 * np.exp(-2j * np.pi * nu * t[i])))

    inv_FT2 = np.array(invft2) * delta_nu

    return t, inv_FT, inv_FT2


dati = np.loadtxt('Lezione_14-05/sp500.txt', skiprows=1)
tempi = dati[:,0]
prezzi = dati[:,1]

N = len(prezzi)
T = tempi[-1]


freq, trasf = FourierT(prezzi, tempi)

tempi_anti, antitraf, antitraf2 = AntiFourier(trasf, freq)



fig0, ax0 = plt.subplots()

ax0.plot(freq, np.abs(trasf))
ax0.set_xlabel('Frequenze [d-1]')
ax0.set_ylabel('Trasformata [U.A.]')
ax0.set_title('Grafico della trasformata dei dati di sp500')

plt.show()


fig, ax = plt.subplots()

ax.plot(tempi, prezzi, label='Dati originali', linewidth=2)
ax.plot(tempi_anti, antitraf2, label='Antitrasformata', linewidth=2)
ax.set_xlabel('Tempi [d]')
ax.set_ylabel('Prezzi [U.A.]')
ax.set_title('Dati originali vs Antitrasformata')
ax.legend()


plt.show()