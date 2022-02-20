from sqlmodel import Field, Relationship, Session, SQLModel, create_engine, select

import datetime

from faker import Faker

from .models import OrderProductLink, Order, Product, Customer


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url)

fake = Faker()
    
def create_db_and_tables():
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)

def session_factory():
        session = Session(engine)
        return session
        
def create_customers():
    session = session_factory()
    with session as session:
        for idx in range(100):
            customer1 = Customer(
                            first_name=fake.first_name(),
                            last_name=fake.last_name(),
                            address=fake.street_address(),
                            city=fake.city(),
                            postcode=fake.postcode(),
                            email=fake.email(),
                            time_created=datetime.datetime.utcnow()
                        )
            session.add(customer1)
            session.commit()
            session.refresh(customer1)

            print(f"Customer #{idx}:", customer1)