import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.setGeometry(300, 300, 250 ,150)
        self.setWindowTitle("Event handler")
        self.show()

    def keyPressEvent(self, e):       # 키가 눌렸을 때 발생되는 메소드
        if e.key() == Qt.key_Escape:  # 키의 값이 아스키 코드화 되서 값이 들어감.
                                      
            self.close()

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
        

    