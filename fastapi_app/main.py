from fastapi import FastAPI
import asyncio

from consumer import consume

# Add logging configuration at the beginning of your main file
# import logging

# logging.basicConfig(level=logging.DEBUG)  # Enable debug logs

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    loop = asyncio.get_event_loop()
    loop.create_task(consume())


@app.get("/")
async def read_root():
    return {"message": "Hello from FastAPI"}
