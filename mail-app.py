#!/bin/python

import sys
import keyring
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QVBoxLayout
from PyQt5.QtGui import QIcon

class Browser(QMainWindow):
    def __init__(self):
        super(Browser, self).__init__()

        # Create two QWebEngineViews for the two tabs
        self.gmail = QWebEngineView()
        self.calendar = QWebEngineView()

        # Load Gmail and Calendar in the two tabs
        self.gmail.load(QUrl("https://mail.google.com/mail/u/0/#inbox"))
        self.calendar.load(QUrl("https://calendar.google.com/calendar/u/0/r?pli=1"))

        # Create a vertical layout and add the two QWebEngineViews to it
        layout = QVBoxLayout()
        layout.addWidget(self.gmail)
        layout.addWidget(self.calendar)

        # Set the layout as the central widget of the main window
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Set the window properties
        self.setWindowTitle("Google Mail and Calendar")
        self.resize(900, 720)

if __name__ == "__main__":
    # creating pyQt5 application
    app = QApplication(sys.argv)

    # setting name to the application
    app.setApplicationName("Mail")
    app.setWindowIcon(QIcon("/usr/share/icons/google.png"))
    # creating a main window object
    browser = Browser()
    browser.setWindowFlags(Qt.FramelessWindowHint)
    browser.show()

    # loop
    sys.exit(app.exec_())
