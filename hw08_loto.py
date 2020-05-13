
#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""
import random

class Player():
    
    def __init__(self, name, type_player="pc", card_w=5, card_h=3):
        self.name = name
        self.type = type_player
        self.card_w = card_w
        self.card_h = card_h
        self.score = 0
        self.player_card = self.Card_init()
        self.result = ""

    def Card_init(self):
        """Генерация карточки"""
        card_list = [sorted([random.randint(1,900) for i in range(self.card_w)]) for _ in range(self.card_h)]
        #print(card_list)
        return card_list if len(set(card_list[0] + card_list[1] + card_list[2])) == 15 else self.Card_init()
    
    def info(self):
        """Инфо"""
        return (f"\nКарточка игрока {self.name}\n {self.player_card[0]}\n {self.player_card[1]}\n {self.player_card[2]}\n")

    def game(self, inp_bch):
        """Действия игрока"""
        bch_bool = self.search_bch(inp_bch)
        if self.type == "user":
            inp_ans = ""
            while inp_ans != "y" and  inp_ans !="n":
                inp_ans = input(f"Зачеркнуть цифру {inp_bch}? (y/n)")
            if (inp_ans == "y" and bch_bool == False) or (inp_ans == "n" and bch_bool == True):
                self.result = f"Игрок {self.name} будте в следующий раз внимательнее, вы проиграли"         
        return self.result
        
    def search_bch(self, inp_bch):
        """Опреации с картой и подсчет вычеркнутых цифер"""
        for i, n in enumerate(self.player_card):
            if inp_bch in n:
                self.player_card[i][n.index(inp_bch)] = "X"
                self.score += 1
                if self.score == 15:
                    self.result = f"ПОЗДРАВЛЯЕМ! \nВыиграл {self.name}\n"
                return True
        return False
    
class Bch:
    def __init__(self, num_bch):
        self.num_bch = num_bch
        self.bch_list = [i for i in range(1, self.num_bch + 1)]
        random.shuffle(self.bch_list)

    def bl(self):
        return self.bch_list

        
def main(player1, player2):
    """Генерация игры в лото с ключевыми параметрами"""
    bch = Bch(90)
    result_loto= ""
    n = 0
    while result_loto == "" and (len(bch.bl()) - n) != 0:
        print(f"\nВыпал боченок: {bch.bl()[n]} (осталось {len(bch.bl()) - n - 1})\n{player1.info()}{player2.info()}")
        result_loto = player1.game(bch.bl()[n]) + player2.game(bch.bl()[n])
        n += 1
    print(result_loto if result_loto else "В игре ничья")
        
if __name__ == "__main__":
    main(Player("Мегакомп"),Player("Дипблю"))
    main(Player("Иван", "user"),Player("Мак"))









