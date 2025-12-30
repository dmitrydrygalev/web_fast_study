from sqlalchemy.orm import Session, joinedload
from typing import List, Optional

from ..models.MOD_product import Product
from ..schemas.SCH_product import ProductCreate


class ProductRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_products_all(self) -> List[Product]:
        return (self.db.query(Product)
                .options(joinedload(Product.category))
                .all())

    def get_product_by_id(self, product_id: int) -> Optional[Product]:
        return (self.db.query(Product)
                .options(joinedload(Product.category))
                .filter(Product.id == product_id)
                .first())

    def get_product_by_category_id(self, category_id: int) -> Product:
        return (
            self.db.query(Product)
            .options(joinedload(Product.category))
            .filter(Product.category_id == category_id)
            .all()
        )

    def init_new_product(self, product_data: ProductCreate) -> Product:
        db_product = Product(**product_data.model_dump())
        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        return db_product

    def get_several_products_by_id_lst(self, products_ids: List[int]) -> List[Product]:
        return (
            self.db.query(Product)
            .options(joinedload(Product.category))
            .filter(Product.id.in_(products_ids))
            .all()
        )