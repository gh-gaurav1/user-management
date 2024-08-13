# main.py
from fastapi import FastAPI
from routes import router
import logging
from fastapi.middleware.cors import CORSMiddleware


origins = [
    "http://localhost:3000",
]

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*']
    
)

logging.basicConfig(level=logging.INFO)


app.include_router(router)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)