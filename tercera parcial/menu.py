import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import pyttsx3
import speech_recognition as sr
import os
from pydub import AudioSegment
from pydub.playback import play
from sentiment_analysis_spanish import sentiment_analysis
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import pos_tag, ne_chunk
from nltk.tokenize import word_tokenize
from nltk.chunk import RegexpParser
import subprocess

# Descargar recursos necesarios para NLTK
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('vader_lexicon')

# Crear instancia del analizador de sentimientos en español
analizador_es = sentiment_analysis.SentimentAnalysisSpanish()

def convertir_a_exe():
    filepath = filedialog.askopenfilename(filetypes=[("Python files", "*.py")])
    if filepath:
        result = subprocess.run(['pyinstaller', '--onefile', filepath], capture_output=True, text=True)
        if result.returncode == 0:
            messagebox.showinfo("Éxito", "El archivo .py se ha convertido a ejecutable.")
        else:
            messagebox.showerror("Error", f"No se pudo convertir el archivo. Error: {result.stderr}")

def grabar_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        messagebox.showinfo("Grabando", "Por favor hable ahora...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio, language='es-ES')
            messagebox.showinfo("Texto del Audio", text)
        except sr.UnknownValueError:
            messagebox.showerror("Error", "No se pudo entender el audio.")
        except sr.RequestError:
            messagebox.showerror("Error", "Error al solicitar resultados del servicio de reconocimiento.")

def texto_a_audio():
    text = simpledialog.askstring("Entrada", "Ingresa el texto a convertir en audio:")
    if text:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

def audio_texto_audio():
    filepath = filedialog.askopenfilename(filetypes=[("Audio files", "*.wav;*.mp3")])
    if filepath:
        audio = AudioSegment.from_file(filepath)
        play(audio)

def texto_a_audio_desde_archivo():
    filepath = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("Word files", "*.docx")])
    if filepath:
        with open(filepath, 'r', encoding='utf-8') as file:
            text = file.read()
            engine = pyttsx3.init()
            engine.say(text)
            engine.runAndWait()

def chat_gpt_simulator():
    # Aquí puedes agregar el código para simular el chat GPT
    pass

def analizar_sentimientos():
    text = simpledialog.askstring("Entrada", "Ingresa el texto para analizar su sentimiento:")
    if text:
        analyzer = SentimentIntensityAnalyzer()
        scores = analyzer.polarity_scores(text)
        messagebox.showinfo("Análisis de Sentimientos", str(scores))

def chunking():
    text = simpledialog.askstring("Entrada", "Ingresa el texto para realizar chunking:")
    if text:
        tokens = word_tokenize(text)
        tagged = pos_tag(tokens)
        grammar = "NP: {<DT>?<JJ>*<NN>}"
        cp = RegexpParser(grammar)
        result = cp.parse(tagged)
        messagebox.showinfo("Chunking Result", str(result))

def ne_chunking():
    text = simpledialog.askstring("Entrada", "Ingresa el texto para identificar entidades nombradas:")
    if text:
        tokens = word_tokenize(text)
        tagged = pos_tag(tokens)
        entities = ne_chunk(tagged)
        messagebox.showinfo("Entidades Nombradas", str(entities))

def analisis_sentimientos_spanish():
    text = simpledialog.askstring("Entrada", "Ingresa una frase en español para analizar su sentimiento:")
    if text:
        puntuacion = analizador_es.sentiment(text)
        sentimiento = interpretar_sentimiento(puntuacion)
        messagebox.showinfo("Análisis de Sentimientos", f"Texto: '{text}'\nSentimiento: {sentimiento}")

def interpretar_sentimiento(puntuacion):
    if puntuacion > 0.6:
        return "positivo"
    elif puntuacion < 0.4:
        return "negativo"
    else:
        return "neutral"

def crear_menu():
    root = tk.Tk()
    root.title("Menú Principal")

    menubar = tk.Menu(root)
    
    opciones_menu = tk.Menu(menubar, tearoff=0)
    opciones_menu.add_command(label="Convertir .py a ejecutable", command=convertir_a_exe)
    opciones_menu.add_command(label="Grabar audio y convertir a texto", command=grabar_audio)
    opciones_menu.add_command(label="Convertir texto a audio", command=texto_a_audio)
    opciones_menu.add_command(label="Convertidor Audio-Texto-Audio", command=audio_texto_audio)
    opciones_menu.add_command(label="Texto de archivo a audio", command=texto_a_audio_desde_archivo)
    opciones_menu.add_command(label="Simulador de Chat GPT", command=chat_gpt_simulator)
    opciones_menu.add_command(label="Análisis de Sentimientos (Inglés)", command=analizar_sentimientos)
    opciones_menu.add_command(label="Chunking", command=chunking)
    opciones_menu.add_command(label="Identificación de Entidades Nombradas", command=ne_chunking)
    opciones_menu.add_command(label="Análisis de Sentimientos (Español)", command=analisis_sentimientos_spanish)

    menubar.add_cascade(label="Opciones", menu=opciones_menu)
    root.config(menu=menubar)

    root.mainloop()

if __name__ == "__main__":
    crear_menu()
