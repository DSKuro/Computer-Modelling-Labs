from practice.classes.Function import Function
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

r1 = 0.5
l1 = 0.01
l2 = 0.01
b2 = 0.2
g1 = 0.0005

def lotka_volterra(z, t):
    x, y = z
    dxdt = r1 * x - l1 * x * y
    dydt = l2 * x * y - b2 * y
    return [dxdt, dydt]

def concur(eq, t):
    x1, y1 = eq
    return [r1*x1-l1*x1*y1-g1*x1**2, l2*x1*y1-b2*y1]

def calculate_lotka(start, stop, step, start_param):
    t = np.arange(start, stop, step)
    sol = odeint(lotka_volterra, start_param, t)
    x = sol[:, 0]
    y = sol[:, 1]
    return t, x, y

def create_lotka_graphics(t, x, y):
    plt.plot(t, x, 'b', label='Жертвы (x)')
    plt.plot(t, y, 'r', label='Хищники (y)')
    plt.title('Динамика жертв и хищников')
    plt.xlabel('Время')
    plt.ylabel('Количество')
    plt.legend(loc='best')
    plt.show()

    plt.plot(x, y, 'g')
    plt.title('Фаза-плоскость: Жертвы vs Хищники')
    plt.xlabel('Жертвы (x)')
    plt.ylabel('Хищники (y)')
    plt.show()

def calculate_concur(start, stop, step, y0):
    ti = np.arange(start, stop, step)
    sol = odeint(concur, y0, ti)
    x = sol[:, 0]
    y = sol[:, 1]
    return ti, x, y

def create_concur_graphics(ti, x, y):
    plt.plot(ti, x, "r", label="x", lw=1)
    plt.plot(ti, y, "b", label="y", lw=1)
    plt.xlabel("t", fontsize=17)
    plt.ylabel("x, y", fontsize=17)
    plt.grid()
    plt.legend()
    plt.show()


    plt.plot(x, y, color="g", lw=1)
    plt.xlabel("x", fontsize=17)
    plt.ylabel("y", fontsize=17)
    plt.grid()
    plt.show()

def refresh_plots4(pl, t1, x1, y1, t2, x2, y2, i):
    if  i == 0:
        v_g = pl.add_subplot()
        pl.subplots_adjust(wspace=0.5, hspace=0.5)
        v_g.plot(t1, x1, 'b', label='Жертвы (x)')
        v_g.plot(t1, y1, 'r', label='Хищники (y)')
        v_g.set_title('Динамика жертв и хищников')
        v_g.set_xlabel('Время')
        v_g.set_ylabel('Количество')
        v_g.legend(loc='best')
    if i == 1:
        v_g = pl.add_subplot()
        v_g.plot(x1, y1, 'g')
        v_g.set_title('Фаза-плоскость: Жертвы vs Хищники')
        v_g.set_xlabel('Жертвы (x)')
        v_g.set_ylabel('Хищники (y)')

    if i == 2:
        v_g = pl.add_subplot()
        v_g.plot(t2, x2, "r", label="x", lw=1)
        v_g.plot(t2, y2, "b", label="y", lw=1)
        v_g.set_xlabel("t", fontsize=10)
        v_g.set_ylabel("x, y", fontsize=10)
        v_g.grid()
        v_g.legend()
    if i == 3:
        v_g = pl.add_subplot()
        v_g.plot(x2, y2, color="g", lw=1)
        v_g.set_xlabel("x", fontsize=10)
        v_g.set_ylabel("y", fontsize=10)
        v_g.grid()

def graphics(pl, start, stop, step, start_param):
    ti1, x1, y1 = calculate_lotka(start, stop, step, start_param)
    ti2, x2, y2 = calculate_concur(start, stop,step, start_param)
    refresh_plots4(pl, ti1, x1, y1, ti2, x2, y2, 0)

    return ti1, x1, y1, ti2, x2, y2

def main(start, stop, step, start_param):
    ti1, x1, y1 = calculate_lotka(start, stop, step, start_param)
    ti2, x2, y2 = calculate_concur(start, stop,step, start_param)
    create_lotka_graphics(ti1, x1, y1)
    create_concur_graphics(ti2, x2, y2)


if __name__ == "__main__":
    main(0, 700, 0.1, [25, 5])


