from dask.distributed import Client
from src.config import DATA_PATH
from src.loader import load_parquet
from src.preprocessing import clean_dataframe
from src.analytics import compute_summary

def main():
    client = Client()

    ddf = load_parquet(DATA_PATH)
    cleaned = clean_dataframe(ddf)

    summary = compute_summary(cleaned)
    print(summary)

if __name__ == "__main__":
    main()
