from pydantic import BaseModel, Field
from typing import Optional


class CartOrigin(BaseModel):
    product_id: int = Field(
        ...,
        description='Product ID'
    )

    amount: int = Field(
        ...,
        gt=0,
        description='Amount of product in cart(greater than zero)'
    )


class CartItemCreate(CartOrigin):
    pass


class CartItemUpdate(BaseModel):
    product_id: int = Field(
        ...,
        description='Product ID'
    )

    amount: int = Field(
        ...,
        gt=0,
        description='Amount of product in cart(greater than zero)'
    )


class CartItem(BaseModel):
    product_id: int
    name: str = Field(
        ...,
        description='Product name'
    )

    price: float = Field(
        ...,
        gt=0,
        description='Price of product in cart(greater than zero)'
    )

    amount: int = Field(
        ...,
        gt=0,
        description='Amount of product in cart(greater than zero)'
    )

    union_price: float = Field(
        ...,
        gt=0,
        description='Union price of product in cart(greater than zero|f=price*amount)'
    )

    image_url: Optional[str] = Field(
        ...,
        description='Product image url'
    )


class CartReponse(BaseModel):
    items: list[CartItem] = Field(
        ...,
        description='List of item in cart'
    )

    union_price: float = Field(
        ...,
        gt=0,
        description='Union cart price(greater than zero)'
    )

    items_amount: int = Field(
        ...,
        gt=0,
        description='Amount of items in cart(greater than zero)'
    )