from sqlalchemy import create_engine, CHAR, ForeignKey, Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Person(Base):
    __tablename__="people"

    ssn = Column('ssn', Integer, primary_key=True)
    first_name = Column("firstname", String)
    last_name = Column('lastname', String)
    gender = Column('gender', CHAR)
    age = Column('age', Integer)

    def __init__(self, ssn, first_name, last_name, gender, age):
        self.ssn = ssn
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age


    def __repr__(self):
        return f"{self.ssn}"
    


engine = create_engine('sqlite:///mydb.db', echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()
    
person1 = Person(122222, "Mike", "okon", 'm', 34)
session.add(person1)
session.commit()
        
