import serial
import time
import speech_recognition as sr
from gtts import gTTS
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from pygame import mixer
mixer.init()
ard=serial.Serial('COM3',9600)
time.sleep(2)
print(ard.readline())
list1=["turn the light on","turn light on","light on","led on","turn led on"]
list2=["turn the light off","turn light off","light off","led off","turn led off"]

while 1:
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
        print("Say your command for LED")
        audio=r.listen(source,phrase_time_limit=5)
    try:
        response=r.recognize_google(audio)
        #response=r.recognize_sphinx(audio)
        var=response.lower()
        print(var)
        for i in range (0,len(list1)):
            if (var in list1[i]):
                ard.write(b'1')
                print("OK ! LED turned on")
                time.sleep(1)
                break
            if (var in list2[i]):
                ard.write(b'0')
                print("OK ! LED turned on")
                time.sleep(1)
                break
            if (var=="exit" or var=="quit"):
                exit()
    except sr.UnknownValueError:
        print("Could not understand voice")
    except sr.RequestError as e:
        print("Error;{0}",format(e))
