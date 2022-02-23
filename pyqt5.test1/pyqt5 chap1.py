import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class Exam(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):
        btn = QPushButton("asdfasdf",self)
        btn.resize(btn.sizeHint())
        btn.setToolTip('툴팁입니다.<b>안녕하세요.<b>') # html 태그도 가능함!
        btn.move(20,30)

 
        self.setGeometry(300,300,400,500) 
        self.setWindowTitle("첫 번째 학습시간")

        self.show()



app = QApplication(sys.argv)  # 어플리케이션 객체 생성단계 -> 쉘 스크립트 명령줄 제어 부분

w= Exam()
sys.exit(app.exec_()) # 프로그램 깔끔하게 종료  app.exec_() 이벤트 정보 처리 -> 입력과 같은 것들 


