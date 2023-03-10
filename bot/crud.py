from model import Message
from sqlalchemy import select


class Crud:
    def __init__(self, session):
        self.session = session

    async def get_all(self):
        pass

    async def get_one(self, id: int) -> Message:
        stmt = select(Message).where(Message.id == id)
        result = await self.session.execute(stmt)
        return result.scalar_one()

    async def get_by_parent_id(self, parent_id: int) -> Message:
        stmt = select(Message).where(Message.parent_id == parent_id)
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def delete_one(self, id: int):
        pass

    async def patch_one(self):
        pass
