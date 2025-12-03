def check_type(method):
        def wrapper(self, other):
            if not isinstance(other, FoodInfo):
                return NotImplemented
            return method(self, other)
        return wrapper

def is_int_or_float(method):
    def wrapper(self, other):
        if not isinstance(other, (int, float)):
            return NotImplemented
        return method(self, other)
    return wrapper

class FoodInfo():
    def __init__(self, proteins, fats, carbohydrates):
        self.proteins = proteins
        self.fats = fats
        self.carbohydrates = carbohydrates

    def __repr__(self):
        return f"FoodInfo({self.proteins}, {self.fats}, {self.carbohydrates})"

    @check_type    
    def __add__(self, other_food):
        return FoodInfo(self.proteins + other_food.proteins, self.fats + other_food.fats, self.carbohydrates + other_food.carbohydrates)
    
    @check_type
    def __sub__(self, other_food):
        return FoodInfo(self.proteins - other_food.proteins, self.fats - other_food.fats, self.carbohydrates - other_food.carbohydrates)
    
    @is_int_or_float
    def __mul__(self, n):
        return FoodInfo(self.proteins * n, self.fats * n, self.carbohydrates * n)

    @is_int_or_float
    def __truediv__(self, n):
        return FoodInfo(self.proteins / n, self.fats / n, self.carbohydrates / n)
    
    @is_int_or_float
    def __floordiv__(self, n):
        return FoodInfo(self.proteins // n, self.fats // n, self.carbohydrates // n)