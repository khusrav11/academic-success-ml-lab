import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyClassifier
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

df = pd.read_csv("data/practice_academic_success.csv")

T0_FEATURES = ["age_band", "entry_route", "prior_gpa", "first_generation", "financial_support", "distance_km"]
T1_FEATURES = T0_FEATURES + ["week4_attendance_rate", "week4_lms_logins", "assignment1_score", "support_sessions_week4"]

TARGET = "academic_success"
RANDOM_SEED = 42

X = df[T0_FEATURES]
X_t1 = df[T1_FEATURES]
y = df[TARGET]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=RANDOM_SEED)
X_train_t1, X_test_t1, y_train_t1, y_test_t1 = train_test_split(X_t1, y, test_size=0.2, stratify=y, random_state=RANDOM_SEED)
print("Train size:", X_train.shape, "Test size:", X_test.shape)

dummy = DummyClassifier(strategy="most_frequent", random_state=RANDOM_SEED)
dummy.fit(X_train, y_train)
dummy_prediction = dummy.predict(X_test)
dummy_accuracy = accuracy_score(y_test, dummy_prediction)
dummy_f1 = f1_score(y_test, dummy_prediction, average="macro")
print("Dummy accuracy:", dummy_accuracy, "Dummy macro F1:", dummy_f1)

numeric_features = ["prior_gpa", "first_generation", "financial_support", "distance_km"]
numeric_features_t1 = numeric_features + ["week4_attendance_rate", "week4_lms_logins", "assignment1_score", "support_sessions_week4"]

categorical_features = ["age_band", "entry_route"]

numeric_transformer = Pipeline(steps=[("imputer", SimpleImputer(strategy="median")), ("scaler", StandardScaler())])
categorical_transformer = Pipeline(steps=[("imputer", SimpleImputer(strategy="most_frequent")), ("onehot", OneHotEncoder(handle_unknown="ignore"))])

preprocessor = ColumnTransformer(transformers=[("num", numeric_transformer, numeric_features), ("cat", categorical_transformer, categorical_features)])
preprocessor_t1 = ColumnTransformer(transformers=[("num", numeric_transformer, numeric_features_t1), ("cat", categorical_transformer, categorical_features)])

logreg_pipeline = Pipeline(steps=[("preprocessor", preprocessor), ("classifier", LogisticRegression(random_state=RANDOM_SEED, max_iter=1000))])
logreg_pipeline_t1 = Pipeline(steps=[("preprocessor", preprocessor_t1), ("classifier", LogisticRegression(random_state=RANDOM_SEED, max_iter=1000))])

logreg_pipeline.fit(X_train, y_train)
logreg_pipeline_t1.fit(X_train_t1, y_train_t1)

logreg_pred = logreg_pipeline.predict(X_test)
logreg_proba = logreg_pipeline.predict_proba(X_test)[:, 1]

logreg_accuracy = accuracy_score(y_test, logreg_pred)
logreg_f1 = f1_score(y_test, logreg_pred, average="macro")
logreg_auc = roc_auc_score(y_test, logreg_proba)
print("Logistic accuracy:", logreg_accuracy, "F1:", logreg_f1, "AUC:", logreg_auc)

dummy_auc = roc_auc_score(y_test, dummy.predict_proba(X_test)[:, 1])

results = pd.DataFrame([
    {"model": "dummy", "accuracy": dummy_accuracy, "macro_f1": dummy_f1, "roc_auc": dummy_auc},
    {"model": "logistic_T0", "accuracy": logreg_accuracy, "macro_f1": logreg_f1, "roc_auc": logreg_auc}
])
results.to_csv("results/baselines.csv", index=False)
print(results)

t1_pred = logreg_pipeline_t1.predict(X_test_t1)
t1_proba = logreg_pipeline_t1.predict_proba(X_test_t1)[:, 1]

t1_accuracy = accuracy_score(y_test_t1, t1_pred)
t1_f1 = f1_score(y_test_t1, t1_pred, average="macro")
t1_auc = roc_auc_score(y_test_t1, t1_proba)
print("T1 accuracy:", t1_accuracy, "F1:", t1_f1, "AUC:", t1_auc)

print("T0 confusion matrix:")
print(confusion_matrix(y_test, logreg_pred))
print("T1 confusion matrix:")
print(confusion_matrix(y_test_t1, t1_pred))

comparison = pd.DataFrame([
    {"model": "logistic_T0", "accuracy": logreg_accuracy, "macro_f1": logreg_f1, "roc_auc": logreg_auc},
    {"model": "logistic_T1", "accuracy": t1_accuracy, "macro_f1": t1_f1, "roc_auc": t1_auc},
])
comparison.to_csv("results/t0_vs_t1.csv", index=False)
print(comparison)

errors_df = X_test_t1.copy()
errors_df["actual"] = y_test_t1.values
errors_df["t0_pred"] = logreg_pred
errors_df["t1_pred"] = t1_pred

wrong_t1 = errors_df[errors_df["actual"] != errors_df["t1_pred"]]
print("Number of T1 wrong predictions:", len(wrong_t1))
print(wrong_t1.head(10))

fixed_by_t1 = errors_df[(errors_df["actual"] != errors_df["t0_pred"]) & (errors_df["actual"] == errors_df["t1_pred"])]
print("Errors fixed by adding week-4 features:", len(fixed_by_t1))