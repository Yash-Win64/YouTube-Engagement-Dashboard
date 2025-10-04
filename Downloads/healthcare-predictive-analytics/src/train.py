import argparse, joblib, os
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, precision_recall_curve, auc
from src.preprocess import load_data, preprocess, NUMERIC_COLS
from src.model import get_xgb_model, get_logistic_model

def evaluate_model(model, X_test, y_test):
    probs = model.predict_proba(X_test)[:,1]
    roc = roc_auc_score(y_test, probs)
    precision, recall, _ = precision_recall_curve(y_test, probs)
    pr_auc = auc(recall, precision)
    return {'roc_auc': roc, 'pr_auc': pr_auc}

def main(data_path, output_path):
    df = load_data(data_path)
    X_proc, y, preprocessor = preprocess(df)
    X_train, X_test, y_train, y_test = train_test_split(X_proc, y, test_size=0.2, stratify=y, random_state=42)
    xgb = get_xgb_model(); xgb.fit(X_train, y_train)
    print('XGB metrics:', evaluate_model(xgb, X_test, y_test))
    log = get_logistic_model(); log.fit(X_train, y_train)
    print('Logistic metrics:', evaluate_model(log, X_test, y_test))
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    joblib.dump({'model': xgb, 'preprocessor': preprocessor, 'features': NUMERIC_COLS}, output_path)
    print('Saved model to', output_path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data-path', required=True)
    parser.add_argument('--output', dest='output_path', default='models/xgb_model.joblib')
    args = parser.parse_args()
    main(args.data_path, args.output_path)
