import pandas as pd
from pathlib import Path

class CommentsDataSet:
    def __init__(self, path: str):
        parquet_files = Path(path).glob("*.parquet")
        self._data_frames = {f.stem: pd.read_parquet(f) for f in parquet_files}

    @property            
    def data_frames(self):
        return self._data_frames