import pytest
from src.feature_guard import check_no_forbidden_columns


def test_valid_features_pass():
    assert check_no_forbidden_columns(["prior_gpa", "age_band"]) is True


def test_forbidden_column_is_rejected():
    with pytest.raises(ValueError):
        check_no_forbidden_columns(["prior_gpa", "final_exam_score"])