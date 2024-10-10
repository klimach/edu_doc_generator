from PyQt6.QtWidgets import QGroupBox, QFormLayout, QComboBox
from handlers.options_handler import OptionsHandler

class DegreeInfoBox(QGroupBox):
    def __init__(self):
        super().__init__()
        self.options_handler = OptionsHandler()
        self.setTitle("Рівень/Галузь/Спеціальність")
        self.__create()
    
    def __create(self):
        form_layout = QFormLayout()
        self.setLayout(form_layout)

        self.study_level_dropdown = QComboBox(self)
        self.discipline_dropdown = QComboBox(self)
        self.specialties_dropdown = QComboBox(self)

        form_layout.addRow('Рівень підготовки:', self.study_level_dropdown)
        form_layout.addRow('Галузь:', self.discipline_dropdown)
        form_layout.addRow('Спеціальність:', self.specialties_dropdown)

        self.levels_update()
        self.disciplines_update()
        self.specialities_update()
        
    def levels_update(self):
        self.study_level_dropdown.clear()
        study_level_raw_otpions = self.options_handler.load_options("study_levels")
        for level in study_level_raw_otpions:
            self.study_level_dropdown.addItem(level["name"], level)

    def disciplines_update(self):
        self.discipline_dropdown.clear()
        study_fields_raw_options = self.options_handler.load_options("study_fields")
        for field in study_fields_raw_options:
            text = f"{field['code']} | {field['name']}"
            self.discipline_dropdown.addItem(text, field)
        self.discipline_dropdown.currentIndexChanged.connect(self.specialities_update)
    
    def specialities_update(self):
        selected_data = self.discipline_dropdown.currentData()
        self.specialties_dropdown.clear()
        for field in selected_data["specialties"]:
            text = f"{field['code']} | {field['name']}"
            self.specialties_dropdown.addItem(text, field)
        

    
