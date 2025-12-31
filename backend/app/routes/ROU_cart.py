from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import Dict
from ..database import get_db
from ..services.SER_cart import CartService
from ..schemas.SCH_cart import CartItemCreate, CartItemUpdate, CartReponse
from pydantic import BaseModel

router = APIRouter(
    prefix='/api/cart',
    tags=["cart"],
)


class AddToCartItem(BaseModel):
    product_id: str
    amount: int
    cart: Dict[int, int] = {}


class UpdateCartRequest(BaseModel):
    product_id: str
    amount: int
    cart: Dict[int, int] = {}


class RemoveFromCartRequest(BaseModel):
    cart: Dict[int, int] = {}


@router.get('/add', status_code=status.HTTP_200_OK)
def add_to_cart(
        request: AddToCartItem,
        db: Session = Depends(get_db),
    ):
    service = CartService(db)
    item = CartItemCreate(product_id=request.product_id, amount=request.amount)
    update_cart = service.add_to_cart(request.cart, item)
    return {"cart": update_cart}


@router.get('', response_model=CartReponse, status_code=status.HTTP_200_OK)
def get_cart(cart_data: Dict[int, int], db: Session = Depends(get_db)):
    return CartService(db).get_cart_details(cart_data)


@router.put('/update', status_code=status.HTTP_200_OK)
def update_cart_item(request: UpdateCartRequest, db: Session = Depends(get_db)):
    service = CartService(db)
    item = CartItemUpdate(product_id=request.product_id, amount=request.amount)
    update_cart = service.update_cart_item(request.cart, item)
    return {"cart": update_cart}


@router.delete('/remove/{product_id}', status_code=status.HTTP_200_OK)
def remove_item_from_cart(product_id: int, reques: RemoveFromCartRequest, db: Session = Depends(get_db)):
    service = CartService(db)
    update_cart = service.del_from_cart(reques.cart, product_id)
    return {"cart": update_cart}