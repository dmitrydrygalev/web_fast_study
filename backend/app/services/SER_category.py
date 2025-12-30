from sqlalchemy.orm import Session
from typing import List
from fastapi import HTTPException, status

from ..repositories.REP_category import CategoryRepository
from ..schemas.SCH_category import CategoryResponse, CategoryCreate


class CategoryService:
    def __init__(self, db: Session):
        self.repository = CategoryRepository(db)

    def get_all(self) -> List[CategoryResponse]:
        categories = self.repository.get_all_categories()
        return [CategoryResponse.model_validate(c) for c in categories]

    def get_by_id(self, category_id: int) -> CategoryResponse:
        category = self.repository.get_category_by_id(category_id)

        if not category:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Category with id {category_id} not found"
            )

        return CategoryResponse.model_validate(category)

    def init_category(self, category_data: CategoryCreate) -> CategoryResponse:
        inited_category = self.repository.init_new_category(category_data)
        return CategoryResponse.model_validate(inited_category)