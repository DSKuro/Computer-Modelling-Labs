class Function:
    def __init__(self, func):
        self.func = func

    def _call_func(self, value):
        return self.func(value)

    def __call__(self, value):
        return self._call_func(value)