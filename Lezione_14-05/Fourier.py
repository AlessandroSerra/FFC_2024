import numpy as np
import matplotlib.pyplot as plt

# opzionale per grafici più carini
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
    t = np.arange(N+1) / nu_max
    delta_nu = np.abs(nu[1] - nu[0])
    invft = []

    for i in range(N+1):

        invft.append(np.sum(f * np.exp(-2j * np.pi * nu * t[i])))

    inv_FT = np.array(invft) * delta_nu

    return t, inv_FT






T = 1           # secondi
N = 1000        # intervallini di campionamento
freq1 = 10      # Hz
freq2 = 20      # Hz
freq3 = 30      # Hz

t = np.linspace(0, T, N)
y = np.sin(2 * np.pi / T * freq1 * t) + np.sin(2 * np.pi / T * freq2 * t) + np.sin(2 * np.pi / T * freq3 * t)


freq, trasform = FourierT(y, t)

time, antitrasf = AntiFourier(trasform, freq)




fig0, ax0 = plt.subplots()

ax0.plot(t, y, label='segnale originale')
ax0.plot(time, antitrasf, label='segnale anti-trasformata')
ax0.set_xlabel('t [s]')
ax0.set_ylabel('y [A.U.]')
ax0.set_title('Segnale originale vs segnale ricostruito con anti-trasformata')
ax0.legend(frameon=True, framealpha=0.8)


fig, ax = plt.subplots()

ax.plot(freq, np.abs(trasform), label='trasformata')
ax.set_xlabel('$\\nu$ [Hz]')
ax.set_ylabel('I [A.U.]')
ax.set_title('Modulo quadro della trasformata del segnale')
ax.text(x=-180, y=0.3, s='Frequenze\nnon\nfisiche', horizontalalignment='center', fontdict=dict(fontsize=12, fontweight='bold'))
ax.text(x=180, y=0.3, s='Frequenze\nfisiche', horizontalalignment='center', fontdict=dict(fontsize=12, fontweight='bold'))
ax.legend()

plt.show()