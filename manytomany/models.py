from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel

from pydantic import BaseModel
""""
user = User.query.first()
user.products  # List all products, eg [<productA>, <productB> ]
user.orders    # List all orders, eg [<order1>, <order2>]
user.orders[0].products  # List products from the first order

p1 = Product.query.first()
p1.users  # List all users who have bought this product, eg [<user1>, <user2>]
"""


class OrderProductLink(SQLModel, table=True):
    order_id: Optional[int] = Field(
        default=None, foreign_key="order.id", primary_key=True
    )
    product_id: Optional[int] = Field(
        default=None, foreign_key="product.id", primary_key=True
    )

class CustomerBase(SQLModel):
    name: str = Field(index=True)
    headquarters: str
    
class Customer(CustomerBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    
    orders: List["Order"] = Relationship(back_populates="customer")                                    
class OrderBase(SQLModel):
    date_time: str
    
    customer_id: Optional[int] = Field(default=None, foreign_key="customer.id")
    
class Order(OrderBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    
    customer: Optional[Customer] = Relationship(back_populates="orders")
    products: List["Product"] = Relationship(back_populates="order",
    link_model=OrderProductLink)
    
class ProductBase(SQLModel):
    product_name: str
    price: int

class Product(ProductBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    order: Optional["Order"] = Relationship(back_populates='products', link_model=OrderProductLink)


