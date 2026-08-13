import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression

from src.config import (RANDOM_SEED, TARGET, T1_FEATURES, NUMERIC_FEATURES_T1, CATEGORICAL_FEATURES, DATA_PATH, MODEL_PATH)
from src.feature_guard import check_no_forbidden_columns

check_no_forbidden_columns(T1_FEATURES)

df = pd.read_csv(DATA_PATH)
X = df[T1_FEATURES]
y = df[TARGET]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=RANDOM_SEED)

numeric_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("onehot", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer(transformers=[
    ("num", numeric_transformer, NUMERIC_FEATURES_T1),
    ("cat", categorical_transformer, CATEGORICAL_FEATURES)
])

pipeline = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("classifier", LogisticRegression(random_state=RANDOM_SEED, max_iter=1000))
])

pipeline.fit(X_train, y_train)

os.makedirs("models", exist_ok=True)
joblib.dump(pipeline, MODEL_PATH)
print(f"Trained pipeline saved to {MODEL_PATH}")