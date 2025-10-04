import sys, os
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)


import streamlit as st, pandas as pd, numpy as np, joblib, shap, matplotlib.pyplot as plt
from src.preprocess import NUMERIC_COLS

st.set_page_config(page_title='Diabetes Risk Demo', layout='centered')

@st.cache_resource
def load_artifact(path='models/xgb_model.joblib'):
    obj = joblib.load(path)
    return obj['model'], obj['preprocessor'], obj['features']

model, preprocessor, feature_cols = load_artifact()

st.title('Diabetes Risk Predictor — Demo')
st.write('Enter patient data. This model is a demo — not for clinical use.')

with st.form('input_form'):
    inputs = {}
    for c in feature_cols:
        val = st.number_input(c, value=1.0)
        inputs[c] = val
    submitted = st.form_submit_button('Predict')

if submitted:
    X_row = pd.DataFrame([inputs])
    zero_invalid = ['Glucose','BloodPressure','SkinThickness','Insulin','BMI']
    for c in zero_invalid:
        if X_row.at[0,c] == 0: X_row.at[0,c] = np.nan
    Xp = preprocessor.transform(X_row[feature_cols])
    prob = model.predict_proba(Xp)[0,1]
    st.metric('Predicted diabetes risk', f"{prob:.3f}")
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(Xp)
    feat_imp = sorted(zip(feature_cols, shap_values[0].tolist()), key=lambda x: abs(x[1]), reverse=True)
    fig, ax = plt.subplots(); ax.barh([f for f,_ in feat_imp], [v for _,v in feat_imp])
    st.pyplot(fig)
