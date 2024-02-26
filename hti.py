carpeta_nombre="hti\\" 
archivo_nombre="act.txt" 
with open(carpeta_nombre+archivo_nombre,"r") as archivo:
    texto=archivo.read() 
palabras_lista=texto.split() 
palabras_lista.sort() 
for palabra in palabras_lista: 
    print(palabra) 