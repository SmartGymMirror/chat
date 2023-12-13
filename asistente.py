import speech_recognition as sr
import pyttsx3


listener = sr.Recognizer()
engine= pyttsx3.init()
engine.say('Hola, soy tu asistente virtual')
engine.runAndWait()

try:
    with sr.Microphone() as source:
        print('Escuchando...')
        voice = listener.listen(source)
        rec = listener.recognize_google(voice)
        print(rec)

except:
    pass
