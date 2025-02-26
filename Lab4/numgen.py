import numpy as np

class GammaGenerator:
    def __init__(self, shape, scale = 1):
        if shape < 0:
            raise ValueError("shape >= 0!")

        if scale < 0:
            raise ValueError("scale >= 0!")

        self.shape = shape
        self.scale = scale


    def generate(self, size):
        if size <= 0:
            raise ValueError("size >= 0!")

        return np.random.gamma(self.shape, self.scale, size)

if __name__ == "__main__":
    gg = GammaGenerator(3)
    print(gg.generate(20))