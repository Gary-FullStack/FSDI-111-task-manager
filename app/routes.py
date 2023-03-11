from flask import Flask, request
from app.database import task


app = Flask(__name__)


@app.get("/")
@app.get("/ping")
def pong():
    out = {
        "message": "pong"
    }
    return out

@app.get ("/tasks")
def get_all_tasks():
    task_list = task.scan()
    out = {
        "tasks": task_list,
        "message": "success"
    }    
    return out

@app.get("/tasks/<int:pk>")
def get_task_by_id(pk):
    task_obj = task.select_by_id(pk)
    out = {
        "task": task_obj,
        "message": "success"
    }
    return out

@app.post("/tasks")
def create_task():
    raw_data = request.json
    task_data = {
        "summary": raw_data.get("summary"),
        "description": raw_data.get("description"),
        "status": raw_data.get("status"),
        "active": raw_data.get("active")
    }
    task.insert(task_data)
    return "", 204

@app.put("/tasks/<int:pk>")
def update_task(pk):
    raw_data = request.json
    task_data = {
        "summary": raw_data.get("summary"),
        "description": raw_data.get("description"),
        "status": raw_data.get("status"),
        "active": raw_data.get("active")    
    }
    task.update(task_data, pk)
    return "", 204

@app.delete("/tasks/<int:pk>")
def delete_task(pk):
    task.delete(pk)
    return "", 204