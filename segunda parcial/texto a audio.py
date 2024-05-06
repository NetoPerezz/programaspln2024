import pyaudio
import winspeech
import speech_recognition as sr

def text_to_audio(text):
    # Inicializar PyAudio
    p = pyaudio.PyAudio()

    # Crear un reproductor de audio
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=44100,
                    output=True)

    
    winspeech.say(text)

    
    stream.stop_stream()
    stream.close()
    p.terminate()

def speech_to_text():
    
    r = sr.Recognizer()

    
    with sr.Microphone() as source:
        print("Diciendo...")
        audio = r.listen(source)

    try:
        
        text = r.recognize_google(audio)
        print("Google Speech Recognition: " + text)
        return text
    except sr.UnknownValueError:
        print("No se pudo entender lo que dijiste")
    except sr.RequestError as e:
        print("Error en la solicitud a la API de Google; {0}".format(e))


texto = input("Escribeme el texto que quieres que diga:")
text_to_audio(texto)


texto_reconocido = speech_to_text()


text_to_audio(texto_reconocido)
