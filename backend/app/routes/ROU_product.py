from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..services.SER_product import ProductService
from ..schemas.SCH_product import ProductResponse, ProductListResponse

router = APIRouter(
    prefix="/api/products",
    tags=["products"],
)


@router.get("", response_model=ProductListResponse, status_code=status.HTTP_200_OK)
def get_products(db: Session = Depends(get_db)):
    return ProductService(db).get_all()


@router.get("/{product_id}", response_model=ProductResponse, status_code=status.HTTP_200_OK)
def get_product(product_id: int, db: Session = Depends(get_db)):
    return ProductService(db).get_by_own_id(product_id)


@router.get("/category/{category_id}", response_model=ProductListResponse, status_code=status.HTTP_200_OK)
def get_product_by_category_id(category_id: int, db: Session = Depends(get_db)):
    return ProductService(db).get_by_category_id(category_id)