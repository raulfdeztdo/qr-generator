import qrcode
from PIL import Image, ImageDraw
from PyQt5.QtGui import QImage

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def pil_image_to_qimage(pil_image):
    pil_image = pil_image.convert("RGBA")
    data = pil_image.tobytes("raw", "RGBA")
    qimage = QImage(data, pil_image.size[0], pil_image.size[1], QImage.Format_RGBA8888)
    return qimage

def generate_qr_code(url, hex_color, logo_path=None):
    rgb_color = hex_to_rgb(hex_color)

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    matrix = qr.get_matrix()
    qr_size = len(matrix)

    img_qr = Image.new('RGB', (qr_size * 10, qr_size * 10), 'white')
    draw = ImageDraw.Draw(img_qr)

    module_size = 10
    radius = 8

    for y in range(qr_size):
        for x in range(qr_size):
            if matrix[y][x]:
                draw.rounded_rectangle(
                    [x * module_size, y * module_size, (x + 1) * module_size, (y + 1) * module_size],
                    radius,
                    fill=rgb_color
                )

    if logo_path:
        logo = Image.open(logo_path).convert("RGBA")
        logo_size = 140
        logo = logo.resize((logo_size, logo_size), Image.LANCZOS)

        pos = (
            (img_qr.size[0] - logo_size) // 2,
            (img_qr.size[1] - logo_size) // 2
        )

        mask_logo = logo.split()[3]
        img_qr.paste(logo, pos, mask=mask_logo)

    return pil_image_to_qimage(img_qr)