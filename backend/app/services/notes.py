from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from ..api.deps import get_async_session
from ..schemas.notes import NoteCreate
from ..repositories.notes import create_note

async def create_new_note(note: NoteCreate, db: AsyncSession = Depends(get_async_session)):
    return await create_note(note, db)




