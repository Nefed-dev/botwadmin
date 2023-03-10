from base import Base
from sqlalchemy import Column, Integer, String, ForeignKey, ARRAY


class Message(Base):
    __tablename__ = "messages"
    id: int = Column(Integer, primary_key=True)
    parent_id: int = Column(Integer, ForeignKey("message.id"))
    button_text: str = Column(String(255))
    message_text: str = Column(String(255))
    media: str = Column(ARRAY(String))
