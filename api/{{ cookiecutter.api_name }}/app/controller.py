import os
import json
import pandas as pd
from joblib import load
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

class JsonIn(BaseModel):
    input_1: int
    input_2: float

class JsonOut(BaseModel):
    output: float

app = FastAPI()

model = load("models/model.pkl")

@app.post("/api/v1/predictions", response_model=JsonOut)
async def predict(input_model: JsonIn):
    input_data = dict(input_model)
    df_input = pd.json_normalize(input_data)
    prediction = model.predict(df_input)[0]
    return {"output": prediction}
