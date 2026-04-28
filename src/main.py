from fastapi import FastAPI, HTTPException

app = FastAPI()

tasks = []

@app.get("/")
def home():
    return {"message": "Hello World! Welcome to the Task Manager API. keep adding tasks to your list and manage them easily."}

@app.get("/tasks")
def get_tasks():
    return tasks

@app.post("/tasks")
def add_task(task: str):
    tasks.append(task)
    return {"message": "Task added", "tasks": tasks}

@app.get("/tasks/{index}")
def get_task(index: int):
    if 0 <= index < len(tasks):
        return {"task": tasks[index]}
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{index}")
def delete_task(index: int):
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        return {"removed": removed}
    raise HTTPException(status_code=404, detail="Task not found")