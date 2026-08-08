import pandas as pd
from sklearn.model_selection import train_test_split
df = pd.read_csv("data/practice_academic_success.csv")
T0_FEATURES = ["age_band", "entry_route", "prior_gpa", "first_generation", "financial_support", "distance_km"]
TARGET = "academic_success"
RANDOM_SEED = 42
X = df[T0_FEATURES]
y = df[TARGET]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=RANDOM_SEED)
print("Train size:", X_train.shape, "Test size:", X_test.shape)