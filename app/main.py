import os

import uvicorn
import uuid
from typing import Union, Dict
from fastapi import FastAPI
from sqlalchemy import create_engine
from starlette.responses import JSONResponse
from pydantic import BaseModel
from sqlalchemy.orm import Session
from db import Secret, engine

session = Session(engine)

class GenerateRequestBody(BaseModel):
    secret: str


class GenerateResponseBody(BaseModel):
    secret_key: str


app = FastAPI()

in_memory = {}


@app.post("/generate", response_model=GenerateResponseBody)
async def create_item(body: GenerateRequestBody):
    secret_key = str(uuid.uuid4())
    # in_memory[secret_key] = body.secret
    exemplyar = Secret(secret=body.secret, secret_key=secret_key)
    session.add(exemplyar)
    session.commit()

    response = GenerateResponseBody(secret_key=secret_key)
    return response


@app.get("/secrets/{secret_key}")
async def create_item(secret_key: str):
    # secret = in_memory[secret_key]
    exemplar = session.query(Secret).filter(Secret.secret_key==secret_key)

    return JSONResponse({"secret": exemplar.first()})



#
if __name__ == '__main__':

    # Команда на запуск uvicorn.
    # Здесь же можно указать хост и/или порт при необходимости,
    # а также другие параметры.
    uvicorn.run('main:app', reload=True, host="127.0.0.1", port=8000)
