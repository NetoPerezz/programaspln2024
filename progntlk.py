import re
import nltk


carpeta_nombre = "punkt\\"
archivo_nombre = "lol.txt"

with open(carpeta_nombre+archivo_nombre,"r") as archivo:
    texto=archivo.read()
tokens=nltk.word_tokenize(texto,"spanish")
texto_nltk=nltk.Text(tokens)
texto_nltk.concordance("hardware")

expresion= re.compile(r".{,30}[\s^][Aa]rtículos? .{,30}")
resultados_busqueda=expresion.finditer(texto)
for resultado in resultados_busqueda:
    print(resultado.group(0))

tokens=nltk.word_tokenize(texto,"spanish")
texto_nltk=nltk.Text(tokens)
texto_nltk.similar("artículo")

with open(carpeta_nombre+archivo_nombre,"r") as archivo:
    texto=archivo.read()
tokens=nltk.word_tokenize(texto,"spanish")
texto_nltk=nltk.Text(tokens)
texto_nltk.similar("artículo")