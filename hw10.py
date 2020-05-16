"""
Предметная область – магазин. Разработать класс Shop, 
описывающий работу магазина продуктов. Разработать класс 
Products, продукт описывается следующими параметрами: 
уникальный идентификатор, название продукта, стоимость, 
количество. Разработать класс FruitProduct на базе класс Product, 
фрукт характеризуется параметрами: страна изготовителя, срок 
годности.
"""
from datetime import datetime

class Shop():
    def __init__(self, shop_name, num_p):
        self.shop_name = shop_name
        self.num_p = num_p
        self.mag = []
        
    def addP(self, *addp):
        for ap in addp:
            self.mag.append(ap) if len(self.mag) < self.num_p else print(f"Товар не добавлен, ассортимент магазина ограничен {self.num_p} позициями")

    def ast_bestbefore(self, date):
        print(f"\nАссортимент свежих товаров магазина {self.shop_name}")
        for pr in self.mag:
            pr.date_exp(date)

    @property
    def assortiment(self):
        print(f"\nАссортимент магазина {self.shop_name}" if self.mag else f"Магазин пуст") 
        for pr in self.mag:
            pr.info()
    @property
    def del_assortiment(self):
        self.mag = []
        print(f"\nАссортимент магазина очищен")

    @property
    def edit_val_assortiment(self):
        print(f"\nОстатки товаров магазина {self.shop_name}" if self.mag else f"Магазин пуст") 
        for pr in self.mag:
            pr.info()
            p_new = input(f"Остаток товара на данный момент: {pr.val}\nВведите новое значение если хотите отредактировать: ")
            if p_new:
                pr.val = int(p_new)
                print(f"Актуальный остаток товара: {pr.val}")

    
class Products(Shop):
    #__slots__ = ("self", "p_id", "p_name", "p_price", "p_val", "p_country", "p_date")
    def __init__(self, p_id, p_name, p_price, p_val):
        self.p_type = "Хоз. товары"
        self.p_id = p_id
        self.p_name = p_name
        self.p_price = p_price
        self.p_val = p_val

    def info(self):
        print(f"ID: {self.p_id:>4}  Товар: {self.p_name:>10}  Категория: {self.p_type:>15}  Цена: {self.p_price:>5}")

    @property
    def val(self):
        return self.p_val

    @val.setter
    def val(self, val):
        self.p_val = val

    def date_exp(self, date_exp):
        print(f"Товар {self.p_name:15} без срока хранения")
    
class FruitProduct(Products):
    def __init__(self, p_id, p_name, p_price, p_val, p_country, p_date):
        super().__init__(p_id, p_name, p_price, p_val)
        self.p_type = "Фрукты"
        self.p_country = p_country
        self.p_date = p_date

    def date_exp(self, date_exp):
        if datetime.strptime(date_exp, "%d/%m/%Y") > datetime.strptime(self.p_date, "%d/%m/%Y"):
            print(f"Товар {self.p_name:15} годен")
        else:
            print(f"Товар {self.p_name:15} просрочен срок годности истек {self.p_date}")
    
        

def mag():
    s = Shop("Пятерочка", 4)
    f1 = Products(400, "Кастрюля", 1500, 40)
    f2 = Products(410, "Банка", 50, 10)
    fp1 = FruitProduct(401, "Ананасы", 200, 110, "Ямайка", "12/10/2021")
    fp2 = FruitProduct(405, "Апельсины", 100, 20, "Польша", "12/10/2020")
    f3 = Products(490, "Нож", 50, 10)
    
    s.addP(f1)
    s.addP(f2, fp1, fp2, f3)
    s.assortiment
    s.ast_bestbefore("31/12/2020")
    s.edit_val_assortiment
    s.del_assortiment
    s.assortiment


if __name__ == "__main__":
    mag()
