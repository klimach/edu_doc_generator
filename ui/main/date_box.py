from PyQt6.QtWidgets import QGroupBox, QFormLayout, QSpinBox, QComboBox
from handlers import Helper, OptionsHandler

class DateBox(QGroupBox):
    def __init__(self):
        super().__init__()
        self.options_handler = OptionsHandler()
        self.setTitle("Дати")
        self.__create()
    
    def __create(self):
        form_layout = QFormLayout()
        self.setLayout(form_layout)

        self.start_year_spinbox = QSpinBox()
        self.study_period_dropdown = QComboBox(self)

        self.start_year_spinbox.setRange(2024, 2050)

        for period in self.options_handler.load_options("study_periods"):
            text = f"{Helper.year_declension(period['years'])} {Helper.month_declension(period['months'])}"
            self.study_period_dropdown.addItem(text, period)

        form_layout.addRow("Рік початку навчання:", self.start_year_spinbox)
        form_layout.addRow('Строк навчання:', self.study_period_dropdown)
