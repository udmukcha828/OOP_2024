class Animal:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_description(self):
        return f"Имя: {self._name}, Возраст: {self._age}"

class Zebra(Animal):
    def get_description(self):
        return f"{super().get_description()}, Вид: Зебра"

class Dolphin(Animal):
    def get_description(self):
        return f"{super().get_description()}, Вид: Дельфин"

# Создаем объекты
zebra = Zebra("Зевс", 3)
dolphin = Dolphin("Дельфи", 8)

# Выводим описание
print(zebra.get_description())
print(dolphin.get_description())
