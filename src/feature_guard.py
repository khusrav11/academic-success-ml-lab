FORBIDDEN_COLUMNS = [
  "final_attendance_rate",
  "final_exam_score",
  "credits_completed",
  "student_id",
]

def check_no_forbidden_columns(feature_list):
  # raise error if any forbidden end-of-term column is present
  leaked = [col for col in feature_list if col in FORBIDDEN_COLUMNS]
  if leaked:
    raise ValueError(f"Forbidden columns detected: {leaked}")
  return True