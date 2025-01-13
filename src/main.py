from fastapi import Body, FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from .core import data_pipline

app = FastAPI()


class Schema(BaseModel):
    text: str | list[str]


@app.post('/', response_model=Schema)
def get_pipline(data_text=Body()):
    return JSONResponse(
        status_code=200, content=data_pipline(data_text['text']))
