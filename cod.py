import nltk
def riqueza_lexica(tokens):
    tokens_conjunto=set(tokens)
    palabras_totales=len(tokens)
    palabras_diferentes=len(tokens_conjunto)
    riqueza_lexica=palabras_diferentes/palabras_totales
    return riqueza_lexica

carpeta_nombre = "punkt\\"
archivo_nombre = "lol.txt"


with open(carpeta_nombre+archivo_nombre,"r") as archivo:
    texto=archivo.read()
tokens=nltk.word_tokenize(texto,"spanish")
riqueza_lexica=riqueza_lexica(tokens)

print("Riqueza total:",riqueza_lexica)

conteo_individual=tokens.count("el")
print("Conteo individual:",conteo_individual)
palabras_totales=len(tokens)
porcentaje=100*conteo_individual/palabras_totales
print("Porcentaje:",porcentaje,'%')