"""
engine is use to connect to postgreSQL 
the sessionmaker creates a session pooler
Every session gets its own session
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autoCommit=False
)