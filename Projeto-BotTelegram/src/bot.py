import requests
import time
import json
import os
from dotenv import load_dotenv

load_dotenv() 

class TelegramBot:
    def __init__(self):
        token = os.getenv('API_KEY')
        self.url_base = f'https://api.telegram.org/bot{token}/'

    def Iniciar(self):
        update_id = None
        while True:
            atualizacao = self.obter_novas_mensagens(update_id)
            dados = atualizacao["result"]
            if dados:
                for dado in dados:
                    update_id = dado['update_id']
                    mensagem = str(dado["message"]["text"])
                    chat_id = dado["message"]["from"]["id"]
                    eh_primeira_mensagem = int(
                        dado["message"]["message_id"]) == 1
                    nome = str(dado["message"]["from"]["first_name"])
                    resposta = self.criar_resposta(mensagem, nome)
                    self.responder(resposta, chat_id)

    def criar_resposta(self, mensagem, nome):
        return f'Boa noite, {nome}'

    def responder(self, resposta, chat_id):
        link_requisicao = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(link_requisicao)

    def obter_novas_mensagens(self, update_id):
        link_requisicao = f'{self.url_base}getUpdates?timeout=1000'
        if update_id:
            link_requisicao = f'{link_requisicao}?timeout=1000&offset={update_id + 1}'
        resultado = requests.get(link_requisicao)
        return json.loads(resultado.content)


bot = TelegramBot()
bot.Iniciar()