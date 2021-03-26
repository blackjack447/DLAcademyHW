# Предметная область – магазин. Разработать класс Shop,
# описывающий работу магазина продуктов. Разработать класс Products,
# продукт описывается следующими параметрами: уникальный идентификатор,
# название продукта, стоимость, количество. Разработать класс FruitProduct
# на базе класс Product, фрукт характеризуется параметрами:
# страна изготовителя, срок годности.
from datetime import date


class Product:
    def __init__(self, id_item, name, cost, quantity):
        self.id = id_item
        self.name = name
        self.cost = cost
        self.quantity = quantity


class FruitProduct(Product):
    def __init__(self, id_item, name, cost, quantity, country,
                 expiration_date):
        self.country = country
        self.expiration_date = expiration_date
        super().__init__(id_item, name, cost, quantity)


class Shop:
    def __init__(self, name, adress, product_lst):
        self.name = name
        self.adress = adress
        self.product_lst = product_lst

    @property
    def shop_name(self):
        return self.name

    @property
    def shop_adress(self):
        return self.adress

    def show_menu(self):
        print(
            f'Вас приветствует магазин {self.shop_name}, мы располагаемся по адресу: {self.shop_adress}, что желаете ?'
        )
        print('1. Купить', '2. Добавить товар', '3. Удалить товары, чей срок годности истек', '4. Выйти', sep='\n')

    def show_products(self):
        for i in self.product_lst:
            print(
                f'В продаже есть {i.name} цене {i.cost} за кг. в кол-ве {i.quantity} кг.'
            )

    def add_product(self, product):
        in_shop = False
        for i in self.product_lst:
            if i.id == product.id:
                in_shop = True
                print(
                    f'Товар {product.name} с таким id {product.id} уже есть у нас в магазине!'
                )
        if not in_shop:
            self.product_lst.append(product)
            print(f'Товар {product.name} -добавлен!')

    def del_product(self, product):
        try:
            self.product_lst.remove(product)
            print(f'Товар {product.name} - удален!')
        except ValueError:
            print(f'Такого товара {product.name} у нас в магазине нету. Удаление - невозможно')

    def check_date(self, product_date, today_date):
        p_year, p_month, p_day = map(int, product_date.split('.'))
        t_year, t_month, t_day = map(int, today_date.split('-'))
        if p_year < t_year:
            return False
        elif p_year == t_year and p_month < t_month:
            return False
        elif p_year == t_year and p_month == t_month and p_day < t_day:
            return False
        else:
            return True

    def del_expired_products(self, today_date):
        print('Проверка срока годности товара...')
        for i in self.product_lst:
            if not self.check_date(i.expiration_date, today_date):
                self.del_product(i)

    def buy_product(self):
        h = str(input('Что хотите купить? - '))
        for i in self.product_lst:
            if i.name == h:
                i.quantity -= 1
                print(f'Спасибо за покупку, вот Ваши {i.name}')
                for i in shop.product_lst:
                    print(
                        f'В продаже остались {i.name} цене {i.cost} за кг. в кол-ве {i.quantity} кг.'
                    )


if __name__ == '__main__':
    fruits = [
        FruitProduct('11970012', 'Апельсины', 350, 30, 'Морокко', '2007.12.30'),
        FruitProduct('10151078', 'Бананы', 150, 98, 'Бразилия', '2022.02.25'),
        FruitProduct('14872056', 'Персики', 450, 75, 'Абхазия', '2021.07.19')
    ]

    shop = Shop('"У Ашотика"', 'ул.Шашлычная,д.5', fruits)

    finish = False
    while not finish:
        shop.show_menu()
        action = int(input())
        if action == 1:
            shop.show_products()
            shop.buy_product()
        elif action == 2:
            id = str(input('Введите id товара:'))
            name = str(input('Введите название товара:'))
            cost = int(input('Введите стоимость:'))
            value = int(input('Введите кол-во:'))
            country = str(input('Введите страну происхождения:'))
            date = str(input('Введите срок годности (год, месяц,день):'))
            g = FruitProduct(id, name, cost, value, country, date)
            shop.add_product(g)
        elif action == 3:
            # pr_name = input('Введите название продукта - ')
            data = date.today()
            split_date = date.strftime(data, '%Y-%m-%d')
            shop.del_expired_products(split_date)
        elif action == 4:
            finish = True