import pytest
import simpy

import task1_python
from Lab4.numgen import GammaGenerator
from Lab4.generator import Generator, TrigonomicOperations
from Lab5.task1_2_simpy import System, customer_generator
import Lab5.task2_python

T1_REJECT = 0.15
T1_ACCEPT = 0.85
T1_LCMO = 4.86
T1_TCMO = 6.95

T2_REJECT = 10e-4
T2_ACCEPT = 1
T2_L = 10e-4

T2_REJECTN = 0
T2_ACCEPTN = 1
T2_LN = 10e-4

def prepare_task1():
    lambda_value = 0.7
    limit = 3
    service_time = 1.25
    max_time = 3000
    oper = TrigonomicOperations(10, -1)
    generator = Generator(oper)
    gg = GammaGenerator(1 / lambda_value)
    server = task1_python.LimitedSingleServer(limit, generator, service_time, lambda_value)
    return server

def prepare_task1_simpy():
    env = simpy.Environment()
    system_capacity = 3
    arrival_rate = 0.7
    gg = GammaGenerator(1 / arrival_rate)

    oper = TrigonomicOperations(10, -1)
    generator = Generator(oper)
    system = System(env, system_capacity, generator, 1, service_time= 1.25)
    return system, env, generator, arrival_rate

def test_theoretical_task1():
    server = prepare_task1()
    p_reject, p_accept, lcmo, tcmo = server.get_theoretical()
    assert round(p_reject, 2) == T1_REJECT
    assert round(p_accept, 2) == T1_ACCEPT
    assert round(lcmo, 2) == T1_LCMO
    assert round(tcmo, 2) == T1_TCMO

def test_experimental_task1():
    server = prepare_task1()
    server.simulate_system(3000)
    p_reject, p_accept = server.get_values()
    assert round(p_reject, 2) == pytest.approx(T1_REJECT, 1)
    assert round(p_accept, 2) == pytest.approx(T1_ACCEPT, 1)

def test_experimental_task1_simpy():
    system, env, generator, arrival_rate = prepare_task1_simpy()
    env.process(customer_generator(env, system, generator, arrival_rate))
    env.run(until=3000)

    p_reject, p_accept, avg = system.get_values()
    assert round(p_reject, 2) == pytest.approx(T1_REJECT, 1)
    assert round(p_accept, 2) == pytest.approx(T1_ACCEPT, 1)

def prepare_task2_limit():
    num_servers = 5
    max_queue_length = 3
    arrival_time = 0.8
    service_time = 1

    system = Lab5.task2_python.System(num_servers, max_queue_length, arrival_time, service_time, True)
    return system

def prepare_task2_non_limit():
    num_servers = 5
    max_queue_length = 3
    total_time = 3000
    arrival_time = 0.8
    service_time = 1

    system = Lab5.task2_python.System(num_servers, None, arrival_time, service_time, True)
    return system

def test_theoretical_task2_limit():
    system = prepare_task2_limit()
    p_reject, p_accept, lq = system.get_theoretical()
    assert round(p_reject, 2) == pytest.approx(T2_REJECT, 1)
    assert round(p_accept, 2) == pytest.approx(T2_ACCEPT, 1)
    assert round(lq, 2) == pytest.approx(T2_L, 1)

def test_theoretical_task2_non_limit():
    system = prepare_task2_non_limit()
    p_reject, p_accept, lq = system.get_theoretical()
    assert round(p_reject, 2) == pytest.approx(T2_REJECTN, 1)
    assert round(p_accept, 2) == pytest.approx(T2_ACCEPTN, 1)
    assert round(lq, 2) == pytest.approx(T2_LN, 1)

def test_experimental_task2_limit():
    system = prepare_task2_limit()
    total_time = 3000
    system.simulate(total_time)
    p_reject, p_accept, lq = system.get_values()
    assert round(p_reject, 2) == pytest.approx(T2_REJECT, 1)
    assert round(p_accept, 2) == pytest.approx(T2_ACCEPT, 1)
    assert round(lq, 2) == pytest.approx(T2_L, 100)

def test_experimental_task2_non_limit():
    system = prepare_task2_non_limit()
    total_time = 3000
    system.simulate(total_time)
    p_reject, p_accept, lq = system.get_values()
    assert round(p_reject, 2) == pytest.approx(T2_REJECTN, 1)
    assert round(p_accept, 2) == pytest.approx(T2_ACCEPTN, 1)
    assert round(lq, 2) == pytest.approx(T2_LN, 100)

def prepare_task2_simpy():
    env = simpy.Environment()
    system_capacity = 5
    arrival_rate = 0.7
    gg = GammaGenerator(1 / arrival_rate)

    oper = TrigonomicOperations(10, -1)
    generator = Generator(oper)
    system = System(env, system_capacity, generator, 5, service_time=1.25)
    return system, env, generator, arrival_rate

def test_experimental_task2_simpy():
    system, env, generator, arrival_rate = prepare_task2_simpy()
    env.process(customer_generator(env, system, generator, arrival_rate))
    env.run(until=3000)

    p_reject, p_accept, lq = system.get_values()
    assert round(p_reject, 2) == pytest.approx(T2_REJECT, 1)
    assert round(p_accept, 2) == pytest.approx(T2_ACCEPT, 1)
    assert round(lq, 2) == pytest.approx(T2_L, 1000)