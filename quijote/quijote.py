import re

def principal():
    
    with open('D:\Datos- NoBorrar\Martin\Documentos\Facultad_igna\DAO\quijote\quijote.txt', encoding='utf-8') as f:
        quijote_text = f.read().lower()

    quijote_words = set(re.findall(r'\b[a-z]+\b', quijote_text))

    with open('D:\Datos- NoBorrar\Martin\Documentos\Facultad_igna\DAO\quijote\words_alpha.txt', encoding='utf-8') as f:
        english_words = set(word.strip().lower() for word in f)

    print("Palabras únicas en el libro:", len(quijote_words))
    print("Palabras en el diccionario:", len(english_words))

    not_in_dict = sorted(quijote_words - english_words)

    print("Palabras del libro que no existen en el diccionario:", len(not_in_dict))
    print("Listado de palabras que no existen en el diccionario:")
    for word in not_in_dict:
        print(word)


if __name__ == "__main__":
    principal()