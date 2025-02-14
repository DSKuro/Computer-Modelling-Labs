import numpy as np

class Interval:
    def __init__(self, start, end):
        self._start = start
        self._end = end

    @property
    def get_start(self):
        return self._start

    @property
    def get_end(self):
        return self._end

class Extremum:
    def __init__(self, x, value):
        self.x = x
        self.value = value

    def __str__(self):
        return f"Extremum at x = { self. x }, value = { self.value }"

class Min(Extremum):
    def __str__(self):
        return f"Minimum at x = { self.x }, value = { self.value }"

class Max(Extremum):
    def __str__(self):
        return f"Max at x = {self.x}, value = {self.value}"

# f(x+h) - f(x) / h
class Derative():
    def __init__(self, func, value, round = True, h = 1e-7):
        self.func = func
        self.value = value
        self.h = h
        self.round = round

    def __call__(self):
        x = ((self.func(self.value + self.h) - self.func(self.value - self.h))
                / (2 * self.h))
        if self.round:
            return round(x, 2)
        else:
            return x

class IntervalSearch():
    def __init__(self, fn, step, interval):
        self.fn = fn
        self.interval = interval
        self.step = step

    def find_extremum_intervals(self):
        x_values = np.arange(self.interval.get_start, self.interval.get_end, self.step)
        new_intervals = []

        for x in x_values:
            derivative = Derative(self.fn, x)()
            root = self.find_root(derivative, x)
            if root is not None:
                new_intervals.append(Interval(root - self.step, root + self.step))

        return new_intervals

    def find_root(self, derivative, x, tolerance = 1e-7, max_iterations = 1000):
        second_derivative = Derative(self.fn, derivative)()
        for _ in range(max_iterations):
            if abs(derivative) < tolerance:
                return x
            if second_derivative == 0:
                return None
            x -= derivative / second_derivative
        return None