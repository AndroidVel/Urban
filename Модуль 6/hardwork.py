from math import pi, sqrt


class Figure:
    sides_count = 0

    def __init__(self, colors, sides):
        self.__color = colors
        self.filled = None
        if not isinstance(sides, int):
            if self.sides_count == len(sides):
                self.__sides = sides
            else:
                self.__sides = [1] * self.sides_count
        else:
            self.__sides = [sides]

    def get_color(self):
        return self.__color

    @staticmethod
    def __is_valid_color(r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, args):
        if len(args) == self.sides_count:
            bool_ = True
            for i in args:
                if not isinstance(i, int):
                    bool_ = False
                    break
                else:
                    bool_ = True
        else:
            bool_ = False
        return bool_

    def set_sides(self, *args):
        if self.__is_valid_sides(args):
            self.__sides = [i for i in args]

    def get_sides(self):
        return self.__sides

    def __len__(self):
        perimeter = 0
        for side in self.__sides:
            perimeter += side
        return perimeter


class Circle(Figure):
    sides_count = 1

    def __init__(self, colors, sides):
        super().__init__(colors, sides)
        self.__radius = sides / (2 * pi)

    def get_square(self):
        return pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, colors, sides):
        super().__init__(colors, sides)

    def get_square(self):
        p = sum((self._Figure__sides[0] + self._Figure__sides[1] + self._Figure__sides[2]) / 2)
        return sqrt(p * (p - self._Figure__sides[0]) * (p - self._Figure__sides[1]) * (p - self._Figure__sides[2]))


class Cube(Figure):
    sides_count = 12

    def __init__(self, colors, sides):
        super().__init__(colors, sides)
        self._Figure__sides = [sides] * 12

    def get_volume(self):
        return self._Figure__sides[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
cube1.set_color(300, 70, 15)  # Не изменится
print(circle1.get_color())
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
circle1.set_sides(15)  # Изменится
print(cube1.get_sides())
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
