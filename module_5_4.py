class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)

    def __init__(self, name, numbers_of_floors):
        self.name = name
        self.numbers_of_floors = numbers_of_floors
        House.houses_history.append(self.name)

    def __str__(self):
        return (f'Название {self.name}, кол-во этажей: {self.numbers_of_floors}')

    def __repr__(self):
        return House.houses_history

    def __del__(self):
        return print(f'{self.name} cнесён, но он останется в истории')


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)

h2 = House('ЖК Акация', 20)
print(House.houses_history)

h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)