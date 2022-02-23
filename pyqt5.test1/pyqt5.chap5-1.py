import sys
from PyQt5.QtWidgets import ( QWidget, QPushButton,QHBoxLayout ,
                                        QVBoxLayout,QApplication )  # hbox 가로 ,vbox 세로 (쌓이는방향)


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
    
    
    def initUI(self):
        ok_button = QPushButton("ok")
        cancel_button = QPushButton("cancel")  # 버튼 2개 생성 

        hbox =QHBoxLayout()
        hbox.addStretch(1)   # 버튼 2개가 차지하지 않고 있는 공간만큼 늘어남
        hbox.addWidget(ok_button)
        hbox.addWidget(cancel_button) 

        vbox = QHBoxLayout()     
        vbox.addStretch(1)  # 버튼들은 항상 오른쪽하단에 있게됨.
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 300 ,150)
        self.setWindowTitle("buttons")
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())