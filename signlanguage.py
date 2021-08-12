import speech_recognition as spr
import numpy as np
import matplotlib.pyplot as plt
import cv2
from easygui import *
import os
from PIL import Image, ImageTk
from itertools import count
import tkinter as tk
import string
from googletrans import Translator
from gtts import gTTS
import pandas as pd
import googletrans

def func():
    r = spr.Recognizer()

    arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    with spr.Microphone() as source:

        r.adjust_for_ambient_noise(source)
        i = 0
        while True:
            print('Say something')
            audio = r.listen(source)

            # recognize speech using Sphinx
            try:
                a = r.recognize_google(audio)
                print("you said " + a.lower())

                for c in string.punctuation:
                    a = a.replace(c, "")

                if(a.lower() == 'goodbye'):
                    print("it's time to say good bye")
                    break


                else:

                    for i in range(len(a)):
                        if(a[i] in arr):

                            ImageAddress = 'letters/'+a[i]+'.jpg'
                            ImageItself = Image.open(ImageAddress)
                            ImageNumpyFormat = np.asarray(ImageItself)
                            plt.imshow(ImageNumpyFormat)
                            plt.axis('off')
                            plt.draw()
                            plt.pause(0.1)  # pause how many seconds
                            # plt.close()
                        else:
                            continue

            except:
                pass
            plt.close()
####################################################################################################################################################33

def start():
      #Creating Recognizer() class objects as recog1 for hello and recog2 for the translation part
      recog1 = spr.Recognizer()
      recog2 = spr.Recognizer()
      recog3 = spr.Recognizer()
      recog4 = spr.Recognizer()
      mc = spr.Microphone()

      #data frame for googletrans
      pd.set_option('max_colwidth', 300)
      lang_df = pd.DataFrame.from_dict(googletrans.LANGUAGES,  orient='index', columns=['Language'])

      #voice capturing
      with mc as source:
          recog1.adjust_for_ambient_noise(source)
          print("Speak 'Hello' to initiate the translation")
          print("----------------------------")
          audio = recog1.listen(source)
      
      #translation part
      if 'hello' in recog1.recognize_google(audio):
          recog1 = spr.Recognizer()
          translator = Translator()
          with mc as source:
              recog3.adjust_for_ambient_noise(source)
              print('first language')
              audio = recog3.listen(source)
              get_sentence = recog3.recognize_google(audio)
              get_sentence=get_sentence.lower()
              print(get_sentence)
              from_lang=lang_df.index[lang_df['Language'] == get_sentence][0]
          with mc as source:
              recog4.adjust_for_ambient_noise(source)
              print('second language')
              audio = recog4.listen(source)
              get_sentence = recog4.recognize_google(audio)
              get_sentence=get_sentence.lower()
              print(get_sentence)
              to_lang=lang_df.index[lang_df['Language'] == get_sentence][0]
          #from_lang = 'en'
          #dto_lang = 'hi'
          with mc as source:
              recog2.adjust_for_ambient_noise(source)
              print('Say something')
              audio = recog2.listen(source)
              get_sentence = recog2.recognize_google(audio)
              
              try:
                  get_sentence = recog2.recognize_google(audio)
                  print('Phrase to be Tranlated: '+ get_sentence)
                  text_to_translate = translator.translate(get_sentence, src = from_lang, dest = to_lang) #############################
                  text = text_to_translate.text
                  speak = gTTS(text=text, lang = to_lang,slow=False)
                  speak.save("captured_voice.mp3")
                  os.system("start captured_voice.mp3")
              except spr.UnknownValueError:
                  print("Unable to understand the input")
              except spr.RequestError as e:
                  print("Unable to provide required output".format(e))
###########################################################################################################################################################################


while 1:
    image = "signlang.png"
    msg = "BAATCHEET"
    choices = ["Voice to sign","voice to voice","sign to text"]
    reply = buttonbox(msg, image=image, choices=choices)
    if reply == choices[0]:
        func()
    if reply == choices[1]:
        start()
    if reply == choices[2]:
        sign_to_text()

