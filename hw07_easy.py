# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

from random import randint

class Triangle:
    def __init__(self, crds=[]):
        self.crds = ([[randint(0,10), randint(0,10)] for _ in range(3)] if not crds else crds)

    def side(self):
        """Определение длин сторон"""
        side_1 = ((self.crds[0][0] - self.crds[1][0]) ** 2 + (self.crds[0][1] - self.crds[1][1]) ** 2) ** 0.5
        side_2 = ((self.crds[2][0] - self.crds[1][0]) ** 2 + (self.crds[2][1] - self.crds[1][1]) ** 2) ** 0.5
        side_3 = ((self.crds[0][0] - self.crds[2][0]) ** 2 + (self.crds[0][1] - self.crds[2][1]) ** 2) ** 0.5
        sides = [side_1, side_2, side_3]
        #print(sides)
        return sides
        
    def prm(self):
        """Определение периметра"""
        prm = sum(self.side())
        return prm
        #print(f"{prm:.2f}")

    def sq(self):
        """Определение площади"""
        pprm = self.prm() / 2
        psides = self.side()
        sq = (pprm * (pprm - psides[0]) * (pprm - psides[1]) * (pprm - psides[2])) ** 0.5
        #print(sq)
        return sq
        
    def hg(self):
        """Определение наибольшей высоты"""
        psides = self.side()
        psq = self.sq()
        hgs = max([psq / psides[i] * 2 for i in range(3)])
        #print(hgs)
        return hgs

    def tri_main_prm(self):
        """Печать основных параметров"""
        print(f"\nКоординаты треугольника: {self.crds[:]} \nПлощадь: {self.sq():.2f} \nПериметр: {self.prm():.2f} \nМаксимальная высота: {self.hg():.2f} ")
    
        
if __name__ == "__main__":

    tri_1 = Triangle()
    tri_2 = Triangle([[0, 0], [3, 4], [1, 1]])
    
    tri_1.tri_main_prm()
    tri_2.tri_main_prm()

    
# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.


class RTrapecia:
    def __init__(self, crds=[]):
        self.crds = ([[randint(0,5), randint(0,5)] for _ in range(4)] if not crds else crds)
            
    def side(self):
        """Определение длин сторон"""
        side_1 = ((self.crds[0][0] - self.crds[1][0]) ** 2 + (self.crds[0][1] - self.crds[1][1]) ** 2) ** 0.5
        side_2 = ((self.crds[1][0] - self.crds[2][0]) ** 2 + (self.crds[1][1] - self.crds[2][1]) ** 2) ** 0.5
        side_3 = ((self.crds[2][0] - self.crds[3][0]) ** 2 + (self.crds[2][1] - self.crds[3][1]) ** 2) ** 0.5
        side_4 = ((self.crds[3][0] - self.crds[0][0]) ** 2 + (self.crds[3][1] - self.crds[0][1]) ** 2) ** 0.5
        sides = [side_1, side_2, side_3, side_4]
        #print(sides)
        return sides
        

    def vld_rtrc(self):
        """Определение являетс ли фигура с заданными координатами равнобедренной трапецией"""
        sides  = self.side()
        diag_ac = ((self.crds[0][0] - self.crds[2][0]) ** 2 + (self.crds[0][1] - self.crds[2][1]) ** 2) ** 0.5
        diag_bd = ((self.crds[1][0] - self.crds[3][0]) ** 2 + (self.crds[1][1] - self.crds[3][1]) ** 2) ** 0.5

        while sides[0] != sides[2] or diag_ac != diag_bd:
            print(self.crds[:], "трапеция не является равнобедренной. загружаем новые координаты")
            trc_new = RTrapecia()
            trc_1 = trc_new
            return trc_new.vld_rtrc()
        #print(diag_ac, diag_bd)
        self.trc_main_prm()

  
    def prm(self):
        """Определение периметра"""
        prm = sum(self.side())
        return prm
        #print(f"{prm:.2f}")

    def sq(self):
        """Определение площади"""
        ss = self.side()
        sq = (ss[1] + ss[3]) * (4 * ss[0] ** 2 - (ss[1] - ss[3]) ** 2) ** 0.5 / 4
        #print(sq)
        return sq

    def trc_main_prm(self):
        """Печать основных параметров"""
        print(f"\nКоординаты равнобедренной трапеции: {self.crds} \nДлины сторон: {self.side()} \nПлощадь: {self.sq():.2f} \nПериметр: {self.prm():.2f} ")


trc_1 = RTrapecia()
trc_2 = RTrapecia([[0, 0], [-1, -4], [5, -4], [4, 0]])

    
trc_1.vld_rtrc()
trc_2.vld_rtrc()
