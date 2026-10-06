# -*- coding: utf-8 -*-
"""团队看板服务（夹具）——4 端点。"""
from fastapi import FastAPI

app = FastAPI()

TASKS = {}

@app.get("/boards")
def get_board():
    return {"columns": ["todo", "doing", "done"], "tasks": list(TASKS.values())}

@app.post("/tasks")
def create_task(name: str, column: str = "todo"):
    task_id = "t_" + name
    TASKS[task_id] = {"id": task_id, "name": name, "column": column, "blocked": False}
    return TASKS[task_id]

@app.patch("/tasks/{id}")
def move_task(id: str, column: str):
    TASKS[id]["column"] = column
    return TASKS[id]

@app.delete("/tasks/{id}")
def delete_task(id: str):
    return {"ok": TASKS.pop(id, None) is not None}
