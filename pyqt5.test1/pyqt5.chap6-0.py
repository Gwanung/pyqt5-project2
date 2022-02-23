import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget,QLCDNumber, QSlider, 
                                     QVBoxLayout , QApplication)



class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        lcd = QLCDNumber(self)  
        sld = QSlider(Qt.Horizontal, self) # H는 가로에 해당하는 부분(슬라이더 가로형태)

        vbox = QVBoxLayout()  # QVBoxLayout() 는 세로로 쌓는 형태
        vbox.addWidget(lcd)   
        vbox.addWidget(sld)

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display) # 슬라이더 값이 변경되었을 때 연결 될 슬롯을 써줌.

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("signal and slot") 
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())