class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Triangle(Shape):
    def area(self):
        return 0.5 * self.width * self.height

class Rectangle(Shape):
    def area(self):
        return self.width * self.height

# Проверка работоспособности
triangle = Triangle(3, 8)
rectangle = Rectangle(3, 8)

print(f"Площадь треугольника: {triangle.area()}")
print(f"Площадь прямоугольника: {rectangle.area()}")
