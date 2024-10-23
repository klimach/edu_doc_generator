import sys
from PyQt6.QtWidgets import QMenuBar
from PyQt6.QtGui import QAction, QIcon

from ui.settings_window import SettingsWindow

class MenuBar(QMenuBar):
    def __init__(self, parent, options):
        super().__init__()
        self.parent_window = parent
        self.options = options
        self.setup()

    def setup(self):
        menu_bar = self.parent_window.menuBar()

        file_menu = menu_bar.addMenu("&Програма")
        
        settings_action = QAction(QIcon("icons\\settings.png"), '&Налаштування', self.parent_window)
        settings_action.setStatusTip('Налаштування')
        settings_action.setShortcut('Alt+F2')
        settings_action.triggered.connect(self.__open_settings_window)
        file_menu.addAction(settings_action)
        
        exit_action = QAction(QIcon("icons\\close.png"), '&Вихід', self.parent_window)
        exit_action.setStatusTip('Вихід')
        exit_action.setShortcut('Alt+F4')
        exit_action.triggered.connect(lambda: sys.exit(self.destroy()))
        file_menu.addAction(exit_action)

    def __open_settings_window(self):
        self.settings_window = SettingsWindow(self.options, self.parent_window)
        self.settings_window.exec()
