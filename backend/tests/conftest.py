
import asyncio
import pytest
from typing import AsyncGenerator
from httpx import AsyncClient, ASGITransport
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.infrastructure.database import Base
from app.core.config import settings

# Import models so Base.metadata knows them
from app.infrastructure.models.user import UserModel
from app.infrastructure.models.task import TaskModel

@pytest.fixture(scope="session")
async def db_engine():
    # Use a test database or the existing one depending on env
    # For simplicity in this plan, we rely on the docker service 'db'
    engine = create_async_engine(settings.DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://"))
    
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        
        # Seed a dummy user for foreign key constraints
        from sqlalchemy import insert
        await conn.execute(
            insert(UserModel).values(
                id=1, 
                email="student@example.com", 
                hashed_password="fake", 
                full_name="Test Student"
            )
        )
    
    yield engine
    
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    
    await engine.dispose()

@pytest.fixture
async def db_session(db_engine) -> AsyncGenerator[AsyncSession, None]:
    async_session = sessionmaker(
        db_engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session

@pytest.fixture
async def client(db_session) -> AsyncGenerator[AsyncClient, None]:
    from app.main import app
    from app.infrastructure.database import get_db
    
    async def override_get_db():
        yield db_session

    app.dependency_overrides[get_db] = override_get_db
    
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as c:
        yield c
    
    app.dependency_overrides.clear()
