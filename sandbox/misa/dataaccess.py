import pandas as pd
from pathlib import Path

class CommentsDataSet:
    def __init__(self, path: str):
        parquet_files = Path(path).glob("*.parquet")
        self._data_frames = {f.stem: Comments(pd.read_parquet(f)) for f in parquet_files}

    @property            
    def datasets(self):
        return self._data_frames
    
    def dataset(self, name=None):
        if name:
            return Comments(self._data_frames[name])
        return Comments(pd.concat(self._data_frames.values))
    
class Comments:
    def __init__(self, dataframe: pd.DataFrame):
        self._dataframe = dataframe
        
    def threads(self):
        return tuple(self._dataframe["title"].unique().tolist())
    
    def raw(self):
        return self._dataframe