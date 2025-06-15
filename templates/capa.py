from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor
from core.qr import gerar_qrcode

def gerar(canvas, config, conteudo, page_number):
    """
    Gera a capa da revista com design configurável e QR Code dinâmico.
    """
    largura, altura = canvas._pagesize

    # Fundo com cor primária
    canvas.setFillColor(HexColor(config['cores']['primaria']))
    canvas.rect(0, 0, largura, altura, fill=1)

    # Título principal
    canvas.setFont(config['fonte_padrao'], 120)
    canvas.setFillColor(HexColor(config['cores']['fundo_claro']))
    canvas.drawCentredString(largura / 2, altura - 8 * cm, conteudo.get('titulo', 'SYN'))

    # Chamada secundária
    canvas.setFont(config['fonte_padrao'], 20)
    canvas.drawCentredString(largura / 2, altura / 2, conteudo.get('subtitulo', 'Revista Técnica e Criativa'))

    # Edição e data
    canvas.setFont(config['fonte_padrao'], 12)
    canvas.drawString(2 * cm, 2 * cm, conteudo.get('edicao', 'Edição Nº 01 // 2025'))

    # Site ou marca
    canvas.setFont(config['fonte_padrao'], 12)
    canvas.drawRightString(largura - 2 * cm, 2 * cm, config['qr']['url_base'])

    # QR Code com link da edição
    url_completa = f"{config['qr']['url_base']}/{conteudo.get('slug', 'ed01')}"
    qr_img = gerar_qrcode(url_completa, tamanho=5)
    canvas.drawImage(qr_img, largura - 5.5 * cm, altura - 6.5 * cm, width=4 * cm, height=4 * cm)

    # Número da página (invisível na capa mas contado)
    # (poderia ser comentado caso deseje omitir completamente)
    # canvas.drawRightString(largura - 2 * cm, 1.5 * cm, f"Página {page_number}")