from email.charset import QP
import sys
import pyautogui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import QCoreApplication

class FishAuto(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()

    
    def initUI(self):

        self.pack_count = 0
        self.click_count = 0

        self.mainImage()
        self.fishPackNumber()
        self.packButton()

        self.setWindowTitle("생선 자동 프로그램")
        self.setWindowIcon(QIcon("img/캣네생선.png"))
        self.setGeometry(800, 300 ,580 ,500)
        self.show()

    def mainImage(self):
        
        self.mainImageL = QLabel(self)
        self.mainImageL.setPixmap(QPixmap("img/weniv-licat.png").scaled(35, 44))
        self.mainImageL.move(10, 10)


    def fishPackNumber(self):
        
        self.fish_packL = QLabel("00 마리가 포장 되었습니다.", self)
        self.fish_packL.setFont(QFont("Helvetica", pointSize=22, weight=2))
        self.fish_packL.move(30, 70)        


    def packButton(self):
        
        self.fish_readyB = QPushButton("생선 준비 버튼", self)
        self.fish_readyB.move(30, 150)
        self.fish_readyB.setFixedSize(250, 40)

        self.fish_SB = QPushButton("생선 다듬기 버튼", self)
        self.fish_SB.move(300, 150)
        self.fish_SB.setFixedSize(250, 40)

        self.fish_PB = QPushButton("생선 준비 버튼", self)
        self.fish_PB.move(30, 200)
        self.fish_PB.setFixedSize(520, 40)

        self.fish_startB = QPushButton("생선 준비 버튼", self)
        self.fish_startB.move(300, 300)
        self.fish_startB.setFixedSize(250, 40)

        self.inputC = QLineEdit(self)
        self.inputC.setPlaceholderText("클릭 간격(초)")
        self.inputC.move(30 ,300)

        self.inputC_EX = QLabel("몇 초 간격으로 포장 할 지 입력하세요.", self)
        self.inputC_EX.setFont(QFont("Helvetica", pointSize=12))    
        self.inputC_EX.move(30, 340)




if __name__ == "__main__":

    app =QApplication(sys.argv)
    a = FishAuto()
    sys.exit(app.exec_())