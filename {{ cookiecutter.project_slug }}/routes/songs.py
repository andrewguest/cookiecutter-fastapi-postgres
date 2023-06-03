from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.db import get_session
from models.song import Song, SongCreate


router = APIRouter(tags=["songs"])


@router.get("/songs", response_model=list[Song])
async def get_songs(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Song))
    songs = result.scalars().all()

    return [
        Song(name=song.name, artist=song.artist, id=song.id) for song in songs
    ]


@router.post("/songs")
async def add_song(
    song: SongCreate, session: AsyncSession = Depends(get_session)
):
    song = Song(name=song.name, artist=song.artist)
    session.add(song)
    await session.commit()
    await session.refresh(song)
    return song
