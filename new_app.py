import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QTextEdit
from PyQt6.QtWidgets import QMenu
from PyQt6.QtGui import QAction
# https://www.pythonguis.com/tutorials/pyqt6-signals-slots-events/

class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__()
            self.label = QLabel("Click in this window")
            self.setCentralWidget(self.label)
            self.setMouseTracking(True)

            self.customContextMenyRequested.connect(self.on_context_meny)

        def mousePressEvent(self, e):
            if e.button() == Qt.MouseButton.LeftButton:
                 self.label.setText("mousePressEvent LEFT")

            elif e.button() == Qt.MouseButton.MiddleButton:
                # handle the middle-button press in here.
                self.label.setText("mousePressEvent MIDDLE")

            elif e.button() == Qt.MouseButton.RightButton:
                 # handle the right-button press in here.
                 self.label.setText("mousePressEvent RIGHT")

        def mouseReleaseEvent(self, e):
            if e.button() == Qt.MouseButton.LeftButton:
                self.label.setText("mouseReleaseEvent LEFT")

            elif e.button() == Qt.MouseButton.MiddleButton:
                self.label.setText("mouseReleaseEvent MIDDLE")

            elif e.button() == Qt.MouseButton.RightButton:
                self.label.setText("mouseReleaseEvent RIGHT")

        def mouseDoubleClickEvent(self, e):
            if e.button() == Qt.MouseButton.LeftButton:
                self.label.setText("mouseDoubleClickEvent LEFT")

            elif e.button() == Qt.MouseButton.MiddleButton:
                self.label.setText("mouseDoubleClickEvent MIDDLE")
            elif e.button() == Qt.MouseButton.RightButton:
                self.label.setText("mouseDoubleClickEvent RIGHT")

        def contextMenuEvent(self, e):
            context = QMenu(self)
            context.addAction(QAction("Test1", self))
            context.addAction(QAction("Test1", self))
            context.addAction(QAction("Test1", self))
            context.ecex(e.globalPos())

        def on_context_menu(self, pos):
            context = QMenu(self)
            context.addAction(QAction("test1", self))
            context.addAction(QAction("test2", self))
            context.addAction(QAction("test3", self))
            context.exec(self.mapToGlobal(pos))

app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
