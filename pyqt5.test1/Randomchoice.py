from email.charset import QP
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QToolTip
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import QCoreApplication
import random



class exam(QWidget):

    def __init__(self):

        super().__init__()
        
        self.initUI()


    def initUI(self):
        self.image()
        self.button()
        self.tooltips()
        self.number()

        self.setWindowTitle("대표 선출")
        self.setWindowIcon(QIcon("ㄹㄸ.png"))
        self.setGeometry(500, 500, 400, 400)
        self.show()

    

    def image(self):
        self.images = QLabel(self)
        self.images.setPixmap(QPixmap("ㄹㄸ.png").scaled(35, 44))
        self.images.move(100, 10)


    def button(self):
        self.buttons = QPushButton("대표 선출", self)
        self.buttons.setFixedSize(340, 40)
        self.buttons.move(30, 290)
        self.buttons.clicked.connect(self.choice)

        self.endbutton = QPushButton("종료 선출", self)
        self.endbutton.setFixedSize(340, 40)
        self.endbutton.move(30, 340)
        self.endbutton.clicked.connect(self.close)


    def tooltips(self):
        self.buttons.setToolTip(' 이 버튼을 누르면 대표를 선출합니다.\n주의하세요 '
        '되돌릴 수 없습니다.')
        self.endbutton.setToolTip("이 버튼을 종료합니다. ")
        self.images.setToolTip("로또 번호")
        self.setToolTip("이곳은 Qwidget")


    def number(self):
        
        self.n_label = QLabel("000", self)
        self.n_label.setFont(QFont("Helvetica", pointSize=75, weight=2))
        self.n_label.move(80, 100)

    def choice(self):

        s = str(random.randint(1, 1000))
        self.n_label.setText(s)

    def close(self):

        return QCoreApplication.instance().quit()


if __name__ == "__main__":

    app = QApplication(sys.argv)
    a = exam()
    sys.exit(app.exec_())

    
