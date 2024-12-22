from sqlalchemy import Column, Integer, String, create_engine, FLOAT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Connecting with SQLite database
DATABASE_URL = "sqlite:///python3task.db"
engine = create_engine(DATABASE_URL, echo=True)

Base = declarative_base()

class Klasa(Base):
    __tablename__ = 'klasa'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    x = Column(FLOAT, nullable=False)
    y = Column(FLOAT, nullable=False)

    def __repr__(self):
        return f'<Klasa(id={self.id}, name={self.name}, x={self.x}, y={self.y})>'

Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)