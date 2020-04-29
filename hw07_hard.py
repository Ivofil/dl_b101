# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла


class Workers:
    def __init__(self, name, surname, oklad, position, norma_time):
        self.name = name 
        self.surname = surname
        self._ok = int(oklad)
        self.position = position
        self.nt = int(norma_time)
        self.wt = 0

    def read_wt(self):
        with open("data/hours_of.txt", "r", encoding="UTF-8") as f:
            for i in f.readlines():
                if i.split()[0] == self.name and i.split()[1] == self.surname:
                    self.wt = int(i.split()[2])
                    break
                else:
                    continue
                
    def write_zp(self, zp):
        with open("data/zp.txt", "a", encoding="UTF-8") as f:
            #print(f"{self.name} {self.surname} {zp:.2f} {self.position}")
            f.write(f"{self.name} {self.surname} {zp:.2f} {self.position}")
            f.write("\n")

    def calc_zp(self):
        if self.wt > self.nt:
            zp = self._ok + 2 * self._ok * (self.wt / self.nt - 1)
        else:
            zp = self._ok * self.wt / self.nt
        return zp       
    

def zp_raschet(file):
    f = open(file, "r", encoding="UTF-8")
    for i in f.readlines():
        if i.count("Имя") == 1:
            continue
        else:
            name, surname, oklad, position, norma_time = i.split()
            Company = Workers(name, surname, oklad, position, norma_time)
            Company.read_wt()
            Company.write_zp(Company.calc_zp())
    f.close()
 
 
zp_raschet("data/workers.txt")




