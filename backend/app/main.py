import sys
import asyncio

if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes.scan import router as scan_router

app = FastAPI(
    title = "ShopSafe",
    version = "1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)
app.include_router(scan_router)

@app.get("/")
def home():
    return {
        "status":"running",
        "project":"ShopSafe"
    }