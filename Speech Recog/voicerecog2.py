import speech_recognition as sr
r = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
    r.adjust_for_ambient_noise(source)
    print("habla perra")
    audio = r.listen(source)

you_said2 = r.recognize_google(audio_data=audio, language="es")
print(you_said2)

if "Alex" in you_said2:
    print("entré en Alexe")
    if "encende" in you_said2 and "luces" in you_said2:
        print("entré en encender luz")
    elif "apagar" in you_said2 and "luces" in you_said2:
        print("entré en apagar luz")
    elif "encende" in you_said2 and "ventilador" in you_said2:
        print("entré en encender ventilador")
    elif "apagar" in you_said2 and "ventilador" in you_said2:
        print("entré en apagar ventilador")
    else:
        print("habla bien carajo!")
