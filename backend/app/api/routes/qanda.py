import uuid
from typing import Any

from fastapi import APIRouter, HTTPException
from sqlmodel import func, select

from app.api.deps import CurrentUser, SessionDep
from app.models import Item, ItemCreate, ItemPublic, ItemsPublic, ItemUpdate, Message

router = APIRouter()


@router.post("/", response_model=ItemPublic)
def prompt(
        # *, session: SessionDep, current_user: CurrentUser, item_in: ItemCreate
) -> Any:
    # item = Item.model_validate(item_in, update={"owner_id": current_user.id})
    # session.add(item)
    # session.commit()
    # session.refresh(item)
    return {"response": "success FIXME"}


@router.get("/")
def prompt(
        # *, session: SessionDep, current_user: CurrentUser, item_in: ItemCreate
) -> Any:
    # item = Item.model_validate(item_in, update={"owner_id": current_user.id})
    # session.add(item)
    # session.commit()
    # session.refresh(item)
    return {"response": "success FIXME"}

