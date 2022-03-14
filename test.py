import sys
import cv2
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class First(QWidget): # 메인 윈도우 


    def __init__(self):

        super().__init__()

        self.Firstwindow()
        
               
        
        # while True:
                
        #     cv2.imshow("video", frame)       # frame의 정보를 video 라는 이름의 창으로 띄움 


        #     cv2.destroyAllWindows()              # 모든 영상 창 닫기 





    
    def Firstwindow(self): 
      

        self.image_label = QLabel(self)         # 배경 예시 이미지 
        self.image_label.setPixmap(QPixmap("img/weniv-licat.png").scaled(300, 300))
        self.image_label.move(150, 100)
        # self.camera = cv2.VideoCapture(0) # frame에 웹캠 정보 저장 , 문제없을 시에 check =True
        # _, frame = self.camera.read()       
        

    

        label1 = QLabel("거북목 교정 프로그램",self)
        
        label1.move(180, 50)
        label1.setFont(QFont("야놀자 야체 B", 30))
        label1.setStyleSheet("Color : #742322")

        image1 = QPixmap("img/weniv-sun.png")
        image1.scaled(30, 30)


        measure_button = QPushButton("실행", self)
        measure_button.setStyleSheet("background-color : #f5f5dc  ; Color : #742322; ")
        measure_button.setGeometry(30, 40, 110, 50)
        

        setting_button = QPushButton("설정", self)    # 두 번째 창 (설정) 버튼 
        setting_button.setGeometry(30, 140, 110, 50)
        setting_button.setStyleSheet("background-color : #f5f5dc  ; Color : #742322; ")
        setting_button.clicked.connect(self.Secondwindowbutton)

        grape_button = QPushButton("통계", self)  # 세 번째 창 (통계) 버튼 
        grape_button.setGeometry(30, 240, 110, 50)
        grape_button.setStyleSheet("background-color : #f5f5dc  ; Color : #742322; ")
        grape_button.clicked.connect(self.Thirdwindowbutton)

        ex_buttom = QPushButton("설명", self)  # 네 번째 창 (설명) 버튼
        ex_buttom.setGeometry(30, 340, 110, 50)
        ex_buttom.setStyleSheet("background-color : #f5f5dc  ; Color : #742322; ")
        ex_buttom.clicked.connect(self.Fourthwindowbutton)

        # start_button = QPushButton("start", self)
        # start_button.move(380, 90)

    
        # stop_button = QPushButton("stop", self)
        # stop_button.move(380, 190)


        # reset_button = QPushButton("reset", self)
        # reset_button.move(380, 290)
        self.setWindowIcon(QIcon("img/weniv-gary.png"))
        self.setWindowTitle("거북목 교정 프로그램")
        self.setGeometry(250, 250, 500, 450)
        self.show()



    def Secondwindowbutton(self):

        self.hide() #메인 윈도우 숨김
        self.second = Second()
        # self.second.exec_()
        # self.show()
    
    def Thirdwindowbutton(self):
        self.hide()
        self.third = Third()

    
    def Fourthwindowbutton(self):
        self.hide()
        self.fourth = Fourth()




class Second(QWidget): # 설정을 담당할 두 번째 윈도우 

    def __init__(self):

        super().__init__()

        self.Secondwindow()

    
    def Secondwindow(self):   
        
        main_button = QPushButton("Home ", self)
        main_button.move(30, 30)
        main_button.clicked.connect(self.Firstwindowbutton)

        sound_set_button = QPushButton("sound 설정 ", self)
        sound_set_button.setGeometry(30, 80, 400, 100)

        proportion_ms_button = QPushButton("나의 비율 측정 하기", self)
        proportion_ms_button.setGeometry(30, 200, 400 ,100)

        cam_set_button = QPushButton("cam 설정", self)
        cam_set_button.setGeometry(30, 320, 400, 100)

     
        self.setWindowIcon(QIcon("img/weniv-gary.png"))
        self.setWindowTitle("설정")
        self.setGeometry(250, 250, 500, 450)
        self.show()
        

    def Firstwindowbutton(self):
        
        self.hide()
        self.first = First()



class Third(QWidget):    # 통계를 담당할 세 번째 윈도우

    def __init__(self):

        super().__init__()

        self.Thirdwindow()

    def Thirdwindow(self):

        
        self.setWindowIcon(QIcon("img/weniv-gary.png"))
        self.setWindowTitle("통계")
        self.setGeometry(250, 250, 500, 450)
        self.show()
        






class Fourth(QWidget): # 설명을 담당할 네 번째 윈도우

    def __init__(self):

        super().__init__()

        self.Fourthwindow()

    
    def Fourthwindow(self):
        
        ex_label = QLabel("거북목 교정 프로그램", self)
        ex_label.move(170 ,10)
        ex_label.setFont(QFont("야놀자 야체 B", 20))
        ex_label.setStyleSheet("Color : #742322; ")

        image_label1 = QLabel(self)
        image_label1.setPixmap(QPixmap("img/ex1").scaled(220, 350))
        image_label1.move(0, 70)

        ex_label2 = QLabel("요즘 같은 코로나로 인한 \n비대면 수업 시기에 거북목에 취약할 수 있습니다. \n따라서 저희는 이러한 거북목을 방지하기 위해서 \n이렇게 프로그램을 만들게 되었습니다. ", self)
        
        ex_right_button = QPushButton("->", self)
        ex_right_button.move(400, 420)
        ex_right_button.clicked.connect(self.Nextpage)


        hbox= QHBoxLayout()      #수평으로 배치 
        hbox.addWidget(image_label1)
        hbox.addWidget(ex_label2)
        self.setLayout(hbox)
      

        self.setWindowIcon(QIcon("img/weniv-gary.png"))
        self.setWindowTitle("설명")
        self.setGeometry(250, 250, 500, 450)
        self.show()

    def Nextpage(self):

        self.hide()
        self.nextpage = NextPage() 



class NextPage(QWidget):

    def __init__(self):

        super().__init__()

        self.Nextexwindow()


    def Nextexwindow(self):


        ex_label = QLabel("거북목 교정 프로그램", self)
        ex_label.move(170 ,10)
        ex_label.setFont(QFont("야놀자 야체 B", 20))
        ex_label.setStyleSheet("Color : #742322; ")



        image_label1 = QLabel(self)             
        image_label1.setPixmap(QPixmap("img/ex1").scaled(220, 350))
        image_label1.move(0, 70)

        ex_right_button = QPushButton("->", self)
        ex_right_button.move(400, 420)
        # ex_right_button.clicked.connect(self)    
        

        ex_left_button = QPushButton("<-", self)
        ex_left_button.move(300, 420)
        # ex_left_button.clicked.connect(self.Previousbutton)

        ex_label2 = QLabel("ex", self)

        hbox= QHBoxLayout()      #수평으로 배치 
        hbox.addWidget(image_label1)
        hbox.addWidget(ex_label2)
        self.setLayout(hbox)
            
    
        self.setWindowIcon(QIcon("img/weniv-gary.png"))
        self.setWindowTitle("설명2")
        self.setGeometry(250, 250, 500, 450)
        self.show()







if  __name__ == "__main__":


    
    app = QApplication(sys.argv) 
    app.setFont(QFont("야놀자 야체 B"))
    a= First()
    sys.exit(app.exec_())