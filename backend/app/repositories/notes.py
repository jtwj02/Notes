from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from ..api.deps import get_async_session
from ..schemas.notes import NoteCreate
from ..models import Notes

async def create_note(note: NoteCreate, db: AsyncSession = Depends(get_async_session)):
    new_note = Notes(**(note.model_dump()))
    async with db.begin():
        db.add(new_note)
    await db.refresh(new_note)
    return new_note

