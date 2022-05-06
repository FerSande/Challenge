import logging
from fastapi import APIRouter,Request
from utilidades.FlavorCards import total
from typing import Optional
from pydantic import BaseModel
logging.basicConfig(level=logging.INFO)

router = APIRouter(responses={404: {"description": "Not found"}})

class Task(BaseModel):
    type: str
    title: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = None
    class Config:
        schema_extra = {
            "example": {
                "type": "issue",
                "title": "Send message",
                "description": "Let pilots send messages to Central"
            }
        }

@router.post("/trello_tasks")
async def executeTrelloTasks(task: Task):
    task = total(task)
    return task


