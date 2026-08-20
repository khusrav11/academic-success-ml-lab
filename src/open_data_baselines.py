import pandas as pd
from ucimlrepo import fetch_ucirepo
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.metrics import f1_score, recall_score, confusion_matrix

from src.config import (RANDOM_SEED, TARGET_OPEN_DATA, T1_FEATURES_OPEN_DATA, validate_open_data_columns)

dataset = fetch_ucirepo(id=697)
X_full = dataset.data.features
y = dataset.data.targets[TARGET_OPEN_DATA]

validate_open_data_columns(X_full.columns)

X = X_full[T1_FEATURES_OPEN_DATA]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=RANDOM_SEED)

numeric_transformer = Pipeline(steps=[("imputer", SimpleImputer(strategy="median")), ("scaler", StandardScaler())])

preprocessor = ColumnTransformer(transformers=[("num", numeric_transformer, T1_FEATURES_OPEN_DATA)])

dummy = DummyClassifier(strategy="most_frequent", random_state=RANDOM_SEED)
dummy.fit(X_train, y_train)
dummy_pred = dummy.predict(X_test)

logreg_pipeline = Pipeline(steps=[("preprocessor", preprocessor), ("classifier", LogisticRegression(random_state=RANDOM_SEED, max_iter=2000))])
logreg_pipeline.fit(X_train, y_train)
logreg_pred = logreg_pipeline.predict(X_test)

labels = sorted(y.unique())

print("Dummy:")
print("Macro F1:", f1_score(y_test, dummy_pred, average="macro"))
print("Per-class recall:", dict(zip(labels, recall_score(y_test, dummy_pred, average=None, labels=labels, zero_division=0))))

print("\nLogistic Regression (T1):")
print("Macro F1:", f1_score(y_test, logreg_pred, average="macro"))
print("Per-class recall:", dict(zip(labels, recall_score(y_test, logreg_pred, average=None, labels=labels, zero_division=0))))
print("Confusion matrix (rows=actual, cols=predicted), labels:", labels)
print(confusion_matrix(y_test, logreg_pred, labels=labels))

results = pd.DataFrame([
    {"model": "dummy", "macro_f1": f1_score(y_test, dummy_pred, average="macro")},
    {"model": "logistic_T1", "macro_f1": f1_score(y_test, logreg_pred, average="macro")},
])
results.to_csv("results/open_data_results.csv", index=False)
print(results)