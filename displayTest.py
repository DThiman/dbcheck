import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit
from PyQt6.QtWidgets import QVBoxLayout, QWidget
from random import choice


window_titles = [
    'my app',
    'still my app',
    'Again, Still my app',
    'Was this not my app??',
    'Why do you keep clicking that???'
]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.n_times_clicked = 0

        self.setWindowTitle("MyApp")

        self.label = QLabel()

        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)
        self.button = QPushButton("Press me")
        self.button.clicked.connect(self.the_button_was_clicked)

        self.windowTitleChanged.connect(self.the_window_title_changed)
        
        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)


        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def the_button_was_clicked(self):
        self.button.setText("Cliecked already")
        print("1: Button clicked!")

        new_window_title = choice(window_titles)

        self.setWindowTitle(new_window_title)
        print("3: title changed in button_was_clicked")
        
    def the_window_title_changed(self, window_title):
        print("2: The window title changed to %s" % window_title)

        if window_title == 'Why do you keep clicking that???':
            self.button.setDisabled(True)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
