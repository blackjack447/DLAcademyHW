# Предметная область – магазин. Разработать класс Shop,
# описывающий работу магазина продуктов. Разработать класс Products,
# продукт описывается следующими параметрами: уникальный идентификатор,
# название продукта, стоимость, количество. Разработать класс FruitProduct
# на базе класс Product, фрукт характеризуется параметрами:
# страна изготовителя, срок годности.
class Products:
    def __init__(self, id_item, name, cost, quantity):
        self.id = id_item
        self.name = name
        self.cost = cost
        self.quantity = quantity


class FruitProduct(Products):
    def __init__(self, id_item, name, cost, quantity, country, expiration_date):
        self.country = country
        self.expiration_date = expiration_date
        super().__init__(id_item, name, cost, quantity)


class Shop:
    def __init__(self, name, adress, product_lst):
        self.name = name
        self.adress = adress
        self.product_lst = product_lst
        
    @property
    def get_shop_name(self):
        return self.name

    @property
    def get_shop_adress(self):
        return self.adress


if __name__ == '__main__':
    fruits = [FruitProduct('11970012', 'Апельсины', 350, 30, 'Морокко', 30),
              FruitProduct('10151078', 'Бананы', 150, 98, 'Бразилия', 25),
              FruitProduct('14872056', 'Персики', 450, 75, 'Абхазия', 60)]

    shop = Shop('"У Ашотика"', 'ул.Шашлычная,д.5', fruits)

    magazin_name = shop.get_shop_name
    magazin_adress = shop.get_shop_adress
    print(f'Вас приветствует магазин {magazin_name}, мы располагаемся по адресу: {magazin_adress}')

    for i in shop.product_lst:
        print(f'В продаже есть {i.name} цене {i.cost} за кг. в кол-ве {i.quantity} кг.')

    h = str(input('Что хотите купить? - '))
    for i in shop.product_lst:
        if i.name == h:
            i.quantity -= 1
            print(f'Спасибо за покупку, вот Ваши {i.name}')
            for i in shop.product_lst:
                print(f'В продаже остались {i.name} цене {i.cost} за кг. в кол-ве {i.quantity} кг.')

    a = FruitProduct('11082054', 'Финики', 100, 15, 'Египет', 100)
    b = fruits.append(a)
    c = FruitProduct('11111111', 'Хурма', 35, 10, 'Подстепки', 8)
    d = fruits.append(c)

    k = 10
    for i in shop.product_lst:
        if i.expiration_date < k:
            print(f'Срок хранения товара {i.name} подходит к концу')