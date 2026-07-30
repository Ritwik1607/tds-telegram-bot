from fastapi import FastAPI
from fastapi.responses import FileResponse
from logger import logger

app = FastAPI()


@app.get("/")
def home():
    return {
        "status": "Data Analyst Agent running"
    }


@app.get("/logs")
def get_logs():

    return FileResponse(
        logger.get_log_path(),
        media_type="application/jsonl",
        filename="run.jsonl"
    )