import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

NUMERIC_COLS = ['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age']
TARGET_COL = 'Outcome'

def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

def build_preprocessor():
    return Pipeline([('imputer', SimpleImputer(strategy='median')),
                     ('scaler', StandardScaler())])

def preprocess(df: pd.DataFrame):
    df = df.copy()
    zero_invalid = ['Glucose','BloodPressure','SkinThickness','Insulin','BMI']
    for c in zero_invalid:
        df[c] = df[c].replace(0, np.nan)
    X = df[NUMERIC_COLS]
    y = df[TARGET_COL] if TARGET_COL in df.columns else None
    preprocessor = build_preprocessor()
    X_proc = preprocessor.fit_transform(X)
    return X_proc, y, preprocessor
