import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QIcon
from ui.main_window import MainWindow

def main():
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('icons\\app.png'))

    window = MainWindow()
    window.show()
    window.setFixedSize(window.size())
    sys.exit(app.exec())

if __name__ == "__main__":
    main()