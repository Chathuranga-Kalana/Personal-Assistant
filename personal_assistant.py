from gtts import gTTS
from time import strftime

import speech_recognition as sr
import os
import webbrowser
import smtplib
import re
import datetime
import requests



def voiceOutput(audio):
    print(audio)
    tts = gTTS(text = audio, lang='en')
    tts.save('audio.mp3')
    os.system('mpg123 audio.mp3')

def myCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('yeah i\'m listening')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print('you said ' + command + '\n')
    except sr.UnknownValueError:
        command = myCommand()
    return command

#getting current time
def time():
    time = datetime.datetime.now().time().strftime("%H:%M")
    return time
#this is the place that magic happen 
def assistant(command):
    if 'google' in command:
        url = 'https://www.google.com'
        webbrowser.open(url)

    elif 'search' in command:
        reg_ex = re.search('search (.+)', command)
        if reg_ex:
            word = reg_ex.group(1)
            webbrowser.open(word,new=2)
        
    if 'what\'s up' in command:
        voiceOutput('chill bro')
    if 'hi' in command:
        voiceOutput('hi')
    
    if 'what\'s the time now'   in command:
        timeNow = time()
        voiceOutput('the time is '+timeNow)
    
    if 'tell me a joke' in command:
        res =requests.get( 'https://icanhazdadjoke.com/',headers={"Accept":"application/json"})
        if res.status_code == 200:
            voiceOutput(str(res.json()['joke']))
        else:
            voiceOutput('oops! The real joke is you ha ha')

    if 'who is your owner' in command:
        voiceOutput('his name is Chathuranga Kalana')

    
voiceOutput('yeah i\'m listening')

while True:
    assistant(myCommand())
