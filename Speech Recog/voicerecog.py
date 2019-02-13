import speech_recognition as sr
r = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
    r.adjust_for_ambient_noise(source)
    print("habla perra")
    audio = r.listen(source)

you_said2 = r.recognize_google(audio)
print(you_said2)

if "Alex" in you_said2:
    print("entré en Alexe")
    if "encende" in you_said2 and "on" in you_said2 and "light" in you_said2:
        print("entré en encender luz")
    elif "turn" in you_said2 and "off" in you_said2 and "light" in you_said2:
        print("entré en apagar luz")
    elif "turn" in you_said2 and "on" in you_said2 and "fan" in you_said2:
        print("entré en encender ventilador")
    elif "turn" in you_said2 and "off" in you_said2 and "fan" in you_said2:
        print("entré en apagar ventilador")
    else:
        print("habla bien carajo!")
