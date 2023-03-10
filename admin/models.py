from base import Base
from sqlalchemy import Column, Integer, String, ARRAY


class Message(Base):
    __tablename__ = "messages"
    id: int = Column(Integer, primary_key=True)
    parent_id: int = Column(Integer)
    button_text: str = Column(String(255))
    message_text: str = Column(String(255))
    media: str = Column(ARRAY(String))

    def getall(self):
        return [
            Message.id,
            Message.parent_id,
            Message.button_text,
            Message.message_text,
            Message.media
        ]
