from PyQt6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QWidget
from PyQt6.QtWidgets import QPushButton, QVBoxLayout, QLabel, QHBoxLayout
import sys


def main():
    

    app = QApplication(sys.argv)
# Windows
    window = QWidget()
    window.setWindowTitle("My first Window")
    window.resize(400,300)


# Layouts
    outerLayout = QVBoxLayout()
    layout = QHBoxLayout()
    layout.setBackgroundColor
    layout2 = QHBoxLayout()

# Output
    label = QLabel("New text")
    layout.addWidget(label)

# Input
    button = QPushButton("Click me!")
    layout2.addWidget(button)

# Add to outer layout
    outerLayout.addLayout(layout)
    outerLayout.addLayout(layout2)

    window.setLayout(outerLayout)

    window.show()
    
    app.exec()

if __name__ == "__main__":
    main()
