import sys
import os
import numpy as np
import winsound
from datetime import datetime
from pywinauto.application import Application
import string

print("\n> Importando recursos de fala       .......: " + str(datetime.now()))
import pyttsx3 as fala
winsound.Beep(2200, 30)

print("> Importando recursos de reconhecimento de fala.......")
import speech_recognition as sr
winsound.Beep(2200, 30)

print("> Importando recursos de conversação  .......: ")
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
winsound.Beep(2200, 30)

print("> Importando recursos de visão computacional: " + str(datetime.now()))
import cv2
winsound.Beep(2200, 30)

rec = sr.Recognizer

bot = ChatBot('Chat_Mentor',
              storage_adapter='chatterbot.storage.SQLStorageAdapter',
              logic_adapters=[
                  'chatterbot.logic.MathematicalEvaluation',
                  #'chatterbot.logic.TimeLogicAdapter',
                  'chatterbot.logic.BestMatch'
              ],
              # filters-[filters.get_recent_repeated_responses]
              database_uri='sqlite:///database.db'
              )
winsound.Beep(2200, 30)

chats = [
    "Olá", "Oi", "Como vai?", "Tudo bem?", "Qual é o seu nome?", "Qual é a sua função?",
    "O que você faz?", "Preciso de ajuda", "Como posso te ajudar?", "Obrigado", "Por favor",
    "Desculpe", "Não entendi", "Poderia repetir?", "Qual é a resposta para a pergunta fundamental?", "Eu te amo",
    "Como está o clima hoje?", "Está chovendo lá fora?", "Qual é a temperatura agora?",
    "Vai fazer sol amanhã?", "Qual é a previsão do tempo para esta semana?",
    "Devo levar um guarda-chuva hoje?", "Como está o clima na cidade X?", "Vai fazer frio no fim de semana?",
    "Está ventando muito?", "Qual é a estação do ano mais agradável para você?", "Você gosta de dias ensolarados?",
    "Já viu um arco-íris?", "Qual é o seu clima favorito?", "Como você se sente em dias nublados?",
    "Gosta de dias chuvosos?", "Você já fez um boneco de neve?", "Qual é o lugar mais quente que você já visitou?",
    "Você já presenciou uma tempestade?", "O que você acha da mudança climática?", "Gosta de ver o pôr do sol?",
]
chats += [
    "Rock", "Pop", "Hip Hop", "Jazz", "Eletrônica", "Ação", "Comédia", "Drama", "Ficção Científica", "Suspense",
    "Ficção", "Não-ficção", "Romance", "Mistério", "Fantasia", "Pintura", "Fotografia", "Leitura", "Esportes",
    "Culinária", "Futebol", "Basquete", "Tênis", "Natação", "Corrida", "Pizza", "Sushi", "Hambúrguer", "Massas",
    "Churrasco", "Praia", "Montanha", "Cidades Históricas", "Aventura", "Natureza", "ajuda", "listar", "adicionar",
    "concluir", "remover", "tarefas", "comandos", "estudar", "prova", "matemática", "compras", "supermercado",
    "ligar", "médico", "consulta", "organizar", "armário", "exercícios", "físicos", "pesquise para mim",
    "busque na internet", "orçamento", "poupança", "investimento", "diversificação", "planejamento financeiro",
    "educação financeira", "metas financeiras", "gestão de dívidas", "controle de gastos", "equilíbrio financeiro",
    "reserva de emergência", "aposentadoria", "crescimento patrimonial", "rentabilidade", "análise de risco",
    "redução de custos", "aumento de receitas", "criação de um plano financeiro", "avaliação de ativos",
    "revisão de investimentos", "estratégias de economia", "educação sobre finanças pessoais",
    "orientação para empreendedores", "estruturação de fluxo de caixa", "proteção financeira",
    "planejamento tributário", "sucessão patrimonial", "consolidação de dívidas",
    "revisão de contratos", "análise de oportunidades de investimento", "acompanhamento de resultados financeiros",
    "Pesquise sobre investimentos", "Encontre informações sobre planejamento financeiro",
    "Busque dados sobre economia global", "Analise o mercado de ações",
    "Verifique as tendências de investimento", "Pesquise sobre fundos de investimento",
    "Descubra estratégias de diversificação de carteira", "Encontre informações sobre impostos e legislação financeira",
    "Faça uma análise de risco de investimentos", "Pesquise sobre opções de financiamento",
    "Verifique as taxas de juros atuais", "Encontre informações sobre seguro de vida e previdência",
    "Analise diferentes tipos de empréstimos", "Verifique as opções de investimento de longo prazo",
    "Pesquise sobre estratégias de aposentadoria"
]

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
