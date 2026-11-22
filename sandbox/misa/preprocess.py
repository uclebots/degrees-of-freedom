_SPACE = " "
_HASH = "#"
_MENTION_START = "@"
_WORD_ENDS = (_SPACE, _HASH)

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