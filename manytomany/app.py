from sqlmodel import Session

from .database import create_db_and_tables, create_customers


def main():
    create_db_and_tables()
    create_customers()
    # add_orders()
    # add_products()
    # add_order_products()


if __name__ == "__main__":
    main()