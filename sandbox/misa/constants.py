DATABASE_PATH = "../../Conicet_digital_11336_235509/contextualized_hate_speech_DATA"
COMMENT_COLUMNS = ["id", "text", "HATEFUL", "CALLS", "WOMEN", "LGBTI", "RACISM", "CLASS", "POLITICS", "DISABLED", "APPEARANCE", "CRIMINAL"]
POST_COLUMNS = ["title", "context_tweet", "body"]
COLUMNS = POST_COLUMNS + COMMENT_COLUMNS