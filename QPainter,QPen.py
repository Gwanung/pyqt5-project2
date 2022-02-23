from email.charset import QP
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QFont , QPen
from PyQt5.QtCore import Qt


class myapp(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()

    
    def initUI(self):

        
        self.setWindowTitle("Qpainter")
        self.setGeometry(300, 300, 500, 500)
        self.show()
        

    def paintEvent(self, event):   # 페인트 이벤트는 기본적으로 정의 되어있음.

        paint = QPainter()
        paint.begin(self)         # begin과 end 사이에 그리는 객체를 정의 해주면 됨.
        self.drawLine(paint)


        paint.end()

    def drawLine(self, paint):

        pen = QPen(Qt.blue, 4, Qt.SolidLine)
        paint.setPen(pen)
        paint.drawLine(100, 40, 400, 40)  # x,y x,y  


        pen.setStyle(Qt.DashLine)
        pen.setColor(Qt.yellow)
        paint.setPen(pen)
        paint.drawLine(100, 80, 400, 80)


        pen.setStyle(Qt.DashDotLine)
        pen.setColor(Qt.red)
        paint.setPen(pen)
        paint.drawLine(100, 120, 400, 120)     # 차트 만들 때 사용 가능.

        pen.setStyle(Qt.DashDotDotLine)
        pen.setColor(Qt.darkMagenta)
        paint.setPen(pen)
        paint.drawLine(100, 160, 400, 160)

        pen.setStyle(Qt.CustomDashLine)
        pen.setDashPattern([1, 4, 5, 4])   #  선의  (1,3 번째 )->  크기  |  (2,4번째) ->간격
        pen.setColor(Qt.darkGray)
        pen.setWidth(8)
        paint.setPen(pen)
        paint.drawLine(100, 200, 400, 200)


if __name__ == "__main__":


    app= QApplication(sys.argv)
    a= myapp()
    sys.exit(app.exec_())


