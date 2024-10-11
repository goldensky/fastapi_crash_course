from database import new_session, TaskORM
from schemas import STaskAdd, STask
from sqlalchemy import select

class TaskRepository:
    @classmethod
    async def add_one(cls, data: STaskAdd) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()

            task = TaskORM(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id

    @classmethod
    async def find_all(cls) -> list[STask]:
        async with new_session() as session:
            query = select(TaskORM)
            result = await session.execute(query)

            task_models = result.scalars().all()
            print("task_models = ", task_models)
            task_schemas = [STask.model_validate(task_model) for task_model in task_models]
            print("task_schemas = ", task_schemas, type(task_schemas))
            return task_schemas



