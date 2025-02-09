from Lab2.solver import Solver
import pytest

solver = Solver()

def test_temp():
    solver.calculate_temp_vars()
    assert solver.mu == 650
    assert round(solver.mb, 2) == 34.14
    assert round(solver.mbg, 2) == 334.56
    assert round(solver.k1, 2) == 1225.22
    assert round(solver.m, 2) == 37.28

def test_t_v_h():
    t, v, h = solver.calculate_speed_height()
    assert t[1] == 0.02
    assert t[2] == 0.04
    assert t[8] == 0.16

    assert round(v[1], 2) == 0.12
    assert round(v[2], 2) == 0.19
    assert round(v[8], 2) == 0.27

    assert round(h[1], 2) == 0.0
    assert round(h[2], 2) == 0.01
    assert round(h[8], 2) == 0.04