from pytest import fixture

import pandas as pd
from pathlib import Path

from misa.dataaccess import CommentsDataSet

_PARQUET_FILENAME = "./test/dev.parquet"

@fixture
def sample_dataframe():
    return pd.DataFrame(
        [(1, "title", "text", "context_tweet", 0, "body")], 
        columns=("id", "title", "text", "context_tweet", "HATEFUL", "body"))

def test_constructor(mocker, sample_dataframe):
    Path("./test").mkdir(exist_ok=True)        
    with open(_PARQUET_FILENAME, "wb") as f:        
        sample_dataframe.to_parquet(f, index=False)
    with open(_PARQUET_FILENAME, "rb") as f:
        f.stem = "dev"

        mocker.patch("misa.dataaccess.Path.glob", return_value=[f])
        assert CommentsDataSet("./test").data_frames["dev"].equals(sample_dataframe)
