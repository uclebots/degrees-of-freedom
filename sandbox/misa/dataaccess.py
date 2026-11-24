import pandas as pd
from pathlib import Path
from .constants import COMMENT_COLUMNS

class CommentsDataSet:
    def __init__(self, path: str):
        parquet_files = Path(path).glob("*.parquet")
        self._data_frames = {f.stem: Comments(pd.read_parquet(f)) for f in parquet_files}

    @property            
    def datasets(self):
        return self._data_frames
    
    def dataset(self, name=None):
        if name:
            return Comments(self._data_frames[name].raw())
        return Comments(pd.concat(v.raw() for v in self._data_frames.values()))
    
class Comments:
    def __init__(self, dataframe: pd.DataFrame):
        self._dataframe = dataframe
        
    def posts(self):
        return [self._post(title) for title in self._dataframe["title"].unique().tolist()]
    
    def raw(self):
        return self._dataframe
    
    def _post(self, title):
        relevant = self._dataframe[self._dataframe["title"] == title]
        return Post(relevant["title"].iloc[0], 
                    relevant["context_tweet"].iloc[0],
                    relevant["body"].iloc[0],
                    relevant[COMMENT_COLUMNS])
    
class Post:
    def __init__(self, title, context_tweet, body, comments):
        self.title = title
        self.context_tweet = context_tweet
        self.body = body
        self.comments = comments
        
    def __eq__(self, other):
        if not isinstance(other, Post):
            return False
        return ((self.title, 
                self.context_tweet, 
                self.body) == (other.title, 
                                   other.context_tweet,
                                   other.body) and
                self.comments.equals(other.comments))
