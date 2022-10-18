'''Main file for FastAPI app.'''

from fastapi import FastAPI

from common.constants import FILE_HEADERS
from services.fileservice import FileService as fs


app = FastAPI()


@app.get("/")
def get_root():
    return {"Hello": "User!"}


@app.get(FILE_HEADERS)
def get_file_headers():
    obj = fs()
    return {"column_names": obj.get_column_names()}
