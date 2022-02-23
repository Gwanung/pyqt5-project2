from csv import list_dialects
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout
from PyQt5.QtGui import QPixmap



class myapp(QWidget):

    
    def __init__(self):

        super().__init__()

        self.initUI()

    
    def initUI(self):
        licat = QLabel()
        pie = QLabel()
        sun = QLabel()

        licat.setStyleSheet(

            "border-style: solid;"
            "border-width: 3px;"
            "border-color: red;"
            "border-radius: 3px;"
            "image: url(img/weniv-licat.png)"
        )

        pie.setStyleSheet(
            "border-style: double;"
            "border-width: 5px;"
            "border-color: blue;"
            "background-color: #87CEFA;"
            "image: url(img/weniv-pie.png)"
        )

        sun.setStyleSheet(

            "border-style: dot-dot-dash;"
            "border-width: 5px;"
            "border-color: green;"
            "border-radius: 3px;"
            "background-color: beige;"
            "image: url(img/weniv-sun.png)"

        )

        hbox = QHBoxLayout()
        hbox.addWidget(licat)
        hbox.addWidget(pie)
        hbox.addWidget(sun)

        self.setLayout(hbox)

        self.setGeometry(400, 400, 500, 400)
        self.setWindowTitle("라벨 꾸미기")
        self.show()

if __name__ == "__main__":

    app = QApplication(sys.argv)
    a = myapp()
    sys.exit(app.exec_())

    