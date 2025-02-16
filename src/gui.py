from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog, QColorDialog, QMessageBox, QApplication
from PyQt5.QtGui import QPixmap, QColor, QClipboard
from PyQt5.QtCore import Qt
from .utils import qr_utils

SUCCESS_MESSAGE_TITLE = 'Éxito'

class QRGeneratorGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Generador de Códigos QR')
        self.setGeometry(100, 100, 400, 400)

        layout = QVBoxLayout()

        self.url_label = QLabel('Introduce la URL para el código QR:')
        layout.addWidget(self.url_label)

        self.url_input = QLineEdit(self)
        layout.addWidget(self.url_input)

        self.color_label = QLabel('Introduce el color en código HEX (por ejemplo, #0000FF para azul) o selecciona un color:')
        layout.addWidget(self.color_label)

        self.color_input = QLineEdit(self)
        layout.addWidget(self.color_input)

        self.color_button = QPushButton('Seleccionar Color', self)
        self.color_button.clicked.connect(self.select_color)
        layout.addWidget(self.color_button)

        self.logo_label = QLabel('Selecciona la imagen del logo (opcional):')
        layout.addWidget(self.logo_label)

        self.browse_button = QPushButton('Buscar Logo', self)
        self.browse_button.clicked.connect(self.browse_logo)
        layout.addWidget(self.browse_button)

        self.generate_button = QPushButton('Generar QR', self)
        self.generate_button.clicked.connect(self.generate_qr)
        layout.addWidget(self.generate_button)

        self.qr_label = QLabel(self)
        layout.addWidget(self.qr_label)

        self.copy_button = QPushButton('Copiar al Portapapeles', self)
        self.copy_button.clicked.connect(self.copy_to_clipboard)
        self.copy_button.setEnabled(False)
        layout.addWidget(self.copy_button)

        self.save_button = QPushButton('Guardar Imagen', self)
        self.save_button.clicked.connect(self.save_image)
        self.save_button.setEnabled(False)
        layout.addWidget(self.save_button)

        self.setLayout(layout)

    def select_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.color_input.setText(color.name())

    def browse_logo(self):
        logo_path, _ = QFileDialog.getOpenFileName(self, 'Buscar Logo', '', 'Images (*.png *.jpg *.bmp)')
        if logo_path:
            self.logo_path = logo_path
        else:
            self.logo_path = None

    def generate_qr(self):
        url = self.url_input.text()
        hex_color = self.color_input.text()
        logo_path = getattr(self, 'logo_path', None)

        if not url or not hex_color:
            QMessageBox.critical(self, 'Error', 'Por favor, completa todos los campos obligatorios.')
            return

        try:
            self.qr_image = qr_utils.generate_qr_code(url, hex_color, logo_path)
            qr_pixmap = QPixmap.fromImage(self.qr_image)
            self.qr_label.setPixmap(qr_pixmap)
            QMessageBox.information(self, SUCCESS_MESSAGE_TITLE, 'Código QR generado exitosamente.')
            self.copy_button.setEnabled(True)
            self.save_button.setEnabled(True)
        except Exception as e:
            QMessageBox.critical(self, 'Error', str(e))

    def copy_to_clipboard(self):
        clipboard = QApplication.clipboard()
        clipboard.setImage(self.qr_image)
        QMessageBox.information(self, SUCCESS_MESSAGE_TITLE, 'Imagen copiada al portapapeles.')

    def save_image(self):
        save_path, _ = QFileDialog.getSaveFileName(self, 'Guardar Imagen', '', 'PNG Files (*.png);;All Files (*)')
        self.qr_image.save(save_path)
        QMessageBox.information(self, SUCCESS_MESSAGE_TITLE, 'Imagen guardada exitosamente.')