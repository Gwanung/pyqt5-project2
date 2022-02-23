import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QPixmap


class myapp(QWidget):

    def __init__(self):

        super().__init__()


        self.initUI()

    
    def initUI(self):

        testbutton = QPushButton("버튼입니다", self)
        testbutton.setGeometry(80, 80, 80, 80)

        self.setWindowTitle("기본위치")
        self.setGeometry(200, 200, 200, 200)
        self.show()

    

if __name__ == "__main__":

    app = QApplication(sys.argv)
    a = myapp()
    sys.exit(app.exec_())