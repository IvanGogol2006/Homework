class House:
    def __init__(self, name, numbers_of_floors):
        self.name = name
        self.numbers_of_floors = numbers_of_floors

    def go_to(self, new_floor, numbers_of_floor=None):
        if new_floor <= 0:
            print('Такого этажа не существует')
        for i in range(new_floor):
            if new_floor > self.numbers_of_floors:
                print('Такого этажа не существует')
                break
            print(i + 1)


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
h3 = House('House3', 14)
h3.go_to(-1)