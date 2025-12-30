from sqlalchemy.orm import Session
from typing import List
from fastapi import HTTPException, status

from ..repositories.REP_product import ProductRepository
from ..repositories.REP_category import CategoryRepository
from ..schemas.SCH_product import ProductListResponse, ProductResponse, ProductCreate


class ProductService:
    def __init__(self, db: Session):
        self.product_repository = ProductRepository(db)
        self.category_repository = CategoryRepository(db)

    def get_all(self) -> ProductListResponse:
        products = self.product_repository.get_products_all()
        products_response = [ProductResponse.model_validate(prod) for prod in products]

        return ProductListResponse(products=products_response, total=len(products))

    def get_by_own_id(self, product_id: int) -> ProductResponse:
        product = self.product_repository.get_product_by_id(product_id)

        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Product with id {product_id} not found"
            )

        return ProductResponse.model_validate(product)

    def get_by_category_id(self, category_id: int) -> ProductListResponse:

        category = self.category_repository.get_category_by_id(category_id)
        if not category:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Product with category id {category_id} not found"
            )

        products = self.product_repository.get_product_by_category_id(category_id)
        products_response = [ProductResponse.model_validate(prod) for prod in products]
        return ProductListResponse(products=products_response, total=len(products))

    def get_several(self, products_ids: List[int]) -> ProductListResponse:
        products = self.product_repository.get_several_products_by_id_lst(products_ids)
        products_response = [ProductResponse.model_validate(prod) for prod in products]
        return ProductListResponse(products=products_response, total=len(products))

    def init_product(self, product_data: ProductCreate) -> ProductResponse:
        category = self.category_repository.get_category_by_id(product_data.category_id)

        if not category:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Category with id {product_data.category_id} not found"
            )

        product = self.product_repository.init_new_product(product_data)
        return ProductResponse.model_validate(product)