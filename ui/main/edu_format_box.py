from PyQt6.QtWidgets import QGroupBox, QFormLayout, QComboBox
from handlers.options_handler import OptionsHandler

class EducationFormatBox(QGroupBox):
    def __init__(self, options: OptionsHandler):
        super().__init__()
        self.options: OptionsHandler = options
        self.setTitle("Форма навчання")
        self.init_ui()
    
    def init_ui(self):
        form_layout = QFormLayout()
        self.setLayout(form_layout)

        self.edu_form_dropdown = QComboBox(self)
        form_layout.addRow(self.edu_form_dropdown)

        self.refresh_data()

    def refresh_data(self):
        self.edu_form_dropdown.clear()
        self.edu_form_dropdown.addItems(self.options.data["study_forms"])