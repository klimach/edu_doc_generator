from PyQt6.QtWidgets import QWidget, QPushButton, QFrame, QGridLayout, QVBoxLayout, QListWidgetItem, QLineEdit, QMessageBox, QListWidget, QLabel, QGroupBox
from PyQt6.QtGui import QRegularExpressionValidator
from PyQt6.QtCore import QRegularExpression, Qt
from handlers import OptionsHandler

class EducationSpecializationWidget(QWidget):
    def __init__(self, options: OptionsHandler):
        super().__init__()
        self.options = options
        self.init_ui()

    def init_ui(self):        
        group_box = QGroupBox('Налаштування галузей та спеціалізацій')

        grid_layout = QGridLayout()

        self.field_num = QLineEdit()
        self.field_num.setValidator(QRegularExpressionValidator(QRegularExpression("^[0-9]+$"), self))
        self.field_num.setPlaceholderText("12")
        self.field_name = QLineEdit()
        self.field_name.setPlaceholderText("Інформаційні технології")
        
        self.field_add_button = QPushButton("Додати галузь")
        self.field_add_button.clicked.connect(self.add_field_value)

        self.specialization_num = QLineEdit()
        self.specialization_num.setValidator(QRegularExpressionValidator(QRegularExpression("^[0-9]+$"), self))
        self.specialization_num.setPlaceholderText("123")
        self.specialization_name = QLineEdit()
        self.specialization_name.setPlaceholderText("Комп'ютерна інженерія")
        self.specialization_name_genitive = QLineEdit()
        self.specialization_name_genitive.setPlaceholderText("Комп'ютерної інженерії")
        
        self.specialization_add_button = QPushButton("Додати спеціалізацію")
        self.specialization_add_button.clicked.connect(self.add_specialization_value)

        self.field_list = QListWidget()
        self.populate_field_values_list()

        self.specialization_list = QListWidget()
        self.populate_specialization_values_list()

        self.field_remove_button = QPushButton("Видалити галузь")
        self.field_remove_button.clicked.connect(self.remove_field_value)

        self.specialization_remove_button = QPushButton("Видалити спеціалізацію")
        self.specialization_remove_button.clicked.connect(self.remove_specialization_value)

        grid_layout.addWidget(QLabel("Код:"), 0, 0)
        grid_layout.addWidget(self.field_num, 0, 1)
        grid_layout.addWidget(QLabel("Галузь:"), 1, 0)
        grid_layout.addWidget(self.field_name, 1, 1)
        grid_layout.addWidget(self.field_add_button, 3, 0, 1, 2)

        grid_layout.addWidget(QLabel("Код:"), 0, 3)
        grid_layout.addWidget(self.specialization_num, 0, 4)
        grid_layout.addWidget(QLabel("Спеціальність:"), 1, 3)
        grid_layout.addWidget(self.specialization_name, 1, 4)
        grid_layout.addWidget(QLabel("У род.відмінку:"), 2, 3)
        grid_layout.addWidget(self.specialization_name_genitive, 2, 4)
        grid_layout.addWidget(self.specialization_add_button, 3, 3, 1, 2)

        grid_layout.addWidget(self.field_list, 4, 0, 1, 2)
        grid_layout.addWidget(self.specialization_list, 4, 3, 1, 2)
        
        grid_layout.addWidget(self.field_remove_button, 5, 0, 1, 2)
        grid_layout.addWidget(self.specialization_remove_button, 5, 3, 1, 2)
        
        line = QFrame()
        line.setFrameShape(QFrame.Shape.VLine)
        line.setFrameShadow(QFrame.Shadow.Sunken)
        grid_layout.addWidget(line, 0, 2, 6, 1)

        main_layout = QVBoxLayout()
        main_layout.addLayout(grid_layout)

        group_box.setLayout(main_layout)

        window_layout = QVBoxLayout(self)
        window_layout.addWidget(group_box)
        
    def add_field_value(self):
        field_num = self.field_num.text().strip()
        field_name = self.field_name.text().strip()
        if field_num and field_name:
            new_value = {
                "code": int(field_num),
                "name": field_name,
                "specialties": []
            }
            result = filter(lambda f: f["code"] == int(field_num), self.options.data["study_fields"])
            if not any(result):
                self.options.data["study_fields"].append(new_value)
                self.populate_field_values_list()
            else:
                QMessageBox.warning(self, "Помилка", f"Галузь з кодом '{int(field_num)}' вже присутня в списку")
        else:
            QMessageBox.warning(self, "Помилка", "Для додавання нового значення, поля мають бути заповнені!")
    
    def add_specialization_value(self):
        specialization_num = self.specialization_num.text().strip()
        specialization_name = self.specialization_name.text().strip()
        specialization_name_gen = self.specialization_name_genitive.text().strip()
        if all([specialization_num, specialization_name, specialization_name_gen]):
            new_value = {
                "code": int(specialization_num),
                "name": specialization_name,
                "name_genitive": specialization_name_gen
            }
            field_data = self.field_list.currentItem().data(Qt.ItemDataRole.UserRole)
            index = next((i for i, d in enumerate(self.options.data["study_fields"]) if d.get("code") == field_data["code"]), None)
            result = filter(lambda s: s["code"] == int(specialization_num), self.options.data["study_fields"][index]["specialties"])
            if not any(result):
                self.options.data["study_fields"][index]["specialties"].append(new_value)
                self.field_list.currentItem().setData(Qt.ItemDataRole.UserRole, self.options.data["study_fields"][index])
                self.populate_specialization_values_list()
            else:
                QMessageBox.warning(self, "Помилка", f"Спеціальність з кодом '{int(specialization_num)}' вже присутня в списку")
        else:
            QMessageBox.warning(self, "Помилка", "Для додавання нового значення, поля мають бути заповнені!")


    def populate_field_values_list(self):
        try:
            self.field_list.currentItemChanged.disconnect()
        except:
            pass

        self.field_list.clear()
        options = self.options.data["study_fields"]
        for field in options:
            item = QListWidgetItem()
            item.setText(f"{field['code']} | {field['name']}")
            item.setData(Qt.ItemDataRole.UserRole, field)
            self.field_list.addItem(item)
        self.field_list.setCurrentRow(0)
        self.field_list.currentItemChanged.connect(self.populate_specialization_values_list)

    def remove_field_value(self):
        selected_item = self.field_list.currentItem()
        if selected_item:
            if self.field_list.count() <= 1:
                QMessageBox.information(self, "Інформація", "Для видалення значення додайте нове")
            else:
                field_data = selected_item.data(Qt.ItemDataRole.UserRole)
                index = next((i for i, d in enumerate(self.options.data["study_fields"]) if d.get("code") == field_data["code"]), None)
                if index != None:
                    del self.options.data["study_fields"][index]
                    self.populate_field_values_list()
                    self.populate_specialization_values_list()
        else:
            QMessageBox.warning(self, "Помилка", "Виберіть значення для видалення!")

    def populate_specialization_values_list(self):
        selected_field_item = self.field_list.currentItem()
        self.specialization_list.clear()
        for specializtion in selected_field_item.data(Qt.ItemDataRole.UserRole)['specialties']:
            item = QListWidgetItem()
            item.setText(f"{specializtion['code']} | {specializtion['name']}")
            item.setData(Qt.ItemDataRole.UserRole, specializtion)
            self.specialization_list.addItem(item)
    
    def remove_specialization_value(self):
        selected_field_item = self.field_list.currentItem()
        selected_specialization_item = self.specialization_list.currentItem()
        if selected_specialization_item:
            field_data = selected_field_item.data(Qt.ItemDataRole.UserRole)
            specialization_data = selected_specialization_item.data(Qt.ItemDataRole.UserRole)
            indexField = next((i for i, d in enumerate(self.options.data["study_fields"]) if d.get("code") == field_data["code"]), None)
            indexSpec = next((i for i, d in enumerate(self.options.data["study_fields"][indexField]["specialties"]) if d.get("code") == specialization_data["code"]), None)
            if indexSpec != None:
                del self.options.data["study_fields"][indexField]["specialties"][indexSpec]
                self.field_list.currentItem().setData(Qt.ItemDataRole.UserRole, self.options.data["study_fields"][indexField])
                self.populate_specialization_values_list()
        else:
            QMessageBox.warning(self, "Помилка", "Виберіть значення для видалення!")