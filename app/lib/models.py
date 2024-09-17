from datetime import datetime

from sqlalchemy import (create_engine, desc, CheckConstraint, UniqueConstraint,
                        Column, DateTime, Integer, String)
from sqlalchemy.orm import declarative_base

engine = create_engine('sqlite:///migration_test.db')

Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'
    __table_args__ = (CheckConstraint('grade BETWEEN 1 AND 12',
                                      name='grade_between_1_and_12'), )

    id = Column(Integer(), primary_key=True)
    name = Column(String(), index=True)
    email = Column(String(55), unique=True)
    grade = Column(Integer())
    birthday = Column(DateTime())
    enrolled_date = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return f"Student({self.id}, {self.name}, {self.grade})"
