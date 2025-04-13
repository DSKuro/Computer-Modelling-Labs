class FunctionsSystem:
    def __init__(self, functions):
        self.functions = functions
        self.a = 0
        self.b = 0
        self.c = 0

    def set_params(self, a, b, c):
        self.a = a
        self.b = c
        self.c = c

    def execute(self, eq, t):
        x, y, z = eq
        return [self.functions[0](x, y, z),
                self.functions[1](x, y, z),
                self.functions[2](x, y, z)]

