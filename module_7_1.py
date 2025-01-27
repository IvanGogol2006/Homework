class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        try:
            with open(self.__file_name, 'r') as file:
                content = file.read()
        except FileNotFoundError:
            # Файл еще не существует, возвращаем пустую строку
            content = ''

        return content.strip().split('\n')

    def add(self, *products):
        existing_products = self.get_products()
        product_dict = {}

        for product in existing_products:
            if product:
                name, weight, category = product.split(', ')
                product_dict[(name, category)] = float(weight)

        for product in products:
            key = (product.name, product.category)
            if key not in product_dict:
                product_dict[key] = product.weight
            else:
                product_dict[key] += product.weight
                print(f'Продукт {product.name} уже был в магазине, его общий вес теперь равен {product_dict[key]}')

        with open(self.__file_name, 'w') as file:
            for (name, category), weight in product_dict.items():
                file.write(f'{name}, {weight}, {category}\n')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

s1.add(p1, p2, p3)

print(s1.get_products())
