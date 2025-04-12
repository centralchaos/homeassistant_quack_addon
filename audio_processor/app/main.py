# home_assistant_addon/audio_processor/app/main.py

import logging
from fastapi import FastAPI

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/")
async def root():
    logger.debug("Root endpoint called")
    return {"message": "Hello, World!"}

# Add your additional routes and logic here