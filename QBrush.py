import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QFont, QPen , QBrush
from PyQt5.QtCore import Qt


class myapp(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()

    
    def initUI(self):

        self.text = "Hello weniv world!"
        self.setWindowTitle("Qpainter")
        self.setGeometry(300, 300, 500, 500)
        self.show()
        

    def paintEvent(self, event):   # 페인트 이벤트는 기본적으로 정의 되어있음.

        paint = QPainter()
        paint.begin(self)         # begin과 end 사이에 그리는 객체를 정의 해주면 됨.
        self.drawFigure(paint)

        paint.end()

    def drawFigure(self, paint):

        paint.setBrush(QColor(10, 250, 40))
        paint.setPen(QColor(Qt.red))
        paint.drawRect(20, 30, 100, 100)

        paint.setBrush(QColor(10, 250, 40))
        paint.setPen(QColor(Qt.red))
        paint.drawRoundedRect(150, 20, 100, 100, 30, 30)

        paint.setBrush(QBrush(Qt.CrossPattern))
        paint.setPen(QColor(Qt.red))
        paint.drawRoundedRect(300, 100, 100, 100, 30, 30)   
    
        paint.setBrush(QColor(Qt.darkGreen))
        paint.setPen(QPen(QColor(Qt.red), 2, Qt.DotLine))
        paint.drawEllipse(150, 200, 180, 180)   
 
 



if __name__ == "__main__":


    app= QApplication(sys.argv)
    a= myapp()
    sys.exit(app.exec_())


