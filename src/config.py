RANDOM_SEED = 42
TARGET = "academic_success"

T0_FEATURES = ["age_band", "entry_route", "prior_gpa", "first_generation", "financial_support", "distance_km"]
T1_FEATURES = T0_FEATURES + ["week4_attendance_rate", "week4_lms_logins", "assignment1_score", "support_sessions_week4"]

NUMERIC_FEATURES_T1 = ["prior_gpa", "first_generation", "financial_support", "distance_km", "week4_attendance_rate", "week4_lms_logins", "assignment1_score", "support_sessions_week4"]

CATEGORICAL_FEATURES = ["age_band", "entry_route"]

FORBIDDEN_COLUMNS = ["final_attendance_rate", "final_exam_score", "credits_completed", "student_id"]

DATA_PATH = "data/practice_academic_success.csv"
MODEL_PATH = "models/t1_pipeline.joblib"

TARGET_OPEN_DATA = "Target"  # Dropout / Enrolled / Graduate

T0_FEATURES_OPEN_DATA = [
    "Marital Status",
    "Application mode",
    "Application order",
    "Course",
    "Daytime/evening attendance",
    "Previous qualification",
    "Previous qualification (grade)",
    "Nacionality",
    "Mother's qualification",
    "Father's qualification",
    "Mother's occupation",
    "Father's occupation",
    "Admission grade",
    "Displaced",
    "Educational special needs",
    "Debtor",
    "Tuition fees up to date",
    "Gender",
    "Scholarship holder",
    "Age at enrollment",
    "International",
    "Unemployment rate",
    "Inflation rate",
    "GDP",
]

T1_FEATURES_OPEN_DATA = T0_FEATURES_OPEN_DATA + [
    "Curricular units 1st sem (credited)",
    "Curricular units 1st sem (enrolled)",
    "Curricular units 1st sem (evaluations)",
    "Curricular units 1st sem (approved)",
    "Curricular units 1st sem (grade)",
    "Curricular units 1st sem (without evaluations)",
]

FORBIDDEN_COLUMNS_OPEN_DATA = [
    "Curricular units 2nd sem (credited)",
    "Curricular units 2nd sem (enrolled)",
    "Curricular units 2nd sem (evaluations)",
    "Curricular units 2nd sem (approved)",
    "Curricular units 2nd sem (grade)",
    "Curricular units 2nd sem (without evaluations)",
]

DATA_PATH_OPEN_DATA = "data/open_data_academic_success.csv"
MODEL_PATH_OPEN_DATA = "models/t1_pipeline_open_data.joblib"


def validate_open_data_columns(columns):
    columns = list(columns)
    all_known = T0_FEATURES_OPEN_DATA + [c for c in T1_FEATURES_OPEN_DATA if c not in T0_FEATURES_OPEN_DATA] + FORBIDDEN_COLUMNS_OPEN_DATA
    missing = set(columns) - set(all_known)
    extra = set(all_known) - set(columns)
    assert not missing, f"X contains missing columns in the partition: {sorted(missing)}"
    assert not extra, f"There are extra columns in the partition: {sorted(extra)}"
    return True