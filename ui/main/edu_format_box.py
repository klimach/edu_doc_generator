from PyQt6.QtWidgets import QGroupBox, QFormLayout, QComboBox
from handlers.options_handler import OptionsHandler

class EducationFormatBox(QGroupBox):
    def __init__(self):
        super().__init__()
        self.options_handler = OptionsHandler()
        self.setTitle("Форма навчання")
        self.__create()
    
    def __create(self):
        form_layout = QFormLayout()
        self.setLayout(form_layout)

        self.edu_form_dropdown = QComboBox(self)
        self.edu_form_dropdown.addItems(self.options_handler.load_options("study_forms"))

        form_layout.addRow(self.edu_form_dropdown)
