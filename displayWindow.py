from PyQt6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QWidget
from PyQt6.QtWidgets import QPushButton, QVBoxLayout
import sys


def main():
    

    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle("My first Window")
    window.resize(400,300)

    layout = QVBoxLayout()
    button = QPushButton("Click me!")

    layout.addWidget(button)
    window.setLayout(layout)

    window.show()
    
    app.exec()

if __name__ == "__main__":
    main()
