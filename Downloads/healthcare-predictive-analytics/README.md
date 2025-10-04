# Healthcare Predictive Analytics — Diabetes Risk (Streamlit demo)

This repository is an end-to-end project that trains a diabetes risk classifier and exposes a Streamlit web app.

## Quickstart
1. Install dependencies: `pip install -r requirements.txt`
2. Place dataset at `data/raw/pima.csv`
3. Train: `python -m src.train --data-path data/raw/pima.csv --output models/xgb_model.joblib`
4. Run app: `streamlit run app/streamlit_app.py`

**Note:** Demo only. Not for clinical use.
