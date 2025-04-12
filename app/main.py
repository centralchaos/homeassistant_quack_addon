# home_assistant_addon/app/main.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, World!"}

# Add your additional routes and logic here