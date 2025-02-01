from math import pi

DENSITY_OF_COPPER = 8900.0
DENSITY_OF_PETROL = 750.0
G = 9.8
R = 0.1
M = 650.0
T = 0.02
MAX_COUNT = 20

def calculate_speed_height(
        den_cop = DENSITY_OF_COPPER,
        den_pet = DENSITY_OF_PETROL,
        r = R,
        mu = M,
        max_count = MAX_COUNT,
        times = T,
        g = G
):
    mb = (den_cop - den_pet) * 4 * pi * r ** 3 / 3
    mbg = mb * g
    k1 = 6 * pi * mu * r
    m = (4 / 3) * pi * r ** 3 * den_cop
    t = []
    v = []
    h = []
    t.append(0)
    v.append(0)
    h.append(0)
    for i in range(1, max_count):
        t.append(t[i - 1] + times)
        v.append(
            v[i - 1] + times / 2 * ((mbg - k1 * v[i - 1]) / m +
                (
                mbg - k1 * (v[i - 1] + times *
                            (
                                mbg - k1 * v[i - 1]
                            ) /
                            m)
                )
                / m
            )
        )
        h.append(h[i - 1] + v[i] * times)

    print(t)
    print(v)
    return t, v, h
if __name__ == "__main__":
    calculate_speed_height()