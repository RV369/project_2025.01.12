from fastapi import Body, FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()


class Schema(BaseModel):
    text: str | list[str]


clf = pipeline(
    task='sentiment-analysis',
    model='SkolkovoInstitute/russian_toxicity_classifier',
)


def data_pipline(text):
    data_rezult = []
    if type(text) is str:
        for sentence in text.split('.'):
            if sentence != '':
                rezult = clf(sentence)
                rezult[0].update({'string': f'{sentence}'})
                data_rezult.append(rezult)
            else:
                continue
    else:
        for i in text:
            data_rezult.append(data_pipline(i))
    return data_rezult


@app.post('/', response_model=Schema)
def get_pipline(data_text=Body()):
    return JSONResponse(
        status_code=200, content=data_pipline(data_text['text']))
