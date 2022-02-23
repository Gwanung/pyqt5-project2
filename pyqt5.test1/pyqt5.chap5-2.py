import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout ,
                                QPushButton , QApplication)



class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
    def initUI(self):

        grid = QGridLayout()
        self.setLayout(grid)

        names = [ "cls", "bck", " ", "close",
                    "7", "8", "9", "/",
                    "4", "5", "6", "*",
                    "1", "2", "3", "-",
                    "0", ".", "#", "+" ]
        positions = [(i,j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):    # zip은 리스트와 튜플을 묶어줌

            if name == " " :   
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position) # *position은 (0,3)이 아닌 0,3을 넘기게 됨

        self.move(300, 150)
        self.setWindowTitle("calculator")
        self.show()

if __name__ == "__main__":    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

