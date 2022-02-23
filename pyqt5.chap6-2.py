import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        
        grid = QGridLayout()
        grid.setSpacing(10)  # 격자 빈공간을 10만큼 두겠다.

        x = 0  # 변수 2개 
        y = 0
        
        self.text = "x: {0} y: {1}".format(x,y)  

        self.label = QLabel(self.text, self)  
        grid.addWidget(self.label, 0, 0, Qt.AlignTop) 
        

        self.setMouseTracking(True)  # 마우스 트래킹 (포인터를 따라감.)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 200)
        self.setWindowTitle("Event object")
        self.show()

    def mouseMoveEvent(self, e): #마우스가 움직일 때를 e로 넘겨받겠다. 

        x = e.x()
        y = e.y()

        text = "x: {0}, y: {1}".format(x,y) 
        self.label.setText(text)

if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())



