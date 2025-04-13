from practice.classes.Function import Function
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def process_func(func, start, stop, step, y0):
    ti = np.arange(start, stop, step)
    return odeint(func, y0, ti), ti

def create_graphics(pl, ti, yi):
    pl.plot(ti, yi, "o-r", alpha=0.7, lw=5, mec="g", mew=2, ms=10)
    pl.xlabel("t, time", fontsize=20)
    pl.ylabel("y", fontsize=20)
    pl.tick_params(axis="both", labelsize=15)
    pl.grid(True)

def process_first_func(start, stop, step, y0):
    func1 = Function(lambda y, t: y ** 2 - y * t)
    yi, ti = process_func(func1, start, stop, step, y0)
    return ti, yi

def process_second_func(start, stop, step, y0):
    func2 = Function(lambda y, t: y ** 2 + 1)
    yi, ti = process_func(func2, start, stop, step, y0)
    return ti, yi

def refresh_plots(pl, ti, yi):
    v_g = pl.add_subplot(1, 1, 1)
    v_g.plot(ti, yi, "o-r", alpha=0.7, lw=5, mec="g", mew=2, ms=10)
    v_g.set_xlabel("t, time", fontsize=12)
    v_g.set_ylabel("y", fontsize=12)
    v_g.tick_params(axis="both", labelsize=8)
    v_g.grid()
    return v_g

if __name__ == "__main__":

    func2 = Function(lambda y, t: y ** 2 + 1)
    yi, ti = process_func(func2, 0, 1, 0.1, 0)
    create_graphics(plt, ti, yi)
