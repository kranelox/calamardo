import speech_recognition as sr
import requests

r = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
    r.adjust_for_ambient_noise(source)
    print("habla perra")
    audio = r.listen(source)

you_said2 = r.recognize_google(audio_data=audio, language="es")
you_said2 = you_said2.lower() #convierte el texto todo a lowercase
print(you_said2)

if "alex" in you_said2:
    print("entré en Alexe")
    if "encende" in you_said2 and "luces" in you_said2:
        print("entré en encender luz")
        requests.get("http://localhost:5000/lucesOn")
    elif "apagar" in you_said2 and "luces" in you_said2:
        print("entré en apagar luz")
        requests.get("http://localhost:5000/lucesOff")
    elif "encende" in you_said2 and "ventilador" in you_said2:
        print("entré en encender ventilador")
    elif "apagar" in you_said2 and "ventilador" in you_said2:
        print("entré en apagar ventilador")
    else:
        print("habla bien carajo!")
