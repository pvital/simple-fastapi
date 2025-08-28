import os
from typing import Union

import instana  # noqa: F401
import psutil
from fastapi import FastAPI, HTTPException

app = FastAPI()

pid = os.getpid()
print(pid)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    if not psutil.pid_exists(item_id):
        raise HTTPException(status_code=404, detail="Item not found")

    # procs = {p.pid: p.info for p in psutil.process_iter(['name', 'username'])}
    procs = {p.pid: p for p in psutil.process_iter()}
    return {"item_id": item_id, "info": procs[item_id].as_dict()}
