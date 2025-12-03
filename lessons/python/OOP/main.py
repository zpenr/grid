import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def length(self):
        return abs((self.y**2 + self.x**2)**0.5)

    def angle(self):
        angle = math.atan2(self.y, self.x)
        angle = math.degrees(angle)

        if angle < 0:
            return angle + 360
        return round(angle,2)

    def add(self, vector2):
        new_x = self.x + vector2.x
        new_y = self.y + vector2.y
        return Vector(new_x, new_y)

    def subtract(self, vector2):
        new_x = self.x - vector2.x
        new_y = self.y - vector2.y
        return Vector(new_x, new_y)

    def multiplication(self, vector2):
        return self.x * vector2.x + self.y * vector2.y

    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __add__(self, vector2):
        new_x = self.x + vector2.x
        new_y = self.y + vector2.y
        return Vector(new_x, new_y)

    def __sub__(self, vector2):
        new_x = self.x - vector2.x
        new_y = self.y - vector2.y
        return Vector(new_x, new_y)
    
    def __mul__(self, vector2):
        return self.x * vector2.x + self.y * vector2.y


v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(f"Длина вектора v1: {v1.length()}")

print(f"Угол вектора v1: {v1.angle()} градусов")

v_sum = v1 + (v2)
print(f"Сумма v1 + v2: {v_sum}")

v_sub = v1 - v2
print(f"v1 - v2: {v_sub}")

s = v1.multiplication(v2)
print(f"Скалярное произведение: {s}")