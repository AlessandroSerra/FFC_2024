import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

def TimeIt(func: callable, args: tuple):

    start = dt.datetime.now()
    values = func(*args)
    stop = dt.datetime.now()

    value = func(*args)
    time = (stop - start).microseconds

    return value, time


def function(x: float) -> float:
    return  x**4 - 2*x + 1


def trapezoid(exact: float, thresh: float) -> float:

    i = 1

    while True:
        x = np.linspace(0, 2, 10*i + 1)
        y = function(x)

        h = np.abs(x[1] - x[0])
        integral = h/2 * (y[0] + y[-1]) + h * np.sum(y[1:-1])

        diff = np.abs(integral - exact)

        if diff < thresh:
            return integral

        i += 1


def simpson(exact: float, thresh: float) -> float:

    i = 1

    while True:
        x = np.linspace(0, 2, 10*i + 1)
        y = function(x)

        h = np.abs(x[1] - x[0])
        integral = h/3 * (y[0] + y[-1] + 4*np.sum(y[1:-1:2]) + 2*np.sum(y[2:-1:2]))

        diff = np.abs(integral - exact)

        if diff < thresh:
            return integral

        i += 1


exact = 4.4
thresh_list = [10**(-i) for i in range(1, 7)]

trap_values, trap_times = [], []
simp_values, simp_times = [], []

for i in range(len(thresh_list)):
    value, time = TimeIt(trapezoid, (exact, thresh_list[i]))
    value2, time2 = TimeIt(simpson, (exact, thresh_list[i]))

    trap_times.append(time)
    simp_times.append(time2)


fig, ax = plt.subplots()

ax.plot(trap_times, thresh_list, marker='o', linewidth=1, label = 'trap')
ax.plot(simp_times, thresh_list, marker='o', linewidth=1, label = 'simps')
ax.set_xlabel('Time [$\mu s$]')
ax.set_ylabel('Threshold [log]')
ax.set_yscale('log')
ax.set_title('Time comparison between Simpson and Trapezoid Integration')
ax.legend()

plt.show()