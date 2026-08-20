## Transfer to open data: findings

### Setup
UCI ID 697 (Predict Students' Dropout and Academic Success), DOI: https://doi.org/10.24432/C5MC89, license CC BY 4.0. 4424 students, target `Target`: Dropout / Enrolled / Graduate.

### Prediction before running
I expect T1 to beat the dummy baseline, since first-semester academic performance should be predictive of the outcome. Since this is a 3-class problem, I expect "Enrolled" (the in-between class) to have the lowest recall hardest to separate from both Dropout and Graduate.

### Results
- Dummy: macro F1 = 0.222
- Logistic Regression (T1): macro F1 = 0.612
- Per-class recall: Dropout 0.746, Enrolled 0.176, Graduate 0.928

T1 is roughly 2.8x better than dummy (macro F1 0.612 vs. 0.222). Graduate is predicted best, Dropout okay, Enrolled poorly — matches my prediction.

### What changed vs. practice study
Target has 3 classes instead of 2 so I used macro F1 / per-class recall instead of accuracy / ROC-AUC (accuracy would hide problems with minority classes). T1 here is built from first-semester curricular units (grades, approved units) instead of week-4 behavioral/LMS signals since this dataset has no behavioral data, T0 uses demographic/admission info instead.

### Interpretation
Confusion matrix (rows = actual, columns = predicted):

| actual \ predicted | Dropout | Enrolled | Graduate |
|---|---|---|---|
| Dropout | 212 | 23 | 49 |
| Enrolled | 52 | 28 | 79 |
| Graduate | 18 | 14 | 410 |

Enrolled is confused mostly with Graduate (79 cases). This makes sense: "Enrolled" is a mid-process snapshot not a final outcome so still-studying student's first-semester profile can look like either a future graduate or a future dropout it has no distinct pattern of its own.

### Conclusion
Both predictions were confirmed: T1 clearly beats the baseline and Enrolled has the lowest recall. This suggests the T0/T1 approach transfers well across datasets (better features beat a naive baseline) but also reveals a new limitation not seen in the binary practice setup: intermediate/transition classes are much harder to predict than clear final outcomes regardless of feature quality.