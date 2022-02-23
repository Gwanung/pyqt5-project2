import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMenu
from PyQt5.QtCore import QCoreApplication 
class Exam(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage("안녕하세요") 

 
        menu = self.menuBar()               # 메뉴바 생성 
        menu_file = menu.addMenu("File")    # 그룹생성
        menu_edit = menu.addMenu("Edit")    # 그룹생성  

        file_exit = QAction("Exit",self)    # 메뉴 객체 생성
        file_exit.setShortcut("ctrl+Q")      # 메모리 안에 만들어 놓은 것 (보이지는 않음)
                                             # setShortcut은 안에 값을 쓰면 꺼짐
        file_exit.setStatusTip("누르면 영원히 빠이빠이")  
        new_txt = QAction("텍스트 파일", self)
        new_py = QAction("파이썬 파일", self)   # 이 5줄은 액션이 가능한 메뉴자체를 생성
        
        file_exit.triggered.connect(QCoreApplication.instance().quit)  #exit 를선택하면 꺼짐.

        file_new = QMenu("New", self)      # 서브그룹 

        
        file_new.addAction(new_txt)
        file_new.addAction(new_py)    #이 2줄은서브메뉴 추가 

        menu_file.addMenu(file_new)    #그룹을 만듬.  addmenu 
        menu_file.addAction(file_exit) # 메뉴 등록! (exit 기능들)
                                       # addmenu와 addaction의 구분하기!

                                    
    
        self.resize(450, 400)
        self.show()

app = QApplication(sys.argv)
w =  Exam()

sys.exit(app.exec_())
