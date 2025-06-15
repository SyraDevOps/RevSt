import os
import json
import logging
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from core.config_loader import carregar_config
from core.qr import gerar_qrcode
from templates import capa, contracapa, artigo, glossario

class RevistaBuilder:
    def __init__(self, config_path='config.yaml', dados_path='data/conteudo.json'):
        self.config = carregar_config(config_path)
        self.dados_path = dados_path
        self.width, self.height = A4
        self.pdf_path = f"output/{self.config['nome_arquivo']}.pdf"
        self.canvas = canvas.Canvas(self.pdf_path, pagesize=A4)
        self.page_number = 0

        logging.basicConfig(
            filename='output/geracao.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )

        logging.info("Inicialização do gerador de revista.")

    def _nova_pagina(self):
        if self.page_number > 0:
            self.canvas.showPage()
        self.page_number += 1
        logging.debug(f"Nova página iniciada: {self.page_number}")

    def gerar(self):
        if not os.path.exists(self.dados_path):
            logging.error("Arquivo de dados não encontrado.")
            return

        with open(self.dados_path, encoding='utf-8') as f:
            conteudos = json.load(f)

        for conteudo in conteudos:
            tipo = conteudo.get('tipo')
            logging.info(f"Gerando página tipo: {tipo}")
            self._nova_pagina()

            if tipo == 'capa':
                capa.gerar(self.canvas, self.config, conteudo, self.page_number)
            elif tipo == 'artigo':
                artigo.gerar(self.canvas, self.config, conteudo, self.page_number)
            elif tipo == 'glossario':
                glossario.gerar(self.canvas, self.config, conteudo, self.page_number)
            elif tipo == 'contracapa':
                contracapa.gerar(self.canvas, self.config, conteudo, self.page_number)
            else:
                logging.warning(f"Tipo de página não reconhecido: {tipo}")

        self.canvas.save()
        logging.info(f"Revista gerada com sucesso em: {self.pdf_path}")