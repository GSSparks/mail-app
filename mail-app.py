#!/bin/python

import sys
import keyring
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5 import QtWebEngineWidgets
from PyQt5.QtWidgets import QAction, QMenu, QMainWindow, QWidget, QApplication, QVBoxLayout, QMessageBox, QSplitter
from PyQt5.QtGui import QIcon, QDesktopServices
from PyQt5.QtCore import QUrl

class WebEnginePage(QtWebEngineWidgets.QWebEnginePage):
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

        # Create two QWebEngineViews for the two windows
        self.gmail = QWebEngineView()
        self.page = WebEnginePage(self.gmail)
        self.gmail.setPage(self.page)

        self.calendar = QWebEngineView()
        self.page = WebEnginePage(self.calendar)
        self.calendar.setPage(self.page)

        # Load Gmail and Calendar in the two windows
        self.gmail.load(QUrl("https://mail.google.com/mail/u/0/#inbox"))
        self.calendar.load(QUrl("https://calendar.google.com/calendar/u/0/r?pli=1"))

        # Create a QSplitter and add the two QWebEngineViews to it
        splitter = QSplitter(Qt.Vertical)
        splitter.addWidget(self.gmail)
        splitter.addWidget(self.calendar)

        # Set the QSplitter as the central widget of the main window
        self.setCentralWidget(splitter)

        # Create a vertical layout and add the two QWebEngineViews to it
        #layout = QVBoxLayout()
        #layout.addWidget(self.gmail)
        #layout.addWidget(self.calendar)

        # Set the layout as the central widget of the main window
        #central_widget = QWidget()
        #central_widget.setLayout(layout)
        #self.setCentralWidget(central_widget)

        # Set the window properties
        self.setWindowTitle("Google Mail and Calendar")
        self.resize(900, 720)

    def on_reload(self):
        self.gmail.reload()
        self.calendar.reload()

    def show_about_dialog(self):
        icon_path = "/usr/share/icons/google.png"
        about_box = QMessageBox()
        about_box.setWindowTitle("About Gmail and Calendar App")
        about_box.setText("Gmail and Calendar App\nVersion 1.0\nWritten by Gary Sparks")
        about_box.setIcon(QMessageBox.Information)
        icon = QIcon(icon_path)
        about_box.setWindowIcon(icon)
        about_box.exec_()

if __name__ == "__main__":
    # creating pyQt5 application
    app = QApplication(sys.argv)

    # setting name to the application
    app.setApplicationName("Mail")
    app.setWindowIcon(QIcon("/usr/share/icons/google.png"))
    # creating a main window object
    browser = Browser()
    browser.show()

    # loop
    sys.exit(app.exec_())
