from PyQt6.QtWidgets import QGroupBox, QFormLayout, QSpinBox, QComboBox
from handlers import Helper, OptionsHandler

class EducationDateBox(QGroupBox):
    def __init__(self, options: OptionsHandler):
        super().__init__()
        self.options: OptionsHandler = options
        self.setTitle("Період навчання")
        self.init_ui()
    
    def init_ui(self):
        form_layout = QFormLayout()
        self.setLayout(form_layout)

        self.start_year_spinbox = QSpinBox()
        self.study_period_dropdown = QComboBox(self)

        form_layout.addRow("Рік початку навчання:", self.start_year_spinbox)
        form_layout.addRow('Строк навчання:', self.study_period_dropdown)

        self.refresh_data()

    def refresh_data(self):
        self.start_year_spinbox.setRange(2024, 2050)
        self.study_period_dropdown.clear()
        for period in self.options.data["study_periods"]:
            text = f"{Helper.year_declension(period['years'])} {Helper.month_declension(period['months'])}".strip()
            self.study_period_dropdown.addItem(text, period)
