import pyttsx3
from docx import Document

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def read_text_file(filename):
    with open(filename, 'r') as file:
        text = file.read()
    return text

def read_word_file(filename):
    doc = Document(filename)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text

def main():
    print("Bienvenido al conversor de texto a audio")
    print("1. Convertir archivo de texto (.txt) a audio")
    print("2. Convertir archivo de Word (.docx) a audio")
    choice = input("Seleccione una opción (1/2): ")

    if choice == '1':
        filename = input("Introduce el nombre del archivo de texto (.txt): ")
        text = read_text_file(filename)
        text_to_speech(text)
    elif choice == '2':
        filename = input("Introduce el nombre del archivo de Word (.docx): ")
        text = read_word_file(filename)
        text_to_speech(text)
    else:
        print("Opción no válida. Por favor seleccione 1 o 2.")

if __name__ == "__main__":
    main()
