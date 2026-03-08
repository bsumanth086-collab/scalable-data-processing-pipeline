import dask.dataframe as dd

def load_parquet(path: str) -> dd.DataFrame:
    """
    Load large Parquet dataset using Dask.
    """
    return dd.read_parquet(path, engine="pyarrow")
