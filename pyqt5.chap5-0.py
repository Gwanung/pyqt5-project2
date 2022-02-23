import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
    
    
    def initUI(self):
        lbl1 = QLabel("zetcode", self) 
        lbl1.move(15, 10)     #왼쪽 맨 윗 부분을 기준 (15,10)-> 아래로15, 오른쪽으로10 이동 
                              #절대 좌표기 때문에 크기 조절을 했을 시 위치 변경x
        lbl2 = QLabel("tutorials", self)
        lbl2.move(35, 40)

        lbl3 = QLabel("for programmers", self)
        lbl3.move(55, 70)          

        self.setGeometry(300, 300, 250, 150)  
        self.setWindowTitle("absolute")
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())