from sqlalchemy import Column, Integer, create_engine, FLOAT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Connecting with SQLite database
DATABASE_URL = "sqlite:///python3task.db"
engine = create_engine(DATABASE_URL, echo=True)

Base = declarative_base()

class WineData(Base):
    __tablename__ = 'wine_data'

    id = Column(Integer, primary_key=True, autoincrement=True)
    fixed_acidity = Column(FLOAT, nullable=False)
    volatile_acidity = Column(FLOAT, nullable=False)
    citric_acid = Column(FLOAT, nullable=False)
    residual_sugar = Column(FLOAT, nullable=False)
    chlorides = Column(FLOAT, nullable=False)
    free_sulfur_dioxide = Column(FLOAT, nullable=False)
    total_sulfur_dioxide = Column(FLOAT, nullable=False)
    density = Column(FLOAT, nullable=False)
    pH = Column(FLOAT, nullable=False)
    sulphates = Column(FLOAT, nullable=False)
    alcohol = Column(FLOAT, nullable=False)
    quality = Column(Integer, nullable=False)

    def __repr__(self):
        return (f"<WineData(fixed_acidity={self.fixed_acidity}, volatile_acidity={self.volatile_acidity}, "
                f"citric_acid={self.citric_acid}, residual_sugar={self.residual_sugar}, chlorides={self.chlorides}, "
                f"free_sulfur_dioxide={self.free_sulfur_dioxide}, total_sulfur_dioxide={self.total_sulfur_dioxide}, "
                f"density={self.density}, pH={self.pH}, sulphates={self.sulphates}, alcohol={self.alcohol}, "
                f"quality={self.quality})>")

Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)