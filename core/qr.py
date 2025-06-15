import qrcode
from reportlab.lib.utils import ImageReader
import io

def gerar_qrcode(url: str, tamanho: int = 4):
    """
    Gera um QR Code para a URL fornecida e retorna uma imagem compatível com ReportLab.

    :param url: Link que será codificado no QR Code.
    :param tamanho: Tamanho do QR code (intensidade de pixels).
    :return: ImageReader contendo o QR.
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=tamanho,
        border=1
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    buffer = io.BytesIO()
    img.save(buffer, format='PNG')
    buffer.seek(0)

    return ImageReader(buffer)
