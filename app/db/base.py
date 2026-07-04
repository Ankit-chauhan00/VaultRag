"""
with base class we can use its function like 
create table, migration, relations
"""
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass