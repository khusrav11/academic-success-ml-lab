# Reliability and fairness

## Calibration
My T1 model achieves a Brier score of **0.2096**. As predicted (given the balanced target distribution and ROC-AUC of 0.734) the probabilities are reasonably calibrated overall though minor deviations exist across bins.

## Subgroup results
* **first_generation:**
  * Group 1 (n = 52): Recall = 0.6296, FPR = 0.2000
  * Group 0 (n = 110): Recall = 0.6604, FPR = 0.3333
* **age_band:**
  * 25+ (n = 22): Recall = 0.8000, FPR = 0.2500
  * 18–20 (n = 101): Recall = 0.6522, FPR = 0.3455
  * 21–24 (n = 39): Recall = 0.5833, FPR = 0.1333

## Threshold choice
I select **Threshold = 0.7** (flagged_as_at_risk_rate = 0.877 vs. 0.160 at threshold 0.3). Because this tool is designed to offer **support** rather than punishment a conservative success threshold ensures 87.7% of students are flagged for potential assistance prioritizing false alarms (offering extra help) over missing a student who genuinely needs aid.

## Limitation
Small subgroup sizes (e.g., n = 22 for 25+, n = 39 for 21–24) mean these recall and FPR estimates are statistically unreliable.