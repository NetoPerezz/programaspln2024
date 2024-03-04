import nltk 
nltk.download('punkt')


carpeta_nombre= "punkt\\"
archivo_nombre= "lol.txt"

with open (carpeta_nombre+archivo_nombre,"r") as archivo:
    texto=archivo.read()

tokens= nltk.word_tokenize(texto,"spanish")

for token in tokens:
    print(token)
    
    
print('\n\n\n')
palabras_totales =len(tokens)
print('El total de la palabas de de: ',palabras_totales)