import os
import json
from joblib import load
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

class JsonIn(BaseModel):
    age: int
    gender: str
    openAnswer: str

class JsonOut(BaseModel):
    modelVersion: str
    trainingId: str
    userOutcome: dict

app = FastAPI()

models = load("/source/models/model.joblib")

@app.post("/api/v1/predictions", response_model=JsonOut)
async def predict(input_model: JsonIn):
    input_data = dict(input_model)

    prediction = model.predict_proba(request=input_data)

    return {"output": prediction}
