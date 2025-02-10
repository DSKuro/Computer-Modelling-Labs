from math import pi

DENSITY_OF_COPPER = 8900.0
DENSITY_OF_PETROL = 750.0
G = 9.8
R = 0.1
M = 650.0
T = 0.02
MAX_COUNT = 20

class Solver:
    def __init__(self,
                 den_cop = DENSITY_OF_COPPER,
                 den_pet = DENSITY_OF_PETROL,
                 r = R,
                 mu = M,
                 max_count = MAX_COUNT,
                 times = T,
                 g = G):
        self.den_cop = den_cop
        self.den_pet = den_pet
        self.r = r
        self.mu = mu
        self.max_count = max_count
        self.times = times
        self.g = g
        self.mb = 0
        self.mbg = 0
        self.k1 = 0
        self.m = 0

    def __calculate_temp_vars(self):
        self.mb = (self.den_cop - self.den_pet) * 4 * pi * self.r ** 3 / 3
        self.mbg = self.mb * self.g
        self.k1 = 6 * pi * self.mu * self.r
        self.m = (4 / 3) * pi * self.r ** 3 * self.den_cop

    def calculate_speed_height(self):
        t = []
        v = []
        h = []
        t.append(0)
        v.append(0)
        h.append(0)
        for i in range(1, self.max_count):
            t.append(round(t[i - 1] + self.times, 4))
            v.append(round(
                v[i - 1] + self.times / 2 * ((self.mbg - self.k1 * v[i - 1]) / self.m +
                                        (
                                                self.mbg - self.k1 * (v[i - 1] + self.times *
                                                            (
                                                                    self.mbg - self.k1 * v[i - 1]
                                                            ) /
                                                            self.m)
                                        )
                                        / self.m
                                        )
            , 4)
            )
            h.append(
                round(h[i - 1] + v[i] * self.times, 4))

        print(t)
        print(v)
        return t, v, h

    def calculate_answer(self):
        self.__calculate_temp_vars()
        return self.calculate_speed_height()