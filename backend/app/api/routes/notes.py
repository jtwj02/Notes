from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from ...schemas.notes import NoteCreate
from ..deps import get_async_session
from ...services.notes import create_new_note

router = APIRouter(prefix="/notes", tags=["Notes"])

@router.get("/")
def get_all_notes():
    return {"message": "success"}

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_note(note: NoteCreate, db: AsyncSession = Depends(get_async_session)):
    return await create_new_note(note, db)
