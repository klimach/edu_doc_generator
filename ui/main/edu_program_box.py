from PyQt6.QtWidgets import QGroupBox, QFormLayout, QLineEdit
from handlers.options_handler import OptionsHandler

class EducationProgramBox(QGroupBox):
    def __init__(self):
        super().__init__()
        self.options_handler = OptionsHandler()
        self.setTitle("Освітньо-професійна програма")
        self.init_ui()
    
    def init_ui(self):
        form_layout = QFormLayout()
        self.setLayout(form_layout)
        
        self.line_edit = QLineEdit(self)
        form_layout.addRow(self.line_edit)