# AI Assistance Log

## 12-08-2026 - Mission 06

- Task attempted: trained a deliberately leaked model, compared it with the valid T1 model, built a function to reject forbidden end-of-term columns, wrote a pytest test for it and explained why the leaked accuracy is invalid.
- Assistance requested: asked Claude for the leaked model code structure, the feature_guard.py function skeleton and the pytest test skeleton.
- What was accepted, changed or rejected: used Claude's code structure as-is, but wrote the leakage explanation myself in my own words so I could genuinely explain it without notes.
- How the result was verified: ran pytest (2 passed) and manually confirmed check_no_forbidden_columns raises a ValueError when a forbidden column is passed in.