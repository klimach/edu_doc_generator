from PyQt6.QtWidgets import QDialog, QVBoxLayout, QGridLayout, QLineEdit,QGroupBox,QTabWidget, QWidget, QFormLayout, QPushButton, QListWidget, QListWidgetItem, QMessageBox
from handlers.options_handler import OptionsHandler
from PyQt6.QtCore import Qt

class SettingsWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Налаштування")
        self.json_handler = OptionsHandler()
        self.initUI()

    def initUI(self):
        ### playground ###
        main_layout = QGridLayout(self)
        self.setLayout(main_layout)

        tab = QTabWidget(self)

        study_level_page = QWidget(self)
        layout = QVBoxLayout()
        study_level_page.setLayout(layout)
        adding_groupbox = QGroupBox('Додати освітню ступінь (ОС)')
        form_layout = QFormLayout()
        adding_groupbox.setLayout(form_layout)

        self.new_value_input = QLineEdit(adding_groupbox)
        self.new_genitive_value_input = QLineEdit(adding_groupbox)

        self.add_button = QPushButton("Додати значення")
        self.add_button.clicked.connect(self.add_value)

        form_layout.addRow("Назва ОС:", self.new_value_input)
        form_layout.addRow("У родовому відмінку:", self.new_genitive_value_input)
        form_layout.addRow(self.add_button)

        layout.addWidget(adding_groupbox)

        deleting_groupbox = QGroupBox('Видалити освітню ступінь (ОС)')
        form_layout = QFormLayout()
        deleting_groupbox.setLayout(form_layout)

        self.values_list = QListWidget()
        self.load_values()

        self.remove_button = QPushButton("Видалити вибране")
        self.remove_button.clicked.connect(self.remove_value)

        form_layout.addRow(self.values_list)
        form_layout.addRow(self.remove_button)

        layout.addWidget(deleting_groupbox)

        # self.setLayout(layout)

        study_form_page = QWidget(self)
        layout = QVBoxLayout()
        study_form_page.setLayout(layout)
        adding_form_groupbox = QGroupBox('Додати форму навчання')
        form_layout = QFormLayout()
        adding_form_groupbox.setLayout(form_layout)
        form_layout.addRow('First Name:', QLineEdit(adding_form_groupbox))
        form_layout.addRow('Last Name:', QLineEdit(adding_form_groupbox))
        layout.addWidget(adding_form_groupbox)

        tab.addTab(study_level_page, "Освітній ступінь")
        tab.addTab(study_form_page, "Форма навчання")

        main_layout.addWidget(tab, 0, 0, 2, 1)

    def load_values(self):
        options = self.json_handler.load_options("study_levels")
        self.values_list.clear()
        options_data = [{ "text": f"{option['name']} ({option['name_genitive']})", "obj": option } for option in options]
        for data in options_data:
            item = QListWidgetItem()
            item.setText(data["text"])
            item.setData(Qt.ItemDataRole.UserRole, data["obj"])
            self.values_list.addItem(item)
        # self.values_list.addItems([f"{option['name']} ({option['name_genitive']})" for option in options])

    def add_value(self):
        new_value = {
            "name": self.new_value_input.text(),
            "name_genitive": self.new_genitive_value_input.text()
        }
        
        if new_value:
            self.json_handler.add_option("study_levels", new_value)
            self.load_values()
            self.new_value_input.clear()
            self.new_genitive_value_input.clear()
        else:
            QMessageBox.warning(self, "Помилка", "Введіть значення для додавання!")

    def remove_value(self):
        selected_item = self.values_list.currentItem()
        if selected_item:
            self.json_handler.remove_option("study_levels", selected_item.data(Qt.ItemDataRole.UserRole))
            self.load_values()
        else:
            QMessageBox.warning(self, "Помилка", "Виберіть значення для видалення!")