class MainFlowers:
    def __init__(self, freshness, color, stem_length, price, life_time):
        self.freshness = freshness
        self.color = color
        self.stem_length = stem_length
        self.__price = price
        self.__life_time = life_time

    @property
    def price(self):
        return self.__price

    @property
    def life_time(self):
        return self.__life_time

    def __repr__(self):
        return (f"{self.__class__.__name__}(цвет={self.color}, свежесть={self.freshness}, "
                f"длина стебля={self.stem_length}см, цена={self.price}, жизнь={self.life_time} дней)")


class Rose(MainFlowers):
    def __init__(self, freshness, color, stem_length):
        super().__init__(freshness, color, stem_length, price=250, life_time=10)


class Tulip(MainFlowers):
    def __init__(self, freshness, color, stem_length):
        super().__init__(freshness, color, stem_length, price=300, life_time=5)


class Daisy(MainFlowers):
    def __init__(self, freshness, color, stem_length):
        super().__init__(freshness, color, stem_length, price=50, life_time=3)


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def total_price(self):
        return sum(flower.price for flower in self.flowers)

    def get_average_life_time(self):
        if not self.flowers:
            return 0
        return sum(flower.life_time for flower in self.flowers) / len(self.flowers)

    def sort_by(self, param):
        self.flowers.sort(key=lambda flower: getattr(flower, param))

    def find_by(self, **kwargs):
        result = self.flowers
        for key, value in kwargs.items():
            result = [flower for flower in result if getattr(flower, key) == value]
        return result

    def __repr__(self):
        return f"Bouquet({self.flowers})"


rose = Rose(8, 'Красный', 50)
tulip = Tulip(7, 'Желтый', 40)
daisy = Daisy(9, 'Белый', 20)

bouquet = Bouquet()
bouquet.add_flower(rose)
bouquet.add_flower(tulip)
bouquet.add_flower(daisy)

print('Общая стоимость:', bouquet.total_price())
print('Среднее время увядания:', bouquet.get_average_life_time())

bouquet.sort_by('stem_length')
print('Букет отсортирован по длине стебля:')
print(bouquet)

white_flowers = bouquet.find_by(color='Белый')
print('Поиск цветов по цвету "Белый":')
print(white_flowers)
