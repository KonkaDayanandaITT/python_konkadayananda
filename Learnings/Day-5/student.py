from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


engine = create_engine("sqlite:///students.db", echo=True)

Base = declarative_base()

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

student = [Student(name="varun", age =22),
        Student(name="sam", age =18),
        Student(name="jack", age =18)
]

session.add_all(student)
session.commit()

students = session.query(Student).all()

for s in students:
    print(s.id, s.name, s.age)
