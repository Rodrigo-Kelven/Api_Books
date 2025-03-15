from sqlalchemy import Column, Integer, String
from config.config_db import Base_books as Base


class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)

