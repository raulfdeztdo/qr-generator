import sys
from PyQt5.QtWidgets import QApplication
from src.gui import QRGeneratorGUI

def main():
    app = QApplication(sys.argv)
    window = QRGeneratorGUI()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()