from sqlmodel import Session

from .database import create_db_and_tables, engine
from .models import OrderProductLink, Order, Product, Customer


def create_customers():
    with Session(engine) as session:
        customer1 = Customer(name="kevin", headquarters="ptown")
        session.add(customer1)
        session.commit()
        session.refresh(customer1)

        print("Customer #1:", customer1)


def main():
    create_db_and_tables()
    create_customers()


if __name__ == "__main__":
    main()