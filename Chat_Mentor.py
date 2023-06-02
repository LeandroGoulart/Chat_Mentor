# Importações de recursos do sistema
import sys
import os
import winsound
from datetime import datetime

# Importações de recursos científicos e de visão computacional
import numpy as np
import cv2

# Importações de recursos de conversação com IA
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

# Importações de recursos de conversão de texto para áudio
import pyttsx3 as fala

# Importações de recursos de reconhecimento de fala
import speech_recognition as sr

# Importações de automação de telas/processos do Windows
from pywinauto.application import Application

print("\n> Importando recursos:... " + str(datetime.now()))

# Configuração do ChatBot
bot = ChatBot('Chat_Mentor',
              storage_adapter='chatterbot.storage.SQLStorageAdapter',
              logic_adapters=[
                  'chatterbot.logic.MathematicalEvaluation',
                  'chatterbot.logic.TimeLogicAdapter',
                  'chatterbot.logic.BestMatch'
              ])

# Treinamento do ChatBot
with open('chats.txt', 'r', encoding='utf-8') as file:
    chats = [line.strip() for line in file]

print("> Iniciando treinamento do chatbot .......: " + str(datetime.now()))
trainer = ListTrainer(bot)
trainer.train(chats)

# Configuração do mecanismo de síntese de voz
voz = fala.init('sapi5')
voices = voz.getProperty('voices')
rate = voz.getProperty('rate')
voz.setProperty('rate', rate + 75)
volume = voz.getProperty('volume')
voz.setProperty('volume', 1.0)

# Configuração do reconhecimento de fala
rec = sr.Recognizer()

# Função principal
def main():
    n = 0
    dtnas = "2020-03-03 13:33:00.000000"
    action = 0
    
    with sr.Microphone() as s:
        rec.adjust_for_ambient_noise(s)
        
        while True:
            rec.adjust_for_ambient_noise(s)
            
            if n == 0:
                print("\n\n >  ***   INICIANDO MENTOR   ***   <\n\n")
                voz.say("SAUDAÇÕES HUMANO, COMO POSSO GUIÁ-LO")
                voz.runAndWait()
            
            try:
                time = datetime.now()
                print('Ouvindo......: ' + str(time))
                winsound.Beep(2200, 30)
                
                audio = rec.listen(s)
                
                time = datetime.now()
                print('Processando..: ' + str(time))
                winsound.Beep(1000, 30)
                
                audio_capt = rec.recognize_google(audio, language='pt')
                
                time = datetime.now()
                print('Respondendo..: ' + str(time) + '\n')
                
            except sr.UnknownValueError:
                voz.say("Desculpe, eu não consegui compreender...")
                voz.runAndWait()
                n += 1
                continue
            
            except sr.RequestError as e:
                voz.say("Desculpe, mas estamos sem conexão no momento...")
                voz.runAndWait()
                n += 1
                continue
            
            except (KeyboardInterrupt, EOFError, SystemExit):
                voz.say("Desculpe, identifiquei um desligamento inesperado.")
                voz.runAndWait()
                print("\n\n> O MENTOR SE DESPEDE  *  E ATE A PROXIMA HUMANO\n L.Goulart")
                exit()
            
            print("Ser humano diz ... -> " + audio_capt + "\n")
            
            audio_capt = audio_capt.upper()
            
            if audio_capt.find('DESLIGAR') >= 0:
                print("\n\n> O MENTOR SE DESPEDE  *  E ATE A PROXIMA HUMANO\n L.Goulart")               
                voz.say("Desligando...")
                voz.runAndWait()
                exit()
            
            if audio_capt.find('YOUTUBE') >= 0:
                busca = audio_capt[audio_capt.find('YOUTUBE')+8:]
                print("Ação executada: Procurando vídeos com o tema... " + busca + "\n")
                os.startfile("https://www.youtube.com/results?search_query=" + busca)
                action = 1
            
            if audio_capt.find('OUTLOOK') >= 0:
                print("Ação executada: Abrindo e-mail...\n")
                os.startfile("Outlook.exe")
                action = 1
            
            if audio_capt.find('GMAIL') >= 0:
                print("Ação executada: Abrindo Gmail...\n")
                os.startfile("http://gmail.com")
                action = 1
            
            if audio_capt.find('CBN') >= 0:
                print("Ação executada: Abrindo rádio online...\n")
                os.startfile("http://cbn.globoradio.globo.com/servicos/estudio-ao-vivo/ESTUDIO-AO-VIVO.htm?praca=SP")
                action = 1
            
            if audio_capt.find('PESQUIS') >= 0:
                busca = audio_capt[audio_capt.find('PESQUIS')+9:]
                print("Ação executada: Pesquisando no Google sobre... " + busca + "\n")
                os.startfile("https://www.google.com.br/search?hl=pt-BR&q=" + busca)
                action = 1
            
            if audio_capt.find('TEMPO') >= 0 or audio_capt.find('CLIMA') >= 0:
                print("Ação executada: Verificando as condições climáticas...\n")
                os.startfile("https://www.ipmetradar.com.br/")
                action = 1
            
            if action == 0:
                resposta = "Ação não reconhecida. Tente novamente."
                print("ISIS responde ... -> " + str(resposta) + "\n")
                voz.say(resposta)
                voz.runAndWait()
                
            n += 1
            action = 0

if __name__ == "__main__":
    main()
