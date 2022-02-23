import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
                                    QTextEdit, QGridLayout, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()
        
        self.initUI()


    def initUI(self):

        title = QLabel("title")
        author = QLabel("author")
        review = QLabel("review")    #3개의 레이블 


        title_edit = QLineEdit()
        author_edit = QLineEdit()     # 텍스트 상자
        review_edit = QTextEdit()     # 조금 더 긴 텍스트 상자

        grid = QGridLayout()
        grid.setSpacing(10)    #객체의 사이사이의 공간 여백

        grid.addWidget(title, 1, 0)  
        grid.addWidget(title_edit, 1, 1)

        grid.addWidget(author,2, 0)
        grid.addWidget(author_edit, 2, 1)

        grid.addWidget(review, 3, 0)      
        grid.addWidget(review_edit, 3, 1, 5, 1)  

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 300) 

        self.setWindowTitle("review")
        self.show()

if __name__ == "__main__":    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


