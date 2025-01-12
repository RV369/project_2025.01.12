from fastapi import Body, FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from .core import data, data_list

app = FastAPI()


class Schema(BaseModel):
    text: str | list[str]


@app.post('/', response_model=Schema)
def get_pipline(data_text=Body()):
    if type(data_text['text']) is str:
        return JSONResponse(status_code=200, content=data(data_text['text']))
    return JSONResponse(status_code=200, content=data_list(data_text['text']))
