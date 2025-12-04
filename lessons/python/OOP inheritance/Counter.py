def is_int(method):
    def wrapper(self, value):
        if not isinstance(value, int):
            return NotImplemented
        return method(self, value)
    return wrapper

class Counter():
    def __init__(self, start=0):
        self.value = start

    @is_int
    def inc(self, value = 1):
        self.value += value

    @is_int
    def dec(self, value = 1):
        self.value -= value
        if self.value < 0: self.value = 0