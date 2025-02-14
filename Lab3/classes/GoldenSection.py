import math

from Lab3.classes.Extremum import Max
from Lab3.classes.Extremum import Min
from Lab3.classes.Extremum import Derative


class GoldenSection:
    _tau = (math.sqrt(5) - 1) / 2
    _iterations = 0

    @property
    def get_iterations(self):
        return self._iterations

    def _increase_iteration(self):
        self._iterations += 1


    def find_extremum(self, fn, interval, min, eps = 1e-7):
        a = interval.get_start
        b = interval.get_end

        lambda1 = a + (1 - self._tau) * (b - a)
        m1 = a + self._tau * (b - a)

        if Derative(fn, a)() > 0 and Derative(fn, b)() > 0:
            print("No extremum!")
            return

        while abs(b - a) / 2 > eps:
            self._increase_iteration()
            if (fn(lambda1) > fn(m1) and min)\
                    or (fn(m1) > fn(lambda1) and not min):
                a = lambda1
                lambda1 = m1
                m1 = a + self._tau * (b - a)
            else:
                b = m1
                m1 = lambda1
                lambda1 = a + (1 - self._tau) * (b - a)

        point = round((a + b) / 2, 2)
        print("GS:")
        if min:
            print(Min(point, round(fn(point), 2)))
        else:
            print(Max(point, round(fn(point), 2)))



