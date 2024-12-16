from sqlalchemy import Column, Integer, String, Text, Boolean
from ..database.creation_database import Base

class Task(Base):
    __tablename__ = "tasks"

    id_task = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), nullable=False)
    description = Column(Text, nullable=True)
    checked = Column(Boolean, default=False)