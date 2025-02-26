import math
from abc import ABC, abstractmethod
import generator
from numgen import GammaGenerator

class BaseGeneratorTest(ABC):
    def __init__(self, values, n):
        self.values = values
        self.n = n

    @abstractmethod
    def calc_char(self):
        pass

    @abstractmethod
    def calc_frequently(self):
        pass

class GeneratorTest(BaseGeneratorTest):
    m_exact = 0.5
    d_exact = 0.0833
    b_exact = 0.2885

    l_bound = 0.2113
    r_bound = 0.7887
    p = 57.7

    def calc_char(self):
        k = 1 / self.n

        e = sum(self.values)
        m = k * e

        dp = 0
        for i in self.values:
            dp += (i - m) ** 2
        d = k * dp

        b = math.sqrt(d)

        print(f'm = {m}, m - m_exact = {abs(m - self.m_exact)}')
        print(f'd = {d}, d - d_exact = {abs(d - self.d_exact)}')
        print(f'b = {b}, b - b_exact = {abs(b - self.b_exact)}')

        return m, d, b

    def calc_frequently(self):
        self.calc_char()
        count = sum(1 for x in self.values if self.l_bound < x < self.r_bound)
        total = len(self.values)
        perc = (count / total) * 100
        print(f'count = {count}, total = {total}, percentage = {perc}')

        count_l = sum(1 for x in self.values if 0 < x < 0.5)
        count_r = sum(1 for x in self.values if 0.5 < x < 1)
        print(f'count_l = {count_l}, count_r = {count_r}')

class NumpyTest(BaseGeneratorTest):
    def calc_char(self):
        k = 1 / self.n

        e = sum(self.values)
        m = k * e

        dp = 0
        for i in self.values:
            dp += (i - m) ** 2
        d = k * dp

        b = math.sqrt(d)

        print(f'm = {m}')
        print(f'd = {m}')
        print(f'b = {b}')

        return (m, d, b)

    def calc_frequently(self):
        self.calc_char()

def prepare_date(n):
    oper = generator.TrigonomicOperations(n, -1)
    gen = generator.Generator(oper)
    values = gen.generate(n)
    print(values)
    gt = GeneratorTest(values, n)
    return gt

def prepare_numpy_date(n):
    gg = GammaGenerator(3)
    values = gg.generate(150)
    nt = NumpyTest(values, n)
    print(values)
    return nt

def vars(n):
    gt = prepare_date(n)
    gt.calc_frequently()

def numpy_vars(n):
    nt = prepare_numpy_date(n)
    nt.calc_frequently()

if __name__ == "__main__":
    print("n = 20")
    vars(20)
    print("n = 150")
    vars(150)
    print("n = 500")
    vars(308)

    print("numpy gamma")
    numpy_vars(150)
