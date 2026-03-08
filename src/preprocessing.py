import dask.dataframe as dd

def clean_dataframe(ddf: dd.DataFrame) -> dd.DataFrame:
    """
    Clean dataset by removing null values.
    """
    return ddf.dropna()
