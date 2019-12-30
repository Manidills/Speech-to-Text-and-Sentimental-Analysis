# -*- coding: utf-8 -*-
"""speech to text with senti

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gvA21zINvGSUN4ieDfbxhD0FfAQg1RdE
"""

!pip install textblob

import nltk

nltk.download('punkt')

nltk.download("averaged_perceptron_tagger")

from textblob import TextBlob as blob

tb=blob("Am unhappy ")

tb.sentiment

tb.tags

!pip install SpeechRecognition

!apt install libasound2-dev portaudio19-dev libportaudio2 libportaudiocpp0 ffmpeg

!pip install pyaudio

import speech_recognition as sr

t=sr.Recognizer()

with sr.Microphone() as source:
    print("say something")
    audio=t.listen(source, timeout=2)
    try:
        text=t.recognize_google(audio)
        tb=blob(text)
        print(text)
        print(tb.sentiment)
        
    except:
        print("sorry .. Try harder")

