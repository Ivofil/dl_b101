from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, mapper, relationship
from sqlalchemy.schema import ForeignKey

engine = create_engine('sqlite:///:memory:', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Sportsman(Base):
    __tablename__ = 'sportsman'
    sportsman_id = Column(Integer, primary_key=True)
    sportsman_name = Column(String)
    rank = Column(String)
    year_of_birth = Column(Integer)
    personal_record = Column(Integer)
    country = Column(String)

    def __init__(self, sportsman_id, sportsman_name, rank, year_of_birth,
                 personal_record, country):
        self.sportsman_id = sportsman_id
        self.sportsman_name = sportsman_name
        self.rank = rank
        self.year_of_birth = year_of_birth
        self.personal_record = personal_record
        self.country = country

class Competition(Base):
    __tablename__ = 'competition'
    competition_id = Column(Integer, primary_key=True)
    competition_name = Column(String)
    world_record = Column(Integer)
    set_date = Column(String)


    def __init__(self, competition_id, competition_name, world_record, set_date):
        self.competition_id = competition_id
        self.competition_name = competition_name
        self.world_record = world_record
        self.set_date = set_date

class Result(Base):
    __tablename__ = 'result'
    id = Column(Integer, primary_key=True)
    competition_id = Column(Integer, ForeignKey("competition.competition_id"))
    sportsman_id = Column(Integer, ForeignKey("sportsman.sportsman_id"))
    result = Column(Integer)
    city = Column(String)
    hold_date = Column(String)

    def __init__(self, competition_id, sportsman_id, result, city, hold_date):
        self.competition_id = competition_id
        self.sportsman_id = sportsman_id
        self.result = result
        self.city = city
        self.hold_date = hold_date

# Создание таблицы
Base.metadata.create_all(engine)

u1 = Sportsman(1001, "Петоров Иван", "КМС", 1990, 9, "Россия")
u2 = Sportsman(1002, "Иванов Иван", "МС", 1980, 19, "Россия")
u3 = Sportsman(2001, "Сидоров Иван", "КМС", 1990, 39, "Россия")
u4 = Sportsman(2002, "Ян Петр", "МС", 1990, 9, "Россия")
u5 = Sportsman(5001, "Джошуа Барнетт", "КМС", 1980, 19, "США")

session.add(u1)
session.add(u2)
session.add(u3)
session.add(u4)
session.add(u5)

c1 = Competition(1, "Бег 100м", 9, "12-05-2010")
c2 = Competition(2, "Бег 200м", 19, "11-05-2010")
c3 = Competition(3, "Бег 400м", 39, "15-05-2010")
c4 = Competition(100, "Плавание 50м", 10, "12-05-2020")
c5 = Competition(200, "Плавание 100м", 20, "11-05-2020")

session.add(c1)
session.add(c2)
session.add(c3)
session.add(c4)
session.add(c5)

r1 = Result(1, 1001, 10, "Москва", "12-05-2010")
r2 = Result(2, 1001, 20, "Вильнус", "15-05-2010")
r3 = Result(3, 1001, 10, "Москва", "13-05-2010")
r4 = Result(4, 1002, 11, "Чикаго", "12-05-2010")
r5 = Result(1, 5001, 12, "Самара", "15-05-2010")

session.add(r1)
session.add(r2)
session.add(r3)
session.add(r4)
session.add(r5)

session.commit()


print("\nВся информация по спортсменам")
for s in session.query(Sportsman):
    print(f" {s.sportsman_name}: {s.sportsman_name} разряд {s.rank} рекорд {s.personal_record}")

print("\nМировые рекордв по видам спорта")
for s in session.query(Competition):
    print(f" {s.competition_name}: мировой рекорд {s.world_record}, установлен {s.set_date}")

print("\nИмена всех спортсменов, которые родились в 1990 году. ")
for s in session.query(Sportsman).filter(Sportsman.year_of_birth==1990):
    print(f" Спортсмен {s.sportsman_name} рожден в {s.year_of_birth} году")

print("\nрезультаты по всем соревнованиям, установленные 12-05-2010 или 15-05-2010")
for s in session.query(Competition).filter(Competition.set_date.in_(["12-05-2010","15-05-2010"])):
    print(f"{s.competition_name} {s.world_record} установлен {s.set_date} ")

print("\nСоревнования в Москве и полученные на них результаты равны 10 секунд.")
for s in session.query(Result).filter(Result.city=="Москва").filter(Result.result==10):
    print(f" {s.hold_date}")

print("\nИмена всех спортсменов, у которых персональный рекорд менее 25с")
for s in session.query(Sportsman).filter(Sportsman.personal_record<25):
    print(f" Спортсмен {s.sportsman_name} рекорд менее 25с: {s.personal_record}")

