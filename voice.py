#!/usr/bin/python
# -*- coding: utf-8 -*-

import speech_recognition as sr

r = sr.Recognizer()

while True:
    try:
        with sr.Microphone() as mic:
            print("Yanshee: I'm Listening")
            audio = r.listen(mic)
            text = r.recognize_google(audio)
            print("You said: " + text)

    except sr.UnknownValueError:
        print("Unable to recognize speech.")
        
