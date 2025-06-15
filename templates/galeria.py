from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader
import os

def gerar(canvas, config, conteudo, page_number):
    largura, altura = canvas._pagesize

    canvas.setFillColor(HexColor(config['cores']['fundo_claro']))
    canvas.rect(0, 0, largura, altura, fill=1)

    # Título da galeria
    canvas.setFont(config['fonte_padrao'], 30)
    canvas.setFillColor(HexColor(config['cores']['texto_escuro']))
    canvas.drawString(2 * cm, altura - 3 * cm, conteudo.get("titulo", "Galeria Visual"))

    imagens = conteudo.get("imagens", [])
    padding = 1 * cm
    img_w = (largura - 4 * cm - padding) / 2
    img_h = (altura - 6 * cm - padding * 2) / 2

    posicoes = [
        (2 * cm, altura - 5 * cm - img_h),
        (2 * cm + img_w + padding, altura - 5 * cm - img_h),
        (2 * cm, altura - 5 * cm - img_h * 2 - padding),
        (2 * cm + img_w + padding, altura - 5 * cm - img_h * 2 - padding)
    ]

    for i, caminho in enumerate(imagens[:4]):
        if not os.path.exists(caminho):
            continue
        x, y = posicoes[i]
        img = ImageReader(caminho)
        canvas.drawImage(img, x, y, width=img_w, height=img_h, preserveAspectRatio=True, mask='auto')

    # Rodapé
    canvas.setFont(config['fonte_padrao'], 9)
    canvas.setFillColor(HexColor(config['cores']['texto_escuro']))
    canvas.drawString(2 * cm, 1.5 * cm, conteudo.get("rodape", "Revista SYN por SyraDevOps"))
    canvas.drawRightString(largura - 2 * cm, 1.5 * cm, f"Página {page_number}")
