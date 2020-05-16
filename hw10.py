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
    pass    

class Products(Shop):
    #__slots__ = ("self", "p_id", "p_name", "p_price", "p_val", "p_country", "p_date")
    def __init__(self, p_id, p_name, p_price, p_val):
        self.p_id = p_id
        self.p_name = p_name
        self.p_price = p_price
        self.p_val = p_val

    def info(self):
        print(f"\nID: {self.p_id:>5}  Наименование: {self.p_name:>10}  Цена: {self.p_price:>5}")

    @property
    def val(self):
        return self.p_val

    @val.setter
    def val(self, val):
        self.p_val = val

    def date_exp(self, date_exp):
        print(f"Товар {self.p_name} годен")
    
class FruitProduct(Products):
    def __init__(self, p_id, p_name, p_price, p_val, p_country, p_date):
        super().__init__(p_id, p_name, p_price, p_val)
        self.p_country = p_country
        self.p_date = p_date

    def date_exp(self, date_exp):
        if datetime.strptime(date_exp, "%d/%m/%Y") > datetime.strptime(self.p_date, "%d/%m/%Y"):
            print(f"Товар {self.p_name} годен")
        else:
            print(f"Товар {self.p_name} просрочен срок годности истек {self.p_date}")
    
        

def mag():
    f1 = Products(400, "Макароны", 150, 40)
    f2 = Products(410, "Мука", 50, 10)
    fp1 = FruitProduct(401, "Ананасы", 200, 110, "Ямайка", "12/10/2021")
    fp2 = FruitProduct(405, "Апельсины", 100, 20, "Польша", "12/10/2020")

    mag_ast = [f1, f2, fp1, fp2]
    for p in mag_ast:
        p.info()
        p.date_exp("31/12/2020")
        p_new = input(f"Остаток товара на данный момент: {p.val}, введите новое значение если хотите отредактировать: ")
        if p_new:
            p.val = p_new
            print(f"Актуальный остаток товара: {p.val}")

if __name__ == "__main__":
    mag()
