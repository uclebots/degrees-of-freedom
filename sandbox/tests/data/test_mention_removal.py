import pytest

from misa.constants import DATABASE_PATH
from misa.dataaccess import CommentsDataSet
from misa.preprocess import MentionsRemover

_MENTION = "@usuario"
@pytest.mark.parametrize("dataset_name", ["dev-00000-of-00001", "test-00000-of-00001", "train-00000-of-00001"])
def test_dataset(dataset_name):
    datasets = CommentsDataSet(DATABASE_PATH).datasets
    df = datasets[dataset_name].raw()
    remover = MentionsRemover()
    mention_removed = [remover.run(text) for text in df["text"]]
    mention_removed_errors = [text for text in mention_removed if _MENTION in text]
    for error in mention_removed_errors:
        print(error)
    assert all(_MENTION not in text for text in mention_removed)