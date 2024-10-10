import sys
from PyQt6.QtWidgets import QMenuBar
from PyQt6.QtGui import QAction

# from ui.settings_window import SettingsWindow

class MenuBar(QMenuBar):
    def __init__(self, window):
        super().__init__()
        self.parent_window = window

    def install(self):
        menu_bar = self.parent_window.menuBar()

        file_menu = menu_bar.addMenu("&Програма")
        # help_menu = menu_bar.addMenu('&Допомога')
        
        # exit_action = QAction('&Налаштування', self.parent_window)
        # exit_action.setStatusTip('Налаштування')
        # exit_action.setShortcut('Alt+F2')
        # exit_action.triggered.connect(self.__open_settings_window)
        # file_menu.addAction(exit_action)
        
        exit_action = QAction('&Вихід', self.parent_window)
        exit_action.setStatusTip('Вихід')
        exit_action.setShortcut('Alt+F4')
        exit_action.triggered.connect(lambda: sys.exit(self.destroy()))
        file_menu.addAction(exit_action)

    # def __open_settings_window(self):
    #     self.settings_window = SettingsWindow(self)
    #     self.settings_window.exec()

    #     self.parent_window.refresh()