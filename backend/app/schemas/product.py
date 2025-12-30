from datetime import datetime

from pydantic import BaseModel, Field
from typing import Optional
from .category import CategoryResponse


class ProductOrigin(BaseModel):

    name: str = Field(
        ...,
        min_length=5,
        max_length=200,
        description='Product name',
    )

    description: Optional[str] = Field(
        None,
        min_length=5,
        max_length=500,
        description='Product description',
    )

    price: float = Field(
        ...,
        gt=0,
        description='Product price(greater than zero)',
    )

    category_id: int = Field(
        ...,
        description='Category id',
    )

    image_url: Optional[str] = Field(
        None,
        description='Product image url',
    )


class ProductCreate(ProductOrigin):
    pass


class ProductResponse(BaseModel):
    id: int = Field(
        ...,
        description='Unique product ID',
    )

    name: str
    description: Optional[str]
    price: float
    category_id: int
    image_url: Optional[str]
    created_at: datetime
    category: CategoryResponse = Field(
        ...,
        description='Product category details',
    )

    class Config:
        form_attributes = True


class ProductListResponse(BaseModel):
    products: list[ProductResponse]
    total: int = Field(
        ...,
        gt=0,
        description='Total number of products(greater than zero)',
    )
