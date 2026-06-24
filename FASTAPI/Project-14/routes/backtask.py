from fastapi import APIRouter, BackgroundTasks

router = APIRouter()

def write_log(message: str):
    with open("app.log", "a") as f:
        f.write(message + "\n")


@router.post("/background-task")
def run_background_task(name: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_log, f"User triggered task: {name}")

    return {"message": f"Task started for {name}"}