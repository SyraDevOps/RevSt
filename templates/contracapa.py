from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor, Color
from core.qr import gerar_qrcode

def gerar(canvas, config, conteudo, page_number):
    largura, altura = canvas._pagesize

    # Fundo escuro degradê simples
    canvas.setFillColor(HexColor(config['cores']['fundo_escuro']))
    canvas.rect(0, 0, largura, altura, fill=1)

    # Círculo decorativo transparente
    canvas.setFillColor(Color(1, 1, 1, alpha=0.03))
    canvas.circle(largura / 2, altura / 2, 10 * cm, fill=1, stroke=0)

    # Mensagem final
    canvas.setFont(config['fonte_padrao'], 28)
    canvas.setFillColor(HexColor(config['cores']['texto_claro']))
    canvas.drawCentredString(largura / 2, altura / 2 + 4 * cm, conteudo.get("mensagem", "Obrigado por ler."))

    # Redes e site
    canvas.setFont(config['fonte_padrao'], 14)
    canvas.setFillColor(HexColor(config['cores']['texto_claro']))
    canvas.drawCentredString(largura / 2, 4 * cm, conteudo.get("redes", "@SyraDevOps  •  github.com/SyraDevOps"))
    
    canvas.setFont(config['fonte_padrao'], 16)
    canvas.setFillColor(HexColor(config['cores']['primaria']))
    canvas.drawCentredString(largura / 2, 2.5 * cm, conteudo.get("site", "syradevops.com"))

    # QR com slug final da edição
    slug = conteudo.get("slug", "ed01")
    url_final = f"{config['qr']['url_base']}/{slug}"
    qr_img = gerar_qrcode(url_final, tamanho=5)
    canvas.drawImage(qr_img, largura - 5.5 * cm, 2 * cm, width=4 * cm, height=4 * cm)