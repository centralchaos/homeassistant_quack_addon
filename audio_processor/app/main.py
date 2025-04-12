# home_assistant_addon/audio_processor/app/main.py

import logging
from fastapi import FastAPI, File, UploadFile
from fastapi.staticfiles import StaticFiles
import os

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = FastAPI()

# Mount the audio_uploader directory at /ui
app.mount("/ui", StaticFiles(directory="audio_uploader", html=True), name="ui")

UPLOAD_DIRECTORY = "/app/uploads"

# Ensure the upload directory exists
os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_location = os.path.join(UPLOAD_DIRECTORY, file.filename)
    with open(file_location, "wb") as buffer:
        buffer.write(await file.read())
    return {"message": f"File '{file.filename}' uploaded successfully"}

@app.get("/files")
async def list_files():
    files = os.listdir(UPLOAD_DIRECTORY)
    return {"files": files}

@app.post("/process/{filename}")
async def process_file(filename: str):
    file_path = os.path.join(UPLOAD_DIRECTORY, filename)
    # Add your processing logic here
    return {"message": f"File '{filename}' processed successfully"}

# Remove the root endpoint
# @app.get("/")
# async def root():
#     logger.debug("Root endpoint called")
#     return {"message": "Hello, World!"}

# Add your additional routes and logic here