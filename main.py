import sys
from PyQt6.QtWidgets import QApplication
from ui.main_window import MainWindow

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.setFixedSize(window.size())
    sys.exit(app.exec())

if __name__ == "__main__":
    main()