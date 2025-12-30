from pydantic import BaseModel, Field


class CategoryOrigin(BaseModel):
    name: str = Field(
        ...,
        min_length=5,
        max_length=100,
        description='Category name'
    )

    slug: str = Field(
        ...,
        min_length=5,
        max_length=100,
        description='ULR-friendly category name'
    )


class CategoryCreate(CategoryOrigin):
    pass


class CategoryResponse(CategoryOrigin):
    id: int = Field(
        ...,
        description='Unique category ID'
    )
    
    class Config:
        form_attributes = True
