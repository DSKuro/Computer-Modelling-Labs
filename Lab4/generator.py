import math

class TrigonomicOperations:
    def __init__(self, n, initial):
        self.x = initial
        self.n = n
        self._valid_parameters()

    def _valid_parameters(self):
        if self.x >= 1:
            raise ValueError("x0 >= 1 !")

    def next(self):
        self.x = (1 / math.pi) * math.acos(math.cos(10 ** self.n * self.x))
        return self.x

class Generator:
    def __init__(self, oper):
        self.oper = oper

    def generate(self, n):
        if n <= 0:
            raise ValueError("Size must be greater zero")

        values = []
        for _ in range(n):
            values.append(self.oper.next())
        return values

if __name__ == "__main__":
    oper = TrigonomicOperations(10, -1)
    generator = Generator(oper)
    print(generator.generate(5))