from PyQt6.QtWidgets import QMainWindow, QHBoxLayout, QVBoxLayout, QWidget, QPushButton, QMessageBox, QFileDialog
from handlers import OptionsHandler, ExcelGenerator
from ui.main import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Навчальний план v0.2-alpha")
        self.options = OptionsHandler()
        self.excel_generator = ExcelGenerator()
        self.init_ui()

    def init_ui(self):
        main_widget = QWidget(self)
        main_layout = QVBoxLayout(main_widget)
        
        self.menu_bar = MenuBar(self, self.options)

        self.edu_date_box = EducationDateBox(self.options)
        self.edu_format_box = EducationFormatBox(self.options)
        self.edu_degree_box = EducationDegreeBox(self.options)
        self.edu_program_box = EducationProgramBox()
        self.edu_program_box.line_edit.textChanged.connect(self.validate_form_data)

        self.button = QPushButton('Створити файл')
        self.button.clicked.connect(self.do_generate_output)
        self.button.setEnabled(False)
        
        top_layout = QHBoxLayout()
        top_layout.addWidget(self.edu_date_box)
        top_layout.addWidget(self.edu_format_box)
        main_layout.addLayout(top_layout)
        main_layout.addWidget(self.edu_degree_box)
        main_layout.addWidget(self.edu_program_box)
        main_layout.addWidget(self.button)
        
        self.setCentralWidget(main_widget)

    def do_generate_output(self):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Підтвердження")
        msg_box.setText("Ви дійсно хочете створити файл?")

        yes_button = QPushButton("Так")
        no_button = QPushButton("Ні")

        msg_box.addButton(yes_button, QMessageBox.ButtonRole.YesRole)
        msg_box.addButton(no_button, QMessageBox.ButtonRole.NoRole)
        msg_box.exec()

        if msg_box.clickedButton() == yes_button:
            file_path, _ = QFileDialog.getSaveFileName(self, "Зберегти файл", "Навчальний план", "Документ Excel (*.xlsx)")
            if file_path:
                try:
                    self.excel_generator.generate(file_path=file_path, values=self.get_form_values())
                    QMessageBox.information(self, "Успіх", f"Файл успішно створено:\n{file_path}")
                except Exception as ex:
                    QMessageBox.warning(self, "Помилка", f"Не вдалося стоврити файл\nПомилка: {ex}")

    def do_refresh_widgets(self):
        self.edu_date_box.refresh_data()
        self.edu_format_box.refresh_data()
        self.edu_degree_box.refresh_data()

    def validate_form_data(self):
        if self.edu_program_box.line_edit.text().strip():
            self.button.setEnabled(True)
        else:
            self.button.setEnabled(False)

    def get_form_values(self):
        values = {
            "start_edu_date": self.edu_date_box.start_year_spinbox.text(),
            "study_period": self.edu_date_box.study_period_dropdown.currentData(),
            "study_form": self.edu_format_box.edu_form_dropdown.currentText(),
            "study_level": self.edu_degree_box.study_level_dropdown.currentData(),
            "discipline": self.edu_degree_box.field_dropdown.currentData(),
            "speciality": self.edu_degree_box.specialties_dropdown.currentData(),
            "study_program": self.edu_program_box.line_edit.text()
        }
        return values
