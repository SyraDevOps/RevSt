from reportlab.lib.units import cm
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import Paragraph
from reportlab.lib.colors import HexColor

def gerar(canvas, config, conteudo, page_number):
    largura, altura = canvas._pagesize

    # Cores condicionais
    fundo_escuro = conteudo.get('fundo_escuro', False)
    cor_fundo = HexColor(config['cores']['fundo_escuro'] if fundo_escuro else config['cores']['fundo_claro'])
    cor_texto = HexColor(config['cores']['texto_claro'] if fundo_escuro else config['cores']['texto_escuro'])
    cor_titulo = HexColor(config['cores']['primaria'])

    canvas.setFillColor(cor_fundo)
    canvas.rect(0, 0, largura, altura, fill=1)

    # Cabeçalho da seção
    canvas.setFont(config['fonte_padrao'], 14)
    canvas.setFillColor(cor_titulo)
    canvas.drawString(2 * cm, altura - 2.5 * cm, conteudo.get('secao', 'SEÇÃO').upper())

    # Título do artigo
    canvas.setFont(config['fonte_padrao'], 28)
    canvas.setFillColor(cor_texto)
    canvas.drawString(2 * cm, altura - 4.5 * cm, conteudo.get('titulo', 'Título do Artigo'))

    # Texto principal
    styles = getSampleStyleSheet()
    estilo_body = ParagraphStyle(
        name='Body',
        parent=styles['Normal'],
        fontName=config['fonte_padrao'],
        fontSize=config.get('tamanho_fonte', 11),
        leading=18,
        textColor=cor_texto
    )

    paragrafo = Paragraph(conteudo.get('texto', ''), estilo_body)
    largura_texto = largura - 4 * cm
    altura_disponivel = altura - 10 * cm
    paragrafo.wrapOn(canvas, largura_texto, altura_disponivel)
    paragrafo.drawOn(canvas, 2 * cm, altura - 10 * cm - paragrafo.height)

    # Citação destacada (opcional)
    citacao = conteudo.get('citar')
    if citacao:
        estilo_quote = ParagraphStyle(
            name='Quote',
            parent=styles['Normal'],
            fontName=config['fonte_padrao'],
            fontSize=14,
            leading=18,
            textColor=cor_titulo,
            leftIndent=1 * cm,
            rightIndent=1 * cm,
            spaceBefore=20,
            spaceAfter=10,
            italic=True
        )
        p_quote = Paragraph(citacao, estilo_quote)
        p_quote.wrapOn(canvas, largura - 4 * cm, 5 * cm)
        p_quote.drawOn(canvas, 2 * cm, 2.5 * cm)

    # Rodapé (opcional)
    canvas.setFont(config['fonte_padrao'], 9)
    canvas.setFillColor(cor_texto)
    canvas.drawString(2 * cm, 1.5 * cm, conteudo.get("rodape", "Revista SYN por SyraDevOps"))
    canvas.drawRightString(largura - 2 * cm, 1.5 * cm, f"Página {page_number}")