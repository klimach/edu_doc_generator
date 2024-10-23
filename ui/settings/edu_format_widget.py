from PyQt6.QtWidgets import QWidget, QFormLayout,QPushButton, QVBoxLayout, QListWidgetItem, QLineEdit, QMessageBox, QListWidget, QLabel, QGroupBox
from PyQt6.QtCore import Qt
from handlers import OptionsHandler

class EducationFormatWidget(QWidget):
    def __init__(self, options: OptionsHandler):
        super().__init__()
        self.options = options
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        
        group_box = QGroupBox('Налаштування форм навчання')
        form_layout = QFormLayout(group_box)

        self.new_value = QLineEdit(group_box)
        self.new_value.setPlaceholderText("Денна")
        
        self.add_button = QPushButton("Додати значення")
        self.add_button.clicked.connect(self.add_value)

        self.values_list = QListWidget()
        self.populate_values_list()

        self.remove_button = QPushButton("Видалити")
        self.remove_button.clicked.connect(self.remove_value)

        form_layout.addRow(QLabel("Форма:"), self.new_value)
        form_layout.addRow(self.add_button)
        form_layout.addRow(self.values_list)
        form_layout.addRow(self.remove_button)

        layout.addWidget(group_box)
        self.setLayout(layout)

    def populate_values_list(self):
        self.values_list.clear()
        for option in self.options.data["study_forms"]:
            item = QListWidgetItem()
            item.setText(option)
            item.setData(Qt.ItemDataRole.UserRole, option)
            self.values_list.addItem(item)

    def add_value(self):
        new_value = self.new_value.text().strip()
        if new_value:
            self.options.add_option("study_forms", new_value)
            self.new_value.clear()
            self.populate_values_list()
        else:
            QMessageBox.warning(self, "Помилка", "Для додавання нового значення, поле мають бути заповнене!")

    def remove_value(self):
        selected_item = self.values_list.currentItem()
        if selected_item:
            if self.values_list.count() <= 1:
                QMessageBox.information(self, "Інформація", "Для видалення значення додайте нове")
            else:
                self.options.remove_option("study_forms", selected_item.data(Qt.ItemDataRole.UserRole))
                self.populate_values_list()
        else:
            QMessageBox.warning(self, "Помилка", "Виберіть значення для видалення!")