from PyQt6.QtWidgets import QMainWindow, QHBoxLayout, QVBoxLayout, QWidget, QPushButton, QMessageBox, QFileDialog
from handlers import OptionsHandler, ExcelGenerator
from ui.main import MenuBar, DateBox, EducationFormatBox, DegreeInfoBox, EducationProgramBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Навчальний план v0.1-alpha")
        self.json_handler = OptionsHandler()
        self.excel_generator = ExcelGenerator()
        self.initUI()

    def initUI(self):
        menu_bar = MenuBar(self)
        menu_bar.install()

        self.button = QPushButton('Створити файл')
        self.button.clicked.connect(self.generate_button)
        self.button.setEnabled(False)

        self.date_box = DateBox()
        self.edu_format_box = EducationFormatBox()
        self.degree_info_box = DegreeInfoBox()
        self.edu_program_box = EducationProgramBox()
        self.edu_program_box.line_edit.textChanged.connect(self.check_input)

        main_widget = QWidget(self)
        main_layout = QVBoxLayout(main_widget)
        
        top_layout = QHBoxLayout()
        top_layout.addWidget(self.date_box)
        top_layout.addWidget(self.edu_format_box)

        main_layout.addLayout(top_layout)
        main_layout.addWidget(self.degree_info_box)
        main_layout.addWidget(self.edu_program_box)
        main_layout.addWidget(self.button)
        
        self.setCentralWidget(main_widget)

    def generate_button(self):
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
                    values = self.get_values()
                    self.excel_generator.generate(file_path=file_path, values=values)
                    QMessageBox.information(self, "Успіх", f"Файл успішно створено:\n{file_path}")
                except Exception as ex:
                    QMessageBox.warning(self, "Помилка", f"Не вдалося стоврити файл\nПомилка: {ex}")

    def check_input(self):
        if self.edu_program_box.line_edit.text().strip():
            self.button.setEnabled(True)
        else:
            self.button.setEnabled(False)

    def get_values(self):
        values = {
            "start_edu_date": self.date_box.start_year_spinbox.text(),
            "study_period": self.date_box.study_period_dropdown.currentData(),
            "study_form": self.edu_format_box.edu_form_dropdown.currentText(),
            "study_level": self.degree_info_box.study_level_dropdown.currentData(),
            "discipline": self.degree_info_box.discipline_dropdown.currentData(),
            "speciality": self.degree_info_box.specialties_dropdown.currentData(),
            "study_program": self.edu_program_box.line_edit.text()
        }
        return values