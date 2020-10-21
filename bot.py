import speech_recognition as sr
from playsound import playsound
from time import sleep
import random
import pyaudio
import sys
from datetime import datetime, date
import easygui

r = sr.Recognizer()
alert = True

def Audio_to_text():
    with sr.Microphone(device_index= 2) as source:
        print("Listening.....")
        audio  = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            print('Did not get that, say it again')
        except sr.RequestError:
            print('Request_Error')
        return voice_data


def respond(voice_data, gend):
    r = random.randint(0, 2)
    if ('tejas') in voice_data:
        playsound("audio/for_"+str(gend)+str(r)+".mp3")
    if ('pages') in voice_data:
        playsound("audio/for_"+str(gend)+str(r)+".mp3")
    if ('98') in voice_data:
        playsound("audio/for_"+str(gend)+str(r)+".mp3")

# UNCOMMENT THIS TO SEE THE LIST OF YOUR DEVICES
#print(sr.Microphone.list_microphone_names()) 
#### change the device_index to the index of the CABLE Output (VB-Audio Virtual) ####

print("Follow this format: python3 bot.py <M/F>")
beginning = datetime.now().time()

try:
    gend = str(sys.argv[1])
    if gend not in ('F', 'M'):
        print("please specify gender of teacher as M/F")
        print("Follow this format: python3 bot.py <M/F>")
        exit()
    else:
        sleep(1)
        while True:
            voice_data = Audio_to_text()
            print(voice_data)
            respond(voice_data.lower(), gend = gend)
            end = datetime.now().time()
            duration = datetime.combine(date.min, end) - datetime.combine(date.min, beginning)
            durint = (str(duration)[2:4])
            if (int(durint) >= 1) and (alert == True):
                alert = False
                easygui.msgbox("Please rejoin, Meeting will end soon", title="Meeting end alert")

except IndexError:
    print("please specify gender of teacher as M/F")