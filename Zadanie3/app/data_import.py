import csv
import os
from django.db import transaction
from .models import WineData
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///python3task.db"
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def map_quality(value):
    """Maps quality values to the range 1-3."""
    if value in [3, 4, 5]:
        return 1
    elif value == 6:
        return 2
    elif value in [7, 8, 9]:
        return 3
    else:
        raise ValueError(f"Incorrect quality value: {value}")

def import_csv_to_db_if_empty():
    """Import data from a CSV file into the database only if the table is empty."""
    session = SessionLocal()

    if session.query(WineData).count():
        print("The WineData table is not empty. Skipping the data import.")
        return

    print("WineData table is empty. Importing the data from a CSV file....")

    # Path to the CSV file
    csv_file_path = os.path.join(os.path.dirname(__file__), 'wine_data.csv')

    if not os.path.exists(csv_file_path):
        print(f"File {csv_file_path} does not exist. Skipping the data import.")
        return

    with open(csv_file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')  # Load the CSV as a dictionary

        for row in reader:
            try:
                wine_data = WineData(
                    fixed_acidity=float(row["fixed acidity"]),
                    volatile_acidity=float(row["volatile acidity"]),
                    citric_acid=float(row["citric acid"]),
                    residual_sugar=float(row["residual sugar"]),
                    chlorides=float(row["chlorides"]),
                    free_sulfur_dioxide=float(row["free sulfur dioxide"]),
                    total_sulfur_dioxide=float(row["total sulfur dioxide"]),
                    density=float(row["density"]),
                    pH=float(row["pH"]),
                    sulphates=float(row["sulphates"]),
                    alcohol=float(row["alcohol"]),
                    quality=map_quality(int(row["quality"]))
                )
                session.add(wine_data)
                session.commit()
            except ValueError as e:
                session.rollback()
                print(f"Error in the line: {row} - {e}")
    print("Data import completed.")
    session.close()
