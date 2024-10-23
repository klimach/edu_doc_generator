import json

class OptionsHandler:
    def __init__(self, json_file='config/formOptions.json'):
        self.json_file = json_file
        self.data: dict = self.load_options()

    def load_options(self):
        with open(self.json_file, 'r', encoding="utf8") as file:
            data = json.load(file)
            return data
        
    def save_options(self):
        with open(self.json_file, 'w', encoding="utf8") as file:
            json.dump(self.data, file, ensure_ascii=False, indent=4)

    def add_option(self, option_name, option_value):
        if option_name not in self.data:
            self.data[option_name] = []
        if option_value not in self.data[option_name]:
            self.data[option_name].append(option_value)

    def remove_option(self, option_name, option_value):
        if option_name in self.data and option_value in self.data[option_name]:
            self.data[option_name].remove(option_value)