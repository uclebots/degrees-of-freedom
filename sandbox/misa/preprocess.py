_SPACE = " "
_MENTION_START = "@"

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
        prev_char = _SPACE
        mention = 0
        for char in text:
            if mention:
                mention += 1
            if char == _MENTION_START and prev_char == _SPACE:
                mention = 1
            if mention>1 and prev_char == _SPACE:
                mention = 0
            if not mention:
                res += char
            prev_char = char
        return res