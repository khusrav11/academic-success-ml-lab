import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score

from src.config import RANDOM_SEED, TARGET, T1_FEATURES, DATA_PATH, MODEL_PATH

df = pd.read_csv(DATA_PATH)
X = df[T1_FEATURES]
y = df[TARGET]

_, X_test, _, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=RANDOM_SEED)

pipeline = joblib.load(MODEL_PATH)
pred = pipeline.predict(X_test)
proba = pipeline.predict_proba(X_test)[:, 1]

print("Accuracy:", accuracy_score(y_test, pred))
print("Macro F1:", f1_score(y_test, pred, average="macro"))
print("ROC-AUC:", roc_auc_score(y_test, proba))