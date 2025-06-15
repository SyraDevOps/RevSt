from reportlab.lib.units import cm
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import Paragraph
from reportlab.lib.colors import HexColor

def gerar(canvas, config, conteudo, page_number):
    largura, altura = canvas._pagesize

    # Fundo claro padrão
    canvas.setFillColor(HexColor(config['cores']['fundo_claro']))
    canvas.rect(0, 0, largura, altura, fill=1)

    # Título principal
    canvas.setFont(config['fonte_padrao'], 36)
    canvas.setFillColor(HexColor(config['cores']['texto_escuro']))
    canvas.drawString(2 * cm, altura - 3 * cm, conteudo.get('titulo', 'Glossário'))

    # Linha decorativa
    canvas.setStrokeColor(HexColor(config['cores']['primaria']))
    canvas.setLineWidth(2)
    canvas.line(2 * cm, altura - 3.5 * cm, 12 * cm, altura - 3.5 * cm)

    # Estilo dos termos
    styles = getSampleStyleSheet()
    estilo_def = ParagraphStyle(
        name='GlossarioDef',
        parent=styles['Normal'],
        fontName=config['fonte_padrao'],
        fontSize=10,
        leading=14,
        textColor=HexColor(config['cores']['texto_escuro'])
    )

    termos = conteudo.get("termos", {})
    y_pos = altura - 5 * cm
    col_width = (largura - 5 * cm) / 2
    padding_bottom = 1.2 * cm

    for i, (termo, definicao) in enumerate(termos.items()):
        col = i % 2
        x_pos = 2 * cm if col == 0 else 2 * cm + col_width + 1 * cm

        # Título do termo
        canvas.setFont(config['fonte_padrao'], 12)
        canvas.setFillColor(HexColor(config['cores']['primaria']))
        canvas.drawString(x_pos, y_pos, termo)

        # Definição do termo
        p = Paragraph(definicao, estilo_def)
        p.wrapOn(canvas, col_width - 1 * cm, altura)
        p.drawOn(canvas, x_pos, y_pos - p.height - 0.2 * cm)

        if col == 1:
            y_pos -= max(p.height + padding_bottom, 2 * cm)

    # Rodapé
    canvas.setFont(config['fonte_padrao'], 9)
    canvas.setFillColor(HexColor(config['cores']['texto_escuro']))
    canvas.drawString(2 * cm, 1.5 * cm, conteudo.get("rodape", "Revista SYN por SyraDevOps"))
    canvas.drawRightString(largura - 2 * cm, 1.5 * cm, f"Página {page_number}")