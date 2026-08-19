from ucimlrepo import fetch_ucirepo

dataset = fetch_ucirepo(id=697)

X = dataset.data.features
y = dataset.data.targets

print("Rows and columns:", X.shape)
print("Target distribution:")
print(y.value_counts())

print("\nDataset citation info:")
print(dataset.metadata.name)
print("DOI:", dataset.metadata.doi if hasattr(dataset.metadata, "doi") else "https://doi.org/10.24432/C5MC89")
print("License: Creative Commons Attribution 4.0 (CC BY 4.0)")
print("Retrieved:", "2026-08-19")
