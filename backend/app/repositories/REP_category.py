from sqlalchemy.orm import Session
from typing import List, Optional

from ..models.MOD_category import Category
from ..schemas.SCH_category import CategoryCreate


class CategoryRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all_categories(self) -> List[Category]:
        return self.db.query(Category).all()

    def get_category_by_id(self, category_id: int) -> Optional[Category]:
        return self.db.query(Category).filter(Category.id == category_id).first()

    def get_category_by_slug(self, slug: str) -> Optional[Category]:
        return self.db.query(Category).filter(Category.slug == slug).first()

    def init_new_category(self, category_data: CategoryCreate) -> Category:
        db_category = Category(**category_data.model_dump())
        self.db.add(db_category)
        self.db.commit()
        self.db.refresh(db_category)
        return db_category