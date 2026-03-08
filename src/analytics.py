import pandas as pd
import dask.dataframe as dd

def compute_summary(ddf: dd.DataFrame) -> pd.DataFrame:
    """
    Compute simple dataset statistics.
    """
    result = {
        "row_count": ddf.shape[0].compute(),
        "column_count": len(ddf.columns),
    }
    return pd.DataFrame([result])
