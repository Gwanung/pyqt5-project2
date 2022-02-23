import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt


class myapp(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()

    
    def initUI(self):

        self.text = "Hello weniv world!"
        self.setWindowTitle("Qpainter")
        self.setGeometry(150, 300, 250, 500)
        self.show()
        

    def paintEvent(self, event):   # 페인트 이벤트는 기본적으로 정의 되어있음.

        paint = QPainter()
        paint.begin(self)         # begin과 end 사이에 그리는 객체를 정의 해주면 됨.
        self.drawText(event, paint)


        paint.end()

    def drawText(self, event, paint):

        paint.setPen(QColor(10, 10, 10))
        paint.setFont(QFont("Decorative", 10))
        paint.drawText(130, 100, "hello world!") # 고정 x 창을 늘리면 변화 함.
        paint.drawText(event.rect(), Qt.AlignCenter, self.text)  # 직사각형 창 , 가운데 정렬




if __name__ == "__main__":


    app= QApplication(sys.argv)
    a= myapp()
    sys.exit(app.exec_())


