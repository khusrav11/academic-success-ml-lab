# AI Assistance Log

## 12-08-2026 - Mission 06

- Task attempted: trained a deliberately leaked model, compared it with the valid T1 model, built a function to reject forbidden end-of-term columns, wrote a pytest test for it and explained why the leaked accuracy is invalid.
- Assistance requested: asked Claude for the leaked model code structure, the feature_guard.py function skeleton and the pytest test skeleton.
- What was accepted, changed or rejected: used Claude's code structure as-is, but wrote the leakage explanation myself in my own words so I could genuinely explain it without notes.
- How the result was verified: ran pytest (2 passed) and manually confirmed check_no_forbidden_columns raises a ValueError when a forbidden column is passed in.

## 12-08-2026 - Mission 07

- Task attempted: Evaluated model calibration (Brier score, calibration table), subgroup performance (recall/FPR by `first_generation` and `age_band`), tested thresholds (0.3, 0.5, 0.7), and drafted fairness analysis (threshold justification and sample-size limitations).
- Assistance requested: Asked Claude for code skeletons (`group_metrics` function, threshold-comparison loop) and a logic review of my draft.
- What was accepted, changed or rejected: Used Claude's code structure directly. Wrote all interpretations myself, fixing a logic error in my threshold justification after realizing I'd confused class-1 recall with `flagged_as_at_risk_rate`.
- How the result was verified: Checked subgroup $n$-counts against total test size for reliability, and confirmed the threshold choice matched the actual proportion of students flagged for support.