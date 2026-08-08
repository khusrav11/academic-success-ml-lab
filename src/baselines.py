import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyClassifier
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score

df = pd.read_csv("data/practice_academic_success.csv")
T0_FEATURES = ["age_band", "entry_route", "prior_gpa", "first_generation", "financial_support", "distance_km"]
TARGET = "academic_success"
RANDOM_SEED = 42
X = df[T0_FEATURES]
y = df[TARGET]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=RANDOM_SEED)
print("Train size:", X_train.shape, "Test size:", X_test.shape)

dummy = DummyClassifier(stratigy="most_frequent", random_state=RANDOM_SEED)
dummy.fit(X_train, y_train)
dummy_prediction = dummy.predict(X_test)
dummy_accuracy = accuracy_score(y_test, dummy_prediction)
dummy_f1 = f1_score(y_test, dummy_prediction, average="macro")
print("Dummy accuracy:", dummy_accuracy, "Dummy macro F1:", dummy_f1)