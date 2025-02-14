import matplotlib.pyplot as plt

class Graphic:
    def __init__(self, func, interval, step):
        self.func = func
        self.interval = interval
        self.step = step

    def create(self):
        xs = []
        for i in range(self.interval.get_start, self.interval.get_end + 1, self.step):
            xs.append(i)

        ys = []
        for i in range(self.interval.get_start, self.interval.get_end + 1, self.step):
            ys.append(self.func(i))

        plt.plot(xs, ys)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title(f"График функции")
        plt.grid()
        plt.show()
