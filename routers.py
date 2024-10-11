from typing import Annotated

from fastapi import Depends
from fastapi import APIRouter

from repository import TaskRepository
from schemas import STaskAdd, STask, STaskId


router = APIRouter(
    prefix="/tasks",
    tags=["Tasks!"],
)


@router.post("")
async def add_task(
        task: Annotated[STaskAdd, Depends()]
) -> STaskId:
    print("+++++++++++++++++==")
    print("task to add = ", task, type(task))
    task_id = await TaskRepository.add_one(task)
    print("TASK_ID = ", task_id)
    return {"ok": True, "task_id": task_id}


@router.get("")
async def get_tasks() -> list[STask]: #
    tasks = await TaskRepository.find_all()
    print("TTT = ", tasks)
    return tasks

