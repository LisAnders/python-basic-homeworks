from typing import TYPE_CHECKING
from sqlalchemy import Column, String, Integer, DateTime, Boolean
from sqlalchemy.sql import func
from flask_sqlalchemy.query import Query
from .database import db

class Article(db.Model):
    id_art = Column(Integer, primary_key=True)
    code = Column(String(20), nullable=False)
    name = Column(String, nullable=False)
    status = Column(Boolean, nullable=False, default=True)
    lastdate = Column(DateTime, nullable=False, default=func.now(), server_default=func.now())
    
    if TYPE_CHECKING:
        query: Query
        
