# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


class School:
    def __init__(self, name):
        self.name = name
        
    def fio(self):
        fio = f"{self.name[0]} {self.name[1][:1]}.{self.name[2][:1]}."
        return fio

        
class Teacher(School):
    def __init__(self, name, teach_pr):
        super().__init__(name)
        self.pr = teach_pr

    def t_cls(self):
        return(self.pr)
    
            
class Student(School):
    def __init__(self, name, study_classes, cls, parents):
        super().__init__(name)
        self.predmet = study_classes
        self.cls = cls
        self.parents = parents

    
    def st_cls(self):
        return(self.cls)

    def st_predmet(self):
        print(f"\nУченик: {self.fio()}\
                \nКласс: {self.cls}\
                \nУчителя: {', '.join(t.fio() for t in teachers if t.t_cls() in self.predmet)}\
                \nПредметы: {', '.join(self.predmet)}")

    def st_predmet_resive(self):
        return(self.predmet)
    
    def st_parents(self):
        return (', '.join(self.parents))
        

#if __name__ == "__main__":
    
    
    
teachers = [Teacher(["Жиров", "Иван", "Иванович"], "Алгебра"),
            Teacher(["Козлов", "Иван", "Иванович"], "Музыка"),
            Teacher(["Иванов", "Иван", "Иванович"], "Физра"),
            Teacher(["Тор", "Иван", "Иванович"], "Физика")
            ]

students = [Student(["Иванов", "Иван", "Иванович"], ["Алгебра", "Физика", "Музыка"], "5A",  ["Иванов Иван", "Иванова Гала"]),
            Student(["Петров", "Илья", "Иванович"], ["Рисование", "Физра", "Музыка"], "5A",  ["Петрова Галина"]),
            Student(["Яковлев", "Илья", "Иванович"], ["Физика", "Физра", "Музыка"], "3Б",  ["Яковлев Гена, Яковлева Галина"]),
            Student(["Тормунд", "Илья", "Иванович"], ["Музыка"], "1Г",  ["Тормунд Галина"])
            ]
            

opr = 0
class_list = sorted(list(set([students[i].st_cls() for i in range(len(students))])))
    
#print(teachers[1].teacher_for_predmet("Музыка"))

while opr != 6:
    opr = int(input("\nВыберите задачу:\
                  \n1. Получить полный список всех классов школы\
                  \n2. Получить список всех учеников в классе\
                  \n3. Получить список всех предметов указанного ученика\
                  \n4. Узнать ФИО родителей указанного ученика\
                  \n5. Получить список всех Учителей, преподающих в указанном классе\
                  \n6. Выйти\n"))

    if opr == 1:
        print(f"Полный список всех классов школы: {', '.join(class_list)}")
    
    if opr == 2:
        for class_num in class_list:
            print(f"\nСписок учеников класса {class_num}:")
            for stdnt in students:
                if stdnt.st_cls() == class_num:
                    print(stdnt.fio())

    if opr == 3:
        for stdnt in students:
            stdnt.st_predmet()    
        
    if opr == 4:
        for i in range(len(students)):
            print(f"Родители ученика {students[i].fio()}: {students[i].st_parents()}")

    if opr == 5:
        for class_num in class_list:
            class_predmet_list = []
            for stdnt in students:
                if stdnt.st_cls() == class_num:
                    class_predmet_list += stdnt.st_predmet_resive()
            tcls_list = [t.fio() for t in teachers if t.t_cls() in list(set(class_predmet_list))]
            print(f"Преподователи класса {class_num}: {', '.join(tcls_list)}")
                    
                    
