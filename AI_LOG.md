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

## 15-08-2026 — Mission 09
- Task attempted: built app.py with a Streamlit form for T1 inputs, connected the saved pipeline, added uncertainty/responsible-use messaging, and handled invalid inputs.
- Assistance requested: asked Claude for the Streamlit form structure, prediction code and try/except error handling skeleton.
- What was accepted, changed or rejected: used Claude's code structure as-is, including the responsible-use warning wording, since it matched exactly what the mission card required (prediction supports human review, not a final decision).
- How the result was verified: ran the app with streamlit run app.py, tested one example input and confirmed the probability matched what src/evaluate.py would produce for the same inputs; tested an out-of-range input to confirm the app shows an error instead of crashing.

## 2026-08-20 — Mission 11
- Task attempted: loaded UCI dataset 697, defined T0/T1 feature partitions with column validation, compared dummy and logistic regression baselines on the 3-class target, wrote a transfer note.
- Assistance requested: asked Claude for the data loader structure, general T0/T1 partitioning logic (which I applied myself to the actual UCI column names) and some part of modelling pipeline structure adapted for multi-class metrics.
- What was accepted, changed or rejected: used the code structure as-is; wrote the T0/T1 column lists and the transfer note myself based on my own review of the dataset's actual columns and results.
- How the result was verified: ran validate_open_data_columns() to confirm no missing/extra columns; compared the "Enrolled" recall result (0.176, weakest of the 3 classes) against my prediction in the issue, which anticipated this outcome.