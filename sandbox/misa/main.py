import argparse

from .constants import DATABASE_PATH
from .dataaccess import CommentsDataSet
from .preprocess import MentionsRemover, PunctuationRemover, StopWordsRemover, WordStemmer
from time import monotonic

_FILTERS = (MentionsRemover, PunctuationRemover, StopWordsRemover, WordStemmer)

def random_comment():
    start = monotonic()    
    data = CommentsDataSet(DATABASE_PATH).dataset().raw().sample(n=1)
    res = {"title": data["title"].iloc[0], 
           "text": data["text"].iloc[0], 
           "context_tweet": data["context_tweet"].iloc[0], 
           "body": data["body"].iloc[0]}
    elapsed = monotonic() - start
    print(f"Elegir un comentario random tomó {elapsed:.3f} segundos.")
    return res
    

def main():
    parser = argparse.ArgumentParser(
        prog="misa", 
        description="""Determina si un comentario corresponde a discurso de odio y muestra cómo lo hace paso a paso.
                    Sin comentario elige uno del conjunto de datos de entrenamiento.""",
        epilog="""Ejemplo: misa "que mal le pega el alcohol" """)
    parser.add_argument("comment", nargs="?", default="", help="Comentario, vacío para elegir uno de los datos de entrenamiento")
    parser.add_argument("--context", default=False, nargs=1)

    args = parser.parse_args()
    
    comment = {"text": args.comment} if args.comment else random_comment()
    
    print(comment.get("text"))
    if args.context:
        print(f"""\n ----------- Título ----------- \n{comment.get("title")}""")
        print(f"""\n ----------- Posteo original -----------\n{comment.get("context_tweet")}""")
        print(f"""\n ----------- Artículo -----------{comment.get("body")}""")
    
    print("----------------------------- Aplicación de filtros -----------------------------")    
    text = comment.get("text")
    for filter in _FILTERS:
        print(filter.__name__)
        text = filter().run(text)
        print(text)
        

if __name__ == "__main__":
    main()