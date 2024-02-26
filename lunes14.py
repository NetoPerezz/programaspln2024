c= "C:\\Users\\Epere\\Desktop\\OPTATIVA\\"
e= "lol.txt"
s= "archivo_nuevo.txt"

e2= open(c+e, "r")


s2=open(c+s, "w")
t=e2.read()
t2=t
s2.write(t2)


e2.close()
s2.close()

#s3=open(c+s, "r")
#print(s3.read())
#s3.close()

with open(c+s,"r") as archivo:
    texto=archivo.read()
#print(texto)
palabra= input("Escirbe la palabra a busar: ")
print(texto)

if palabra in texto:
    print("Encontre la palabra")
    
else:
    print("No encontre la palabra")
print("Ernesto Perez")
    

    
