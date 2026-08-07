# Data Audit - Mission 02

## What I found

1. The dataset has the rows and columns shown by `df.shape` when running `src/data_audit.py` with one target column `academic_success` (0/1).
2. The target is imbalanced: value_counts() shows more students in one class than the other, confirming my prediction before running the script.
3. Missing values appear in `prior_gpa` (28), `distance_km` (16) and `assignment1_score` (40) all other columns are complete.
4. Unlike my prediction the dataset is **not** free of duplicates - `duplicated(subset="student_id")` found 8 duplicate student_id rows which will need to be handled before any modeling in later missions.