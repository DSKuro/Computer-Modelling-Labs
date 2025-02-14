from Lab3.classes.Extremum import Max
from Lab3.classes.Extremum import Min
from Lab3.classes.Extremum import Derative

class Chord:
    _iterations = 0

    @property
    def get_iterations(self):
        return self._iterations

    def _increase_iteration(self):
        self._iterations += 1


    def find_extremum(self, fn, interval, eps = 1e-7):
        a = interval.get_start
        b = interval.get_end
        x0 = a
        x1 = b

        if Derative(fn, a)() > 0 and Derative(fn, b)() > 0:
            print("No extremum!")
            return

        while abs(x1 - x0) > eps:
            self._increase_iteration()
            x0 = x1
            x1 = a - (Derative(fn, a)() * (b - a)) / (Derative(fn, b)() - Derative(fn, a) ())
            fx1 = fn(x1)
            if fx1 == 0:
                print("CH:")
                if Derative(fn, x1 + eps, False)() > 0:
                    print(Min(x1, fn(x1)))
                else:
                    print(Max(x1, fn(x1)))
                break

            if fx1 * Derative(fn, b)() > 0:
                b = x1
            else:
                a = x1


