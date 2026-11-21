from misa.preprocess import MentionsRemover

TEXT_WITH_MENTIONS = "@usuario La sociedad les dio la espalda en 2019 y no ayuda mostrarse como una fuerza intentando dar un golpe, Pato."
TEXT_WITHOUT_MENTIONS = "La sociedad les dio la espalda en 2019 y no ayuda mostrarse como una fuerza intentando dar un golpe, Pato."

def test_mentions_removed() -> None:
    assert MentionsRemover().run(TEXT_WITH_MENTIONS) == TEXT_WITHOUT_MENTIONS