#!/bin/python

import sys
import os
from PyQt5 import QtWebEngineWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PyQt5.QtWidgets import QAction, QMenu, QMainWindow, QTabWidget, QLabel, QWidget, QApplication, QVBoxLayout, QMessageBox, QSplitter, QSystemTrayIcon, QDockWidget
from PyQt5.QtGui import QIcon, QDesktopServices, QPixmap
from PyQt5.QtCore import Qt, QUrl, QObject

class WebEnginePage(QtWebEngineWidgets.QWebEnginePage):
    def __init__(self, parent=None):
        super().__init__(parent)

    def certificateError(self, error):
        # Ignore SSL certificate errors
        return True

    def javaScriptConsoleMessage(self, level, message, lineNumber, sourceID):
        # Ignore JavaScript console messages
        pass

    def createWindow(self, _type):
        page = WebEnginePage(self)
        page.urlChanged.connect(self.open_browser)
        return page

    def open_browser(self, url):
        page = self.sender()
        QDesktopServices.openUrl(url)
        page.deleteLater()

class Browser(QMainWindow):
    def __init__(self):
        super(Browser, self).__init__()

        # Create a menubar
        menubar = self.menuBar()

        # Add menus to the menubar
        file_menu = menubar.addMenu("File")
        view_menu = menubar.addMenu("View")
        about_menu = menubar.addMenu("Info")

        # Add an "Exit" action to the "File" menu
        exit_action = file_menu.addAction("Exit")
        exit_action.triggered.connect(self.close)

        # Add a Reload action to the View menu
        reload_action = view_menu.addAction("Reload")
        reload_action.setShortcut("Ctrl+R")
        reload_action.triggered.connect(self.on_reload)

        # Add an "About" action to the "File" menu
        about_action = about_menu.addAction("About")
        about_action.triggered.connect(self.show_about_dialog)

        # Create a QTabWidget to hold the QWebEngineView widgets
        self.tab_widget = QTabWidget()
        self.tab_widget.setTabPosition(QTabWidget.West)

        # Create two QWebEngineViews for the two windows
        self.page = WebEnginePage()

        self.gmail = QWebEngineView()
        self.calendar = QWebEngineView()

        self.gmail.setPage(self.page)
        self.calendar.setPage(self.page)

        # Load Gmail and Calendar in the two windows
        self.gmail.load(QUrl("https://mail.google.com/mail/u/0/#inbox"))
        self.calendar.load(QUrl("https://calendar.google.com/calendar/u/0/r?pli=1"))

        # Create a QSplitter and add the two QWebEngineViews to it
        splitter = QSplitter(Qt.Vertical)
        splitter.addWidget(self.gmail)
        splitter.addWidget(self.calendar)

        # Add QSplitter to a new tab in the QTabWidget
        self.tab_widget.addTab(splitter, "Home")

        # Create a QWebEngineView widget for Maps and load the webpage
        self.maps = QWebEngineView()
        self.maps.load(QUrl("https://maps.google.com"))

        # Add the Maps QWebEngineView widget to a new tab in the QTabWidget
        self.tab_widget.addTab(self.maps, "Maps")

        # Set the QTabWidget as the central widget of the main window
        self.setCentralWidget(self.tab_widget)

        # Set the icons for the tabs
        iconHome = os.path.expanduser("~/.icons/home_FILL1_wght400_GRAD0_opsz48.png")
        iconMaps = os.path.expanduser("~/.icons/map_FILL1_wght400_GRAD0_opsz48.png")
        tab_bar = self.tab_widget.tabBar()
        tab_bar.setTabIcon(0, QIcon(iconHome))
        tab_bar.setTabIcon(1, QIcon(iconMaps))

        # Set the window properties
        self.setWindowTitle("The Unofficial Google Apps ... App")
        self.resize(900, 720)

    def on_reload(self):
        self.gmail.reload()
        self.calendar.reload()

    def show_about_dialog(self):
        icon_path = os.path.expanduser("~/.icons/tugaa-48px.png")
        about_box = QMessageBox()
        about_box.setWindowTitle("About the Unofficial Google Apps ... app")
        about_box.setText("This is a Google webapps Python and QT wrapper\nVersion 1.0\nWritten by Gary Sparks, 2023\nNot affiliated with Google.")
        about_box.setIcon(QMessageBox.Information)
        icon = QIcon(icon_path)
        about_box.setWindowIcon(icon)
        about_box.exec_()

if __name__ == "__main__":
    # creating pyQt5 application
    app = QApplication(sys.argv)

    # setting name to the application
    app.setApplicationName("Mail")
    iconApp = os.path.expanduser("~/.icons/tugaa.svg")
    app.setWindowIcon(QIcon(iconApp))

    # creating a main window object
    browser = Browser()
    browser.show()

    # loop
    sys.exit(app.exec_())
