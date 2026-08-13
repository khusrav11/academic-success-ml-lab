RANDOM_SEED = 42
TARGET = "academic_success"

T0_FEATURES = ["age_band", "entry_route", "prior_gpa", "first_generation", "financial_support", "distance_km"]
T1_FEATURES = T0_FEATURES + ["week4_attendance_rate", "week4_lms_logins", "assignment1_score", "support_sessions_week4"]

NUMERIC_FEATURES_T1 = ["prior_gpa", "first_generation", "financial_support", "distance_km", "week4_attendance_rate", "week4_lms_logins", "assignment1_score", "support_sessions_week4"]

CATEGORICAL_FEATURES = ["age_band", "entry_route"]

FORBIDDEN_COLUMNS = ["final_attendance_rate", "final_exam_score", "credits_completed", "student_id"]

DATA_PATH = "data/practice_academic_success.csv"
MODEL_PATH = "models/t1_pipeline.joblib"