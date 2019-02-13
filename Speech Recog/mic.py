import speech_recognition as sr
r = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
    audio = r.listen(source)

BING_KEY = "f578f72c36634748a629df0301d167dd"  # Microsoft Bing Voice Recognition API keys 32-character lowercase hexadecimal strings
try:
    print("Microsoft Bing Voice Recognition thinks you said " + r.recognize_bing(audio, key=BING_KEY))
except sr.UnknownValueError:
    print("Microsoft Bing Voice Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))
