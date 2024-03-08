import nltk 
nltk.download('punkt')


carpeta_nombre= "punkt\\"
archivo_nombre= "lol.txt"

with open (carpeta_nombre+archivo_nombre,"r") as archivo:
    texto=archivo.read()

tokens= nltk.word_tokenize(texto,"spanish")

tokens_conjunto=set(tokens)

palabras_totales=len(tokens)
palabras_diferentes=len(tokens_conjunto)

riqueza_lexica=palabras_diferentes/palabras_totales


print(riqueza_lexica)

