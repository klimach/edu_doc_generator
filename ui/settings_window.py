from PyQt6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QTabWidget, QPushButton
from ui.settings import *
from copy import deepcopy

class SettingsWindow(QDialog):
    def __init__(self, options, main_window):
        super().__init__(main_window)
        self.setWindowTitle("Settings")
        self.options = options
        self.main_window = main_window
        self.init_ui()

    def init_ui(self):
        self.options_copy = deepcopy(self.options)
        layout = QVBoxLayout()
        self.tab_widget = QTabWidget()

        self.tab_widget.addTab(EducationDateWidget(self.options_copy), "Роки")
        self.tab_widget.addTab(EducationDegreeWidget(self.options_copy), "Ступінь")
        self.tab_widget.addTab(EducationFormatWidget(self.options_copy), "Форма")
        self.tab_widget.addTab(EducationSpecializationWidget(self.options_copy), "Галузь\\Спеціалізація")
        
        layout.addWidget(self.tab_widget)

        save_button = QPushButton("Зберегти", self)
        save_button.clicked.connect(self.save_settings)
        cancel_button = QPushButton("Скасувати", self)
        cancel_button.clicked.connect(self.close)

        horizontal_buttons_layout = QHBoxLayout()
        horizontal_buttons_layout.addWidget(save_button)
        horizontal_buttons_layout.addWidget(cancel_button)

        layout.addLayout(horizontal_buttons_layout)
        self.setLayout(layout)

    def save_settings(self):
        self.options.data = deepcopy(self.options_copy.data)
        del self.options_copy
        self.options.save_options()
        self.main_window.do_refresh_widgets()
        self.accept()