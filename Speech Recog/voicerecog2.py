import speech_recognition as sr
import requests

r = sr.Recognizer()
mic = sr.Microphone()
SERVER = "http://192.168.1.207:5000"

while True:
    with mic as source:
        r.adjust_for_ambient_noise(source)
        print("habla perra")
        audio = r.listen(source)

    you_said2 = r.recognize_google(audio_data=audio, language="es")
    you_said2 = you_said2.lower() #convierte el texto todo a lowercase
    print(you_said2)

    if "alex" in you_said2 or "pepit" in you_said2:
        print("entré en Alexe")
        if "encende" in you_said2 and "luces" in you_said2:
            print("entré en encender luz")
            requests.get(SERVER + "/lucesOn")
        elif "apagar" in you_said2 and "luces" in you_said2:
            print("entré en apagar luz")
            requests.get(SERVER + "/lucesOff")
        elif "encende" in you_said2 and "ventilador" in you_said2:
            print("entré en encender ventilador")
            requests.get(SERVER + "/ventiOn")
        elif "apagar" in you_said2 and "ventilador" in you_said2:
            print("entré en apagar ventilador")
            requests.get(SERVER + "/ventiOff")
        else:
            print("habla bien carajo!")
