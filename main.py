# FastAPI
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import time
# Routers
from routers import spaceX


# app definition
app = FastAPI()

# app config
app.include_router(spaceX.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

