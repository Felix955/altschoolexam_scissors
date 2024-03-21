import sqlalchemy
import uuid
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ShortenedURL(Base):
    __tablename__ = "url"

    id = Column(sqlalchemy.types.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    old_url = Column(String)
    new_url = Column(String)

