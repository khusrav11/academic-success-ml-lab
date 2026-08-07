# Modelling Plan

## Target, prediction time, unit of analysis
- **Target:** `academic_success` (1 = success, 0 = not success)
- **Checkpoint:** end of week 4 — no features from after this point
- **Unit of analysis:** one row per student (`student_id` not used as a predictor)

## T0 — enrollment-only
Available at enrollment, before the course starts:
`age_band`, `entry_route`, `prior_gpa`, `first_generation`, `financial_support`, `distance_km`

## T1 — enrollment + week-4
Everything in T0, plus signals available by the end of week 4:
T0 + `week4_attendance_rate`, `week4_lms_logins`, `assignment1_score`, `support_sessions_week4`

## Forbidden end-of-term columns
These columns are only known at the end of the term, after the outcome is already decided. Using them would leak future information into a prediction that is supposed to happen at week 4:
- `final_attendance_rate`, `final_exam_score`, `credits_completed` — only known after the term ends, so they leak the outcome
- `student_id` — identifier, not a predictor.

## Hypothesis:
I expect T1 will outperform T0 since early behavioural signals (attendance, logins, first assignment, support use) are more predictive than enrollment data alone.