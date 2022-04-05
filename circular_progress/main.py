import sys
import os
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from circular_progress import CircularProgress



class Main(QMainWindow):

    def __init__(self):

        QMainWindow.__init__(self)

        self.resize(700, 500)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.container =QFrame()
        self.container.setStyleSheet("background-color: transparent")
        self.layout = QVBoxLayout()

        self.progress = CircularProgress()
        self.progress.value = 50
        self.progress.suffix = "%"
        self.progress.font_size = 12
        self.progress.width = 300
        self.progress.height = 300
        self.progress.text_color = 0xFFFFFF
        self.progress.progress_color = 0xFFFFFF
        self.progress.progress_rounded_cap = True
        self.progress.setMinimumSize(self.progress.width, self.progress.height)
        self.progress.add_shadow(True)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 100)
        self.slider.valueChanged.connect(self.change_value)
# Changed.connect(self.change_value)
        self.layout.addWidget(self.progress, Qt.AlignCenter, Qt.AlignCenter)
        self.layout.addWidget(self.slider, Qt.AlignCenter, Qt.AlignCenter)


        self.container.setLayout(self.layout)
        self.setCentralWidget(self.container)

        self.show()
    
    def change_value(self, value):
        self.progress.set_value(value)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec_())