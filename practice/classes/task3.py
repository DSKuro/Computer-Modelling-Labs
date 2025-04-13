import math

from practice.classes.Function import Function
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def func3(y, t):
    p, p1 = y
    dydt = [p1, -0.1*p]
    return dydt

def first_func(y, t):
    p, p1 = y
    dydt = [p1, math.cos(t) - 3 * p - 2 * p1]
    return dydt

def second_func(z, a):
    x, y = z
    return [y, a * (1 - x ** 2) * y - x]

def process_calculation(func, start, stop, step, y0):
    ti = np.arange(start, stop, step)
    sol = odeint(func, y0, ti)
    return ti, sol[:, 0], sol[:, 1]

def create_graphics(ti, x, y):
    plt.plot(ti, x, "r", label="y")
    plt.plot(ti, y, "g", label="y'")
    plt.xlabel("t", fontsize=17)
    plt.ylabel("y", fontsize=17)
    plt.grid()
    plt.legend()
    plt.show()

def process_test_func():
    ti, x, y = process_calculation(func3, 0, 20, 0.1, [1, 0])
    create_graphics(ti, x, y)

def process_first_func(start, stop, step, y0):
    ti, x, y = process_calculation(first_func, start, stop, step, y0)
    return ti, x, y

def process_second_func(start, stop, step, y0):
    ti, x, y = process_calculation(first_func, start, stop, step, y0)
    return ti, x, y

def refresh_plots3(pl, ti, x, y):
    v_g = pl.add_subplot(1, 1, 1)
    v_g.plot(ti, x, "r", label="y")
    v_g.plot(ti, y, "g", label="y'")
    v_g.set_xlabel("t", fontsize=17)
    v_g.set_ylabel("y", fontsize=17)
    v_g.grid()
    v_g.legend()
    return v_g


if __name__ == "__main__":
    #process_test_func()
    #process_first_func()
    process_second_func(0, 30, 0.01, [2, 0])
