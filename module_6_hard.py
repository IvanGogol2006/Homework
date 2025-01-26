import math

class Figure:
    sides_count = 0

    def __init__(self, color=(0, 0, 0), *args):
        # Проверка количества сторон при создании объекта
        if len(args) == self.sides_count:
            self._sides = args
        else:
            self._sides = [1] * self.sides_count

        self.color = color
        self.filled = False

    @property
    def sides(self):
        return self._sides

    def get_color(self):
        return self.color

    def _is_valid_color(self, r, g, b):
        if not isinstance(r, int) or not isinstance(g, int) or not isinstance(b, int):
            return False
        if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
            return False
        return True

    def set_color(self, r, g, b):
        if self._is_valid_color(r, g, b):
            self.color = (r, g, b)

    def _is_valid_sides(self, new_sides):
        if len(new_sides) != self.sides_count:
            return False
        for side in new_sides:
            if not isinstance(side, int) or side <= 0:
                return False
        return True

    def get_sides(self):
        return self.sides

    def __len__(self):
        return sum(self.sides)

    def set_sides(self, *new_sides):
        if self._is_valid_sides(new_sides):
            self._sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color=(0, 0, 0), radius=1):
        super().__init__(color, radius)
        self.radius = radius

    @property
    def radius(self):
        return self._sides[0] / (2 * math.pi)

    @radius.setter
    def radius(self, value):
        if value > 0:
            self._sides = [2 * math.pi * value]

    def get_square(self):
        return math.pi * self.radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color=(0, 0, 0), *args):
        super().__init__(color, *args)

    def get_square(self):
        a, b, c = self.sides
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return area


class Cube(Figure):
    sides_count = 12

    def __init__(self, color=(0, 0, 0), edge_length=1):
        super().__init__(color, *([edge_length] * self.sides_count))

    @property
    def edge_length(self):
        return self._sides[0]

    @edge_length.setter
    def edge_length(self, value):
        if value > 0:
            self._sides = [value] * self.sides_count

    def get_volume(self):
        return self.edge_length ** 3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())