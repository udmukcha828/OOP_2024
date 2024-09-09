import random

class Mother:
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return f"Я мама, зовут {self._name}"

class Daughter(Mother):
    def __init__(self, name, age):
        super().__init__(name)
        self._age = age

    def __str__(self):
        return f"Я дочь, зовут {self._name}, мне {self._age} лет"

# Создаем объекты
mother = Mother("Анна")
daughter = Daughter("Мария", 20)

# Список имен для рандомного выбора
names = ["Екатерина", "Ольга", "Ирина", "Светлана", "Татьяна"]

# Выбираем случайные имена из списка
mother._name = random.choice(names)
daughter._name = random.choice(names)

# Выводим информацию об объектах
print(mother)
print(daughter)
