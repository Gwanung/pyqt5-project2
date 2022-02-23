import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtCore import QCoreApplication


class Exam(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn = QPushButton("push me!", self)
        btn.resize(btn.sizeHint())
        btn.move(50,50)
        btn.clicked.connect(QCoreApplication.instance().quit)  #클릭이 되었을 때 꺼짐

        self.resize(500,500)
        self.setWindowTitle("두 번째 시간")
        
        self.show()

    def closeEvent(self, QcloseEvent): 

        ans=  QMessageBox.question(self,"종료 확인", "종료 하시겠습니까?" , 
                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)


        if ans == QMessageBox.Yes: 
            QcloseEvent.accept() # yes를 누르면 꺼짐

        else:
            QcloseEvent.ignore()  # no를 누르면 안꺼짐


    
app =QApplication(sys.argv)
w = Exam()
sys.exit(app.exec_())     