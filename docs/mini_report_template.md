# TWO-PAGE MINI REPORT | ML LAB

**Title:** Predicting Academic Success at Enrollment and at Week 4

---

## 1. Research question
Can academic success be predicted more effectively at week 4 than at enrollment, using only information available at each checkpoint?

---

## 2. Data and prediction setup
I audited dataset and found 808 student rows and 15 columns, including one target column, `academic_success` (1 = success, 0 = not success; 400 vs. 408 students, roughly balanced). `duplicated(subset="student_id")` I found 8 duplicate `student_id` rows, which were handled before modeling so that no student appears on both sides of the train/test split. Missing values were present in `prior_gpa` (28), `distance_km` (16) and `assignment1_score` (40); all other columns were complete. All models share the same held out test set (n = 81 students, stratified by target).

* **T0 (enrollment-only):** `age_band`, `entry_route`, `prior_gpa`, `first_generation`, `financial_support`, `distance_km`.
* **T1 (enrollment + week 4):** T0 + `week4_attendance_rate`, `week4_lms_logins`, `assignment1_score`, `support_sessions_week4`.

**Prediction time:** end of week 4. `student_id` is used only as a row identifier, never as a predictor. `final_attendance_rate`, `final_exam_score` and `credits_completed` are excluded from both T0 and T1 because they are only known at the end of the term.

---

## 3. Methods
I compared two models: a dummy baseline that predicts the majority class and a logistic-regression pipeline with imputation and encoding. For the T0 vs. T1 comparison, I kept the same train/test split, target, and model type. The only change was adding week-4 features, so the performance difference reflects the extra information available at T1.

---

## 4. Results

| Model | Feature checkpoint | Macro F1 | ROC-AUC | Brier score |
| :--- | :--- | :---: | :---: | :---: |
| Dummy baseline | (majority class) | 0.336 | 0.500 | - |
| Logistic regression | T0 - enrollment only | 0.654 | 0.673 | - |
| Logistic regression | T1 - enrollment + week 4 | 0.679 | 0.734 | 0.2096 |

### Target balance (academic_success)
![Target balance: academic_success](target_balance.png)
---

## 5. Error and group analysis
I found two main error patterns. First, adding week-4 signals corrected 18 of the T0 errors, showing that early behavioural data provides useful information beyond enrollment data. However, 52 errors remained in T1, mostly false negatives for students with `assignment1_score` between 50 and 70. This mid-range score was the most difficult case for the model to classify. 

I found subgroup (`age_band`, without stereotyping): the 21–24 group had lower recall (0.583, n = 39) than the 18–20 group (0.652, n = 101) but also a lower false-positive rate (0.133 vs. 0.345). With group sizes this small (22–101 students), these recall/FPR estimates are not statistically reliable and should not be read as a stable property of any age group.

---

## 6. Leakage and validity
I also trained a deliberately invalid model using `final_attendance_rate`, `final_exam_score`, and `credits_completed`, which are only available at the end of the term. It achieved perfect accuracy, macro F1, and ROC-AUC of 1.0, but this result is misleading. In particular, `credits_completed` is almost a direct representation of the final outcome. This shows that a model can perform perfectly but still be invalid if it uses information that would not be available when the prediction is actually made.

---

## 7. Conclusion and limitations
My results show that week-4 data (T1) predicts academic success better than enrollment data alone (T0). ROC-AUC increased from 0.673 to 0.734, while accuracy improved from 0.654 to 0.679. This supports my research question, although the improvement is modest. The T1 model still misclassified 26 of 81 students (about 32%), so it should not replace human judgment. Because of the small subgroup samples and moderate calibration (Brier = 0.2096), I would use the model to help prioritize outreach and support, rather than make final decisions about students.

---

## Reproducibility line
* **Repository commit/tag:** `draft academic success modelling report`
* **Command used:** `python -m src.train, python -m src.evaluate, python3 -m pytest -v`
* **Random seed:** `42`

> **Writing rule:** Report evidence, not effort. Do not say “the model is good”; state the metric, test set and limitation.