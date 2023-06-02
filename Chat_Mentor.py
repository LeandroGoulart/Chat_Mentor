import sys                                                        #recursos sistema
import os                                                     #recursos sistema operacional
import numpy as np                                              #cientifica matematica
import winsound                                                 #recursos windows de som
from datetime import datetime                                      #recursos de data           

#automacao de telas/processos windows
from pywinauto.application import Application                                             
import string                                             

print("\n> Importando recursos:... " + str(datetime.now()))
#conversao de texto pra audio
import pyttsx3 as fala
 #reconhecimento de fala com i.a
import speech_recognition as sr

#recursos de conversação com i.a                             #recursos de conversação com i.a    
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

import cv2                                                       #visao computacional

rec = sr.Recognizer                                     #tratamento do reconhecimento de fala
###tratamento da robo
print("> Iniciando bot:..................")
bot = ChatBot('Chat_Mentor',                                   #inicia o Bot no ambiente
                storage_adapter='chatterbot.storage.SQLStorageAdapter',
                logic_adapters=[
                    'chatterbot.logic.MathematicalEvaluation',
                    'chatterbot.logic.TimeLogicAdapter',          #Hora e horario testes em ingles
                    'chatterbot.logic.BestMatch'
                ],
                filters-[filters.get_recent_repeated_responses]    #filtros de comportamento
                database_uri='sqlite:///database.db'            #base de dados do bot na pasta raiz
                
              )
winsound.Beep(2200, 30)

#treinamento do chat 
with open('arquivo.txt', 'r') as file:
    chats = eval(file.read())

print("> Iniciando treinamento do chatbot  .......: " + str(datetime.now()))

trainer = ListTrainer(bot)
trainer.train(chats)  #executa o treino com o vocabulario fornecido

voz = pyttsx3.init('sapi5')
voices = voz.getProperty('voices')  # Vozes disponíveis
rate = voz.getProperty('rate')  # Velocidade
print("> Velocidade de fala..................: " + str(rate))
voz.setProperty('rate', rate + 75)  # Ajusta a velocidade da voz, buscando algo mais 'natural'
volume = voz.getProperty('volume')
print("> Volume de voz.......................: " + str(volume))
voz.setProperty('volume', 1.0)  # Ajusta o volume máximo

# Inicia captura de áudio

def main():
    n = 0  # Contador para controlar o diálogo
    dtnas = "2020-03-03 13:33:00.000000"  # Data de 'nascimento' (não utilizado no código)
    action = 0  # Variável para controlar ações executadas
    
    rec = sr.Recognizer()  # Cria uma instância do objeto Recognizer para realizar o reconhecimento de fala
    voz = pyttsx3.init()  # Inicializa o mecanismo de síntese de voz
    
    with sr.Microphone() as s:
        rec.adjust_for_ambient_noise(s)  # Ajusta para o ruído ambiente antes de iniciar a captura de áudio
        
        while True:
            rec.adjust_for_ambient_noise(s)  # Ajusta para o ruído ambiente a cada iteração
            
            if n == 0:
                print("\n\n||||| INICIANDO ÍSIS - PROTÓTIPO COMPUTACIONAL MAKER ||||| ... [modo log] ...\n\n")
                voz.say("Oi, eu sou o PROTÓTIPO ÍSIS. Como posso ajudar?")
                voz.runAndWait()
            
            try:
                time = datetime.datetime.now()
                print('Ouvindo......: ' + str(time))
                winsound.Beep(2200, 30)  # Emite um bipe de 2200 Hz por 30 ms para indicar que está ouvindo
                
                audio = rec.listen(s)  # Captura o áudio
                
                time = datetime.datetime.now()
                print('Processando..: ' + str(time))
                winsound.Beep(1000, 30)  # Emite um bipe de 1000 Hz por 30 ms para indicar que está processando
                
                audio_capt = rec.recognize_google(audio, language='pt')  # Realiza o reconhecimento de fala usando a API do Google
                
                time = datetime.datetime.now()
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
                print("\n\n||||| DESLIGANDO ÍSIS - PROTÓTIPO COMPUTACIONAL MAKER ||||| \n||||| Andre Medeiros ")
                exit()
            
            print("Ser humano diz ... -> " + audio_capt + "\n")
            
            audio_capt = audio_capt.upper()  # Converte a entrada para letras maiúsculas para facilitar as comparações
            
            # Verifica as palavras-chave na entrada e executa a ação correspondente
            if audio_capt.find('DESLIGAR') >= 0:
                print("\n\n||||| DESLIGANDO ÍSIS - PROTÓTIPO COMPUTACIONAL MAKER ||||| \n||||| Andre Medeiros ")
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

