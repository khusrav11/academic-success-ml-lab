import os
import subprocess
import joblib

from src.config import MODEL_PATH

def test_train_creates_model_file():
    subprocess.run(["python3", "-m", "src.train"], check=True)
    assert os.path.exists(MODEL_PATH)

def test_pipeline_predicts_probabilities():
    pipeline = joblib.load(MODEL_PATH)
    assert hasattr(pipeline, "predict_proba")

def test_evaluate_runs_without_error():
    result = subprocess.run(["python3", "-m", "src.evaluate"], capture_output=True, text=True)
    assert result.returncode == 0
    assert "Accuracy" in result.stdout