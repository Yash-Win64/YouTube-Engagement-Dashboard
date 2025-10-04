from xgboost import XGBClassifier
from sklearn.linear_model import LogisticRegression

def get_xgb_model(random_state=42):
    return XGBClassifier(n_estimators=100, max_depth=4, learning_rate=0.1,
                         use_label_encoder=False, eval_metric='logloss',
                         random_state=random_state)

def get_logistic_model():
    return LogisticRegression(max_iter=1000, class_weight='balanced')
