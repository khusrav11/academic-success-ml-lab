from ucimlrepo import fetch_ucirepo

dataset = fetch_ucirepo(id=697)

X = dataset.data.features
y = dataset.data.targets

print("Rows and columns:", X.shape)
print("Target distribution:")
print(y.value_counts())
print("\nВсе колонки:")
for i, col in enumerate(X.columns.tolist()):
    print(i, repr(col))

from src.config import T1_FEATURES_OPEN_DATA, validate_open_data_columns

validate_open_data_columns(X.columns)
X_model = X[T1_FEATURES_OPEN_DATA]

print("X_model shape:", X_model.shape)
print("Columns in X_model:", X_model.columns.tolist())