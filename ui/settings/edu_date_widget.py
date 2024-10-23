from PyQt6.QtWidgets import QWidget, QFormLayout,QPushButton, QVBoxLayout, QHBoxLayout, QListWidgetItem, QLineEdit,QMessageBox, QListWidget, QLabel, QGroupBox
from PyQt6.QtGui import QRegularExpressionValidator
from PyQt6.QtCore import QRegularExpression, Qt
from handlers import OptionsHandler, Helper

class EducationDateWidget(QWidget):
    def __init__(self, options: OptionsHandler):
        super().__init__()
        self.options = options
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        
        group_box = QGroupBox('Налаштування періодів навчання')
        form_layout = QFormLayout(group_box)

        self.years_le = QLineEdit(group_box)
        self.years_le.setValidator(QRegularExpressionValidator(QRegularExpression("^(1[0-5]|[0-9])$"), self))
        self.years_le.setPlaceholderText("0-15 років")
        self.months_le = QLineEdit(group_box)
        self.months_le.setValidator(QRegularExpressionValidator(QRegularExpression("^(1[0-2]|[0-9])$"), self))
        self.months_le.setPlaceholderText("0-12 місяців")
        
        self.add_button = QPushButton("Додати значення")
        self.add_button.clicked.connect(self.add_range)

        self.ranges_list = QListWidget()
        self.populate_ranges_list()

        self.sort_button = QPushButton("Сортувати")
        self.sort_button.clicked.connect(self.sort_range)
        self.sort_button_clicked = False

        self.remove_button = QPushButton("Видалити")
        self.remove_button.clicked.connect(self.remove_range)

        horizontal_buttons_bl = QHBoxLayout()
        horizontal_buttons_bl.addWidget(self.sort_button)
        horizontal_buttons_bl.addWidget(self.remove_button)

        form_layout.addRow(QLabel("Роки:"), self.years_le)
        form_layout.addRow(QLabel("Місяці:"), self.months_le)
        form_layout.addRow(self.add_button)
        form_layout.addRow(self.ranges_list)
        form_layout.addRow(horizontal_buttons_bl)

        layout.addWidget(group_box)
        self.setLayout(layout)

    def populate_ranges_list(self):
        self.ranges_list.clear()
        for period in self.options.data["study_periods"]:
            text = f"{Helper.year_declension(period['years'])} {Helper.month_declension(period['months'])}"
            item = QListWidgetItem()
            item.setText(text)
            item.setData(Qt.ItemDataRole.UserRole, period)
            self.ranges_list.addItem(item)

    def add_range(self):
        try:
            new_value = {
                "years": int(self.years_le.text()),
                "months": int(self.months_le.text())
            }

            self.options.add_option("study_periods", new_value)
            self.populate_ranges_list()
        except:
            QMessageBox.warning(self, "Помилка", "Для додавання нового значення, поля мають бути заповнені!")

    def remove_range(self):
        selected_item = self.ranges_list.currentItem()
        if selected_item:
            if self.ranges_list.count() <= 1:
                QMessageBox.information(self, "Інформація", "Для видалення значення додайте нове")
            else:
                self.options.remove_option("study_periods", selected_item.data(Qt.ItemDataRole.UserRole))
                self.populate_ranges_list()

        else:
            QMessageBox.warning(self, "Помилка", "Виберіть значення для видалення!")
    
    def sort_range(self):
        self.sort_button_clicked = not self.sort_button_clicked
        self.options.data["study_periods"] = sorted(
            self.options.data["study_periods"], 
            key=lambda x: (x["years"], x["months"]), 
            reverse=self.sort_button_clicked)
        self.populate_ranges_list()