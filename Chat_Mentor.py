import sys
import os
import numpy as np
import winsound
from datetime import datetime
from pywinauto.application import Application
import string

print("\n> Importando recursos de fala:... " + str(datetime.now()))
import pyttsx3 as fala
winsound.Beep(2200, 30)

print("> Importando recursos de reconhecimento da fala:....... ")
import speech_recognition as sr
winsound.Beep(2200, 30)

print("> Importando recursos de conversação:....... ")
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
winsound.Beep(2200, 30)

print("> Importando recursos de visão computacional: " + str(datetime.now()))
import cv2
winsound.Beep(2200, 30)

rec = sr.Recognizer  #tratamento do reconhecimento de fala

bot = ChatBot('Chat_Mentor',
                storage_adapter='chatterbot.storage.SQLStorageAdapter',
                logic_adapters=[
                    'chatterbot.logic.MathematicalEvaluation',
                    'chatterbot.logic.TimeLogicAdapter',
                    'chatterbot.logic.BestMatch'
                ],
                filters-[filters.get_recent_repeated_responses]
                database_uri='sqlite:///database.db'
                
              )
winsound.Beep(2200, 30)

chats = 
print("> Iniciando treinamento do chatbot  .......: " + str(datetime.now()))

trainer = ListTrainer(bot)
trainer.train(chats)

# TRATAMENTO DA VOZ
voz = fala.init('sapi5')
ids = voz.getProperty('voices')  # tipo de voz

rate = voz.getProperty('rate')
print("Velocidade da fala: " + str(rate))
voz.setProperty('rate', rate + 75)  # Ajusta velocidade da voz

volume = voz.getProperty('volume')
print("Volume da voz: " + str(volume))
voz.setProperty('volume', volume + 5)  # Ajusta volume
