class Function:
    def __init__(self, func):
        self.func = func

    def _call_func(self, *args):
        return self.func(*args)

    def __call__(self, *args):
        return self._call_func(*args)
