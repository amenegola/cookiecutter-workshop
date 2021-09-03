import os
import json
from joblib import load
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

class JsonIn(BaseModel):
    season: int
    mnth: int
    holiday: int
    weekday: int
    workingday: int
    weathersit: int
    temp: float
    atemp: float
    hum: float
    windspeed: float

class JsonOut(BaseModel):
    outcome: dict

app = FastAPI()

models = load("/source/models/model.joblib")

@app.post("/api/v1/predictions", response_model=JsonOut)
async def predict(input_model: JsonIn):
    input_data = dict(input_model)
    df_input = pd.json_normalize(input_data)
    prediction = model.predict(df_input)[0]
    return {"output": prediction}
