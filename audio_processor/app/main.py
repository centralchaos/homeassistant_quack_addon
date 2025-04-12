# home_assistant_addon/audio_processor/app/main.py

import logging
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = FastAPI()

# Mount the audio_uploader directory
app.mount("/", StaticFiles(directory="audio_uploader", html=True), name="static")

# Remove the root endpoint
# @app.get("/")
# async def root():
#     logger.debug("Root endpoint called")
#     return {"message": "Hello, World!"}

# Add your additional routes and logic here