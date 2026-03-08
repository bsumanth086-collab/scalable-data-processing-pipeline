from src.loader import load_parquet
import pytest

def test_invalid_path():
    with pytest.raises(Exception):
        load_parquet("invalid_path")
