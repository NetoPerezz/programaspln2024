import speech_recognition as sr
import pyttsx3
import os

def audio_a_texto(nombre_archivo):
    reconocedor = sr.Recognizer()
    with sr.AudioFile(nombre_archivo) as fuente:
        audio = reconocedor.listen(fuente)
        try:
            texto = reconocedor.recognize_google(audio, language="es-ES")  # Configura el idioma según sea necesario
            return texto
        except sr.UnknownValueError:
            return "No se pudo entender el audio"
        except sr.RequestError as e:
            return f"Error en la solicitud: {e}"

def texto_a_audio(texto, nombre_archivo_salida="salida.wav"):
    engine = pyttsx3.init()
    engine.save_to_file(texto, nombre_archivo_salida)
    engine.runAndWait()

def menu():
    while True:
        print("1. Convertir audio a texto")
        print("2. Convertir texto a audio")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            archivo_audio = input("Ingresa el nombre del archivo de audio (con extensión): ")
            texto_generado = audio_a_texto(archivo_audio)
            print("Texto reconocido:", texto_generado)
        elif opcion == "2":
            texto = input("Ingresa el texto que quieres convertir a audio: ")
            nombre_archivo_audio_salida = input("Ingrese el nombre del archivo de audio de salida (con extensión): ")
            texto_a_audio(texto, nombre_archivo_audio_salida)
            print(f"Audio guardado como '{nombre_archivo_audio_salida}'")
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")


menu()
