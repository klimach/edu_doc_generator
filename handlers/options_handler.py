import json

class OptionsHandler:
    def __init__(self, json_file='config/formOptions.json'):
        self.json_file = json_file

    def load_options(self, option_name):
        with open(self.json_file, 'r', encoding="utf8") as file:
            data = json.load(file)
            return data.get(option_name, [])

    def add_option(self, option_name, option_value):
        with open(self.json_file, 'r', encoding="utf8") as file:
            data = json.load(file)

        if option_name not in data:
            data[option_name] = []
        if option_value not in data[option_name]:
            data[option_name].append(option_value)

        with open(self.json_file, 'w', encoding="utf8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def remove_option(self, option_name, option_value):
        with open(self.json_file, 'r', encoding="utf8") as file:
            data = json.load(file)

        if option_name in data and option_value in data[option_name]:
            data[option_name].remove(option_value)

        with open(self.json_file, 'w', encoding="utf8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)