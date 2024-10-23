from PyQt6.QtWidgets import QGroupBox, QFormLayout, QComboBox
from handlers.options_handler import OptionsHandler

class EducationDegreeBox(QGroupBox):
    def __init__(self, options):
        super().__init__()
        self.options = options
        self.setTitle("Рівень/Галузь/Спеціальність")
        self.init_ui()
    
    def init_ui(self):
        form_layout = QFormLayout()
        self.setLayout(form_layout)

        self.study_level_dropdown = QComboBox(self)
        self.field_dropdown = QComboBox(self)
        self.specialties_dropdown = QComboBox(self)

        form_layout.addRow('Рівень підготовки:', self.study_level_dropdown)
        form_layout.addRow('Галузь:', self.field_dropdown)
        form_layout.addRow('Спеціальність:', self.specialties_dropdown)

        self.refresh_data()

    def refresh_data(self):
        self.__levels_refresh()
        self.__fields_refresh()
        self.__specialities_refresh()
        
    def __levels_refresh(self):
        self.study_level_dropdown.clear()
        study_level_raw_otpions = self.options.data["study_levels"]
        for level in study_level_raw_otpions:
            self.study_level_dropdown.addItem(level["name"], level)

    def __fields_refresh(self):
        try:
            self.field_dropdown.currentIndexChanged.disconnect()
        except:
            pass

        self.field_dropdown.clear()
        study_fields_raw_options = self.options.data["study_fields"]
        for field in study_fields_raw_options:
            text = f"{field['code']} | {field['name']}"
            self.field_dropdown.addItem(text, field)
        self.field_dropdown.currentIndexChanged.connect(self.__specialities_refresh)
    
    def __specialities_refresh(self):
        selected_data = self.field_dropdown.currentData()
        self.specialties_dropdown.clear()
        for field in selected_data["specialties"]:
            text = f"{field['code']} | {field['name']}"
            self.specialties_dropdown.addItem(text, field)
        

    
