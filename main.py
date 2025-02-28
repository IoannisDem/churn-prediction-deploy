from fastapi import FastAPI
from pydantic import BaseModel 
from typing import List, Union
from xgboost import XGBClassifier
import numpy as np

app = FastAPI()

class InputData(BaseModel):
    features: List[Union[int, float, bool]]

@app.get("/")
async def health_check():
    return{"Hello":"World"}

@app.post("/predict/")
async def inference(input_data: InputData):
    model = XGBClassifier()
    model.load_model("./best_model/model.xgb")
    pred = model.predict(np.expand_dims(np.array(input_data.features), 0))
    return{"result":pred.tolist()}

