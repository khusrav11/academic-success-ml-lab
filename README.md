# Academic Success ML Lab

**Author:** Ziyoboev Khusravkhon

Start with `docs/00_START_HERE.docx`. Complete Missions 01-11 in order.

## Research question

How well can academic success be predicted using only information available by an early checkpoint?

## Data sequence

1. Missions 01-10 use the included synthetic practice dataset.
2. Mission 11 repeats the study on the UCI **Predict Students' Dropout and Academic Success** dataset.
3. OULAD is listed as an optional advanced extension in `docs/00_OPEN_DATASETS.docx`.

## Project folders

- `data/` practice data and dataset notes
- `docs/` mission cards and templates
- `src/` reusable Python code
- `tests/` automated tests
- `results/` saved experiment outputs

Do not place private student data, secrets or large model files in the repository.

## Running the pipeline

Install dependencies:
```bash
pip install -r requirements.txt
```

Train the model:
```bash
python3 -m src.train
```

Evaluate the trained model:
```bash
python3 -m src.evaluate
```

Run the test suite:
```bash
python3 -m pytest -v
```

How to run the web app:
```bash
python -m streamlit run app.py
```