from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

# Main class for project
class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Example project'
        self.minimumWidth = 400
        self.minimumHeight = 140
        self.time = 0
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setMinimumSize(self.minimumWidth, self.minimumHeight)
        self.setWindowIcon(QIcon("images/icon.png"))

        self.widget = QLabel("Hello, World!")
        self.widget.setStyleSheet("font-size: 24pt; color: #922b21;")
        self.widget.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(self.widget)

        self.show()