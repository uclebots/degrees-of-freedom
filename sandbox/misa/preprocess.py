import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer

_SPACE = " "
_HASH = "#"
_MENTION_START = "@"
_WORD_ENDS = (_SPACE, _HASH)
_LANGUAGE = "spanish"
_PUNCTUATION = (_HASH, ",", ".", ":", ";", "¿", "?", "!", "¡", "-", "_")


nltk.download('stopwords')

class MentionsRemover:
    def run(self, text: str) -> str:
        """
        Removes mentions from the given text.

        Args:
            text (str): The input text containing mentions.

        Returns:
            str: The text with mentions removed.
        """
        res = ""
        mention = 0
        for char in text:
            if mention:
                mention += 1
            if char == _MENTION_START:
                mention = 1
            if mention>1 and char in _WORD_ENDS:
                mention = 0
            if not mention:
                res += char
        return res.strip()
    
class StopWordsRemover:
    def __init__(self):
        self.stop_words = set(stopwords.words(_LANGUAGE))-set(["no", "ni", "sin"])

    def run(self, text):
        tokens = word_tokenize(text)
        filtered_tokens = [word for word in tokens if word.lower() not in self.stop_words]
        return " ".join(filtered_tokens)
    
class PunctuationRemover:
        
    def run(self, text):
        res = []
        for c in text:
            if c not in _PUNCTUATION:
                res.append(c)
        return "".join(res)
                
    
class WordStemmer:
    def __init__(self):
        self.stemmer = SnowballStemmer(_LANGUAGE)
        
    def run(self, text):
        tokens = word_tokenize(text)
        return " ".join([self.stemmer.stem(word) for word in tokens])
                