from pydantic import BaseModel, Field
from fastapi import FastAPI
from typing import Annotated, Literal
from fastapi.responses import JSONResponse
from joblib import load
import pandas as pd
import numpy as np

app = FastAPI()

# Import models
model = load('model.joblib')

# Pydantic Validation
class UserInput(BaseModel):
    Area : Annotated[str, Field(...,title='Country', example='Pakistan')]
    Item : Annotated[Literal['Maize', 'Potatoes', 'Rice, paddy','Sorghum', 'Soybeans', 'Wheat', 'Cassava', 'Sweet potatoes', 'Plantains and others', 'Yams'], Field(..., title='Crop', example='Maize')]
    Year : Annotated[int, Field(..., gt=1000, title='Year', example=2024)]
    average_rain_fall_mm_per_year : Annotated[float, Field(..., gt=0, title='Average Rainfall', example=758.0)]
    pesticides_tonnes : Annotated[float, Field(..., gt=0, title='Pesticides Tonnes', example=827.45)]
    avg_temp : Annotated[float, Field(..., gt=0, title='Average Temperature', example=26.98)]

@app.post("/yield_predict")
def predict_yield(data: UserInput):
    # Build DataFrame with the same column names your pipeline was trained on
    X = pd.DataFrame([{
        "Area": data.Area,
        "Item": data.Item,
        "Year": data.Year,
        "average_rain_fall_mm_per_year": data.average_rain_fall_mm_per_year,
        "pesticides_tonnes": data.pesticides_tonnes,
        "avg_temp": data.avg_temp
    }])
    predict = model.predict(X)
    return JSONResponse(status_code=200, content={"hg/ha_yield": predict[0]})
