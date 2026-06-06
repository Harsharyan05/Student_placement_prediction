from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI()

model = joblib.load("placement_model.pkl")
feature_names = joblib.load("feature_names.pkl")


class StudentData(BaseModel):
    gender: str
    ssc_p: float
    ssc_b: str
    hsc_p: float
    hsc_b: str
    hsc_s: str
    degree_p: float
    degree_t: str
    workex: str
    etest_p: float
    specialisation: str
    mba_p: float


@app.get("/")
def home():
    return {"message": "Student Placement Prediction API Running"}


@app.post("/predict")
def predict(data: StudentData):

    input_dict = data.dict()

    df = pd.DataFrame([input_dict])

    categorical_cols = [
        "gender",
        "ssc_b",
        "hsc_b",
        "hsc_s",
        "degree_t",
        "workex",
        "specialisation"
    ]

    df = pd.get_dummies(df, columns=categorical_cols)

    for col in feature_names:
        if col not in df.columns:
            df[col] = 0

    df = df[feature_names]

    prediction = model.predict(df)[0]

    result = "Placed" if prediction == 1 else "Not Placed"

    return {
        "prediction": result
    }