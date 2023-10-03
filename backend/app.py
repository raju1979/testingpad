from functools import partial
from fastapi import FastAPI, Request
import sys
import time

from pymongo import MongoClient
from dotenv import load_dotenv
from dotenv import dotenv_values
import os
from fastapi.encoders import jsonable_encoder
from typing import Any, Coroutine, List
from middlewares import CheckApiKey

from models.book import Book, BookUpdate

from routes.book import router as book_router

from routes.project import router as project_router

from starlette.middleware.base import BaseHTTPMiddleware

from middlewares.Middlewares import auth_header_middleware

from fastapi.responses import JSONResponse


#load_dotenv()  # Load environment variables from .env file

config = dotenv_values(".env")
app = FastAPI()

# MongoDB configuration

mongo_uri = os.getenv('MONGO_URI')
mongo_client = MongoClient(mongo_uri)
db = mongo_client['testingpad']
collection = db['your_collection_name']  # Replace with your collection name

# Set the default encoding to datetime.datetime
#mongo_client.codec_options.uuid_representation = 1  # Use standard UUID representation
mongo_client.codec_options.DatetimeRepresentation = 2  # Use standard datetime.datetime

def receive_signal(signalNumber, frame):
    print('Received:', signalNumber)
    sys.exit()

# Define a simple middleware function
# async def catch_exceptions_middleware(request: Request, call_next):
#     try:
#         return await call_next(request)
#     except Exception:
#         # you probably want some kind of logging here
#         print_exception(e)
#         return Response("Internal server error", status_code=500)

# app.middleware('http')(catch_exceptions_middleware)

# Apply the custom middleware to the entire FastAPI app

@app.exception_handler(Exception)
async def validation_exception_handler(request, err):
    base_error_message = f"Failed to execute: {request.method}: {request.url}"
    # Change here to LOGGER
    return JSONResponse(status_code=400, content={"message": f"{base_error_message}. Detail: {err}"})


app.middleware("http")(auth_header_middleware)

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response    

@app.on_event("startup")
def startup_db_client():
    import signal
    signal.signal(signal.SIGINT, receive_signal)
    try:
        app.mongodb_client = MongoClient(config["MONGO_URI"])
        app.database = app.mongodb_client[config["DB_NAME"]]
        app.mongodb_client.server_info()
    except:
        raise ConnectionError("MongoDB connection failed. Please check the MongoDB URI.")

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()

app.include_router(book_router, tags=["books"], prefix="/book")    
app.include_router(project_router, tags=["projects"], prefix="/project")    

if __name__ == "__main__":
    import os
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8001)), reload=True,
    reload_dirs=['./'])
