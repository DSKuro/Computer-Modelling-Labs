from practice.classes.Function import Function
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

from practice.classes.System import FunctionsSystem

def process_system(system, y0, start, stop, step):
    ti = np.arange(start, stop, step)
    sol = odeint(system.execute, y0, ti)
    x = sol[:, 0]
    y = sol[:, 1]
    z = sol[:, 2]
    return x, y, z, ti

def create_graphics(x, y, z, ti):
    create_y_x(x, y)
    create_x_ti(x, ti)
    create_ti_y(ti, y)
    create_ti_z(ti, z)
    plt.show()


def create_y_x(x, y):
    plt.subplot(221)
    plt.plot(x, y, lw=1)
    plt.title("Фазовый портрет")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()

def create_x_ti(x, ti):
    plt.subplot(222)
    plt.plot(ti, x, lw=1, color="orange")
    plt.title("x(t)")
    plt.xlabel("t")
    plt.ylabel("x")
    plt.grid(); plt.tight_layout()

def create_ti_y(ti, y):
    plt.subplot(223)
    plt.plot(ti, y, lw=1, color="g")
    plt.title("y(t)")
    plt.xlabel("t")
    plt.ylabel("y")
    plt.grid(); plt.tight_layout()

def create_ti_z(ti, z):
    plt.subplot(224)
    plt.plot(ti, z, lw=1, color="r")
    plt.title("z(t)")
    plt.xlabel("t")
    plt.ylabel("z")
    plt.grid(); plt.tight_layout()

def process_all(funcs,
                      a,
                      b,
                      c,
                      y0,
                      start,
                      stop,
                      step):
    system = FunctionsSystem([funcs[0], funcs[1], funcs[2]])
    system.set_params(a, b, c)

    x1, y1, z1, ti1 = process_system(system, y0, start, stop, step)
    return x1, y1, z1, ti1

def refresh_plots2(pl, ti, z, x, y):
    v_g = pl.add_subplot(2, 2, 1)
    v_g.plot(x, y, lw=1)
    v_g.set_title("Фазовый портрет")
    v_g.set_xlabel("x")
    v_g.set_ylabel("y")
    v_g.grid()

    v_g = pl.add_subplot(2, 2, 2)
    v_g.plot(ti, x, lw=1, color="orange")
    v_g.set_title("x(t)")
    v_g.set_xlabel("t")
    v_g.set_ylabel("x")
    v_g.grid()

    v_g = pl.add_subplot(2, 2, 3)
    v_g.plot(ti, y, lw=1, color="g")
    v_g.set_title("y(t)")
    v_g.set_xlabel("t")
    v_g.set_ylabel("y")
    v_g.grid()

    v_g = pl.add_subplot(2, 2, 4)
    v_g.plot(ti, z, lw=1, color="r")
    v_g.set_title("z(t)")
    v_g.set_xlabel("t")
    v_g.set_ylabel("z")
    v_g.grid()

    return v_g

def process_test_func():
    a = -8 / 3
    b = -10
    c = 28

    func1 = Function(lambda v, u, e: a * v + u * e)
    func2 = Function(lambda v, u, e: b * (u - e))
    func3 = Function(lambda v, u, e: -v * u + c * u - e)

    process_all([func1, func2, func3], a, b, c, [1, 1, 1], 0, 100, 0.01)


def process_func():
    a = 0.2
    b = 0.2
    c = 5
    y0 = [1, 1, 1]
    start = 0
    stop = 100
    step = 0.01

    func1 = Function(lambda x, y, z: -y-z)
    func2 = Function(lambda x, y, z: x+a*y)
    func3 = Function(lambda x, y, z: b+z*(x-c))

    x, y, z, ti = process_all([func1, func2, func3], a, b, c, y0, start, stop, step)
    create_graphics(x, y, z, ti)

if __name__ == "__main__":
    #process_test_func()
    process_func()

