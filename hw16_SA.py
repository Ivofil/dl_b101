from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, mapper

engine = create_engine('sqlite:///:memory:', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class sportsman(Base):
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

# Создание таблицы
Base.metadata.create_all(engine)

u1 = sportsman(1001, "Петоров Иван", "КМС", 1990, 9, "Россия")
u2 = sportsman(1002, "Иванов Иван", "МС", 1980, 19, "Россия")
u3 = sportsman(2001, "Сидоров Иван", "КМС", 1990, 39, "Россия");
u4 = sportsman(2002, "Ян Петр", "МС", 1990, 9, "Россия");
u5 = sportsman(5001, "Джошуа Барнетт", "КМС", 1980, 19, "США");

session.add(u1)
session.add(u2)
session.add(u3)
session.add(u4)
session.add(u5)

session.commit()

print("\nВся информация по спортсменам")
for s in session.query(sportsman):
    print(f" {s.sportsman_name}: {s.sportsman_name} разряд {s.rank} рекорд {s.personal_record}")

print("\nИмена всех спортсменов, которые родились в 1990 году. ")
for s in session.query(sportsman).filter(sportsman.year_of_birth==1990):
    print(f" Спортсмен {s.sportsman_name} рожден в {s.year_of_birth} году")

print("\nИмена всех спортсменов, у которых персональный рекорд менее 25с")
for s in session.query(sportsman).filter(sportsman.personal_record<25):
    print(f" Спортсмен {s.sportsman_name} рекорд менее 25с: {s.personal_record}")
