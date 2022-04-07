import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import cv2, numpy, time
# from keras.models import load_model
from keras.utils import np_utils
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Activation
import numpy as np
from numpy import argmax
from tensorflow import keras
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

class MainW(QWidget):

    def __init__(self):

        super().__init__()


        self.firstUI()

    

    def firstUI(self):

        self.setStyleSheet("background-color: #e2e2e2")  # 전체 배경

        self.main_image_label = QLabel(self)
        self.main_image_label.setPixmap(QPixmap("./main.png"))  # 나중에 수정할거임 (주말 디자인)

        self.start_button = QPushButton("시작", self)       # 시작 버튼
        self.start_button.clicked.connect(self.secondWindow)
        self.start_button.setMinimumSize(150, 70)
        self.start_button.setFont(QFont("메이플스토리", 20))
        self.start_button.setStyleSheet("background-color: #C8FFB5")

        self.graph_button = QPushButton("통계", self)       # 통계 버튼
        self.graph_button.clicked.connect(self.thirdWindow)
        self.graph_button.setMinimumSize(150, 70)
        self.graph_button.setFont(QFont("메이플스토리", 20))
        self.graph_button.setStyleSheet("background-color: #C8FFB5")

        self.set_button = QPushButton("설정", self)         # 설정 버튼
        self.set_button.clicked.connect(self.fourthWindow)
        self.set_button.setMinimumSize(150, 70)
        self.set_button.setFont(QFont("메이플스토리", 20))
        self.set_button.setStyleSheet("background-color: #C8FFB5")

        self.ex_button = QPushButton("설명", self)          # 설명 버튼
        self.ex_button.clicked.connect(self.fifthWindow)
        self.ex_button.setMinimumSize(150, 70)
        self.ex_button.setFont(QFont("메이플스토리", 20))
        self.ex_button.setStyleSheet("background-color: #C8FFB5")

        self.num_label = QLabel(self)

        self.login_button = QPushButton("내 정보 등록하기!", self)
        self.login_button.clicked.connect(self.sixthWindow)
        self.login_button.setMinimumSize(40, 40)  # 가로 길이는 라벨때문에 의미없음
        self.login_button.setFont(QFont("메이플스토리", 12))
        self.login_button.setStyleSheet("background-color: #C8FFB5")



    
        hbox = QHBoxLayout()  #수평 박스 
        hbox.addStretch(10)
        hbox.addWidget(self.main_image_label)
        hbox.addStretch(1)

        vbox = QVBoxLayout() #수직 박스
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(self.start_button)
        hbox2.addStretch(2)
        hbox2.addWidget(self.graph_button)
        hbox2.addStretch(1)

        vbox.addLayout(hbox2)
        vbox.addStretch(2)

        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        hbox3.addWidget(self.set_button)
        hbox3.addStretch(2)
        hbox3.addWidget(self.ex_button)
        hbox3.addStretch(1)

        vbox.addLayout(hbox3)
        vbox.addStretch(1)

        hbox4 = QHBoxLayout()
        hbox4.addWidget(self.num_label)
        hbox4.addStretch(1)
        hbox4.addWidget(self.login_button)

        vbox.addLayout(hbox4)
        
        
        self.setLayout(vbox)

        self.show()
        self.setGeometry(400, 200, 800, 600)

    def secondWindow(self):
        self.hide()
        self.second = SecondW()

    def thirdWindow(self):
        self.hide()
        self.third = ThirdW()

    def fourthWindow(self):
        self.hide()
        self.fourth = FourthW()

    def fifthWindow(self):
        self.hide()
        self.fifth = FifthW()

    def sixthWindow(self):
        self.hide()
        self.sixth = SixthW()

class SecondW(QWidget):   # 시작버튼 (카메라 거북목 판별)

    def __init__(self):

        super().__init__()
        self.secondUI()

    def secondUI(self):

        self.setGeometry(400, 200, 800, 600)
        self.show()
        self.cam=cv2.VideoCapture(0)
        self.cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) 
        self.timer=QTimer()
        from keras.models import load_model #모델 들고오기
        self.model = keras.models.load_model('./test-model2')
        self.fps=60
        self.turtleScale=0

        self.frame_Camera = QLabel(self)
        self.frame_Camera.resize(640,480)
        self.frame_Camera.setScaledContents(True)

        self.setStyleSheet("background-color: #C9E5CE")  # 전체 배경
        self.home_icon = QIcon("./icon/cil-house")
        self.home_button1 = QPushButton("home", self)
        self.home_button1.setIcon(self.home_icon)
        # self.home_button1.setIconSize(QSize(10,10))
        self.home_button1.setStyleSheet("background-color: #C8FFB5")
        self.home_button1.clicked.connect(self.mainWindow)

        self.button_On = QPushButton("ON",self)
        self.button_On.clicked.connect(self.clickOn)

        self.button_Off = QPushButton("OFF",self)
        self.button_Off.clicked.connect(self.clickOff)

        self.progressBar_turtle_scale=QProgressBar(self)
        
        hbox = QHBoxLayout()
        hbox.addWidget(self.home_button1)
        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        # vbox.addStretch(1)
        vbox.addWidget(self.frame_Camera)
        # vbox.addStretch(1)
        
        hbox2 = QHBoxLayout()
        # hbox2.addStretch(1)
        hbox2.addWidget(self.button_On)
        hbox2.addWidget(self.button_Off)
        # hbox2.addStretch(2)
        hbox2.addWidget(self.progressBar_turtle_scale)
        # hbox2.addStretch(1)
    
        vbox.addLayout(hbox2)
        vbox.addStretch(1)

        self.setLayout(vbox)

    def clickOn(self):
        self.timer.timeout.connect(self.nextFrameCamera)
        self.timer.start(int(1000/self.fps))
    def nextFrameCamera(self):
        retval, frame = self.cam.read()
        if not retval:
            self.frame_Camera.setPixmap()
            return
        frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        frame=cv2.flip(frame,1)
        pix=QPixmap.fromImage(QImage(frame,frame.shape[1],frame.shape[0],QImage.Format_RGB888))
        self.frame_Camera.setPixmap(pix)
        frame = cv2.resize(frame, dsize=(320,240))
        frame=frame.reshape(1,320,240,3).astype('float32')/255.0
        self.turtleScale=self.model.predict(frame)
        self.timer.timeout.connect(self.changeProgressBar)
        
    def changeProgressBar(self):
        
        self.progressBar_turtle_scale.setValue(int(np.round(self.turtleScale[0][0],2)*100))
        print((int(np.round(self.turtleScale[0][0],2)*100)))

    def clickOff(self):
        self.timer.stop()

    def mainWindow(self):
        self.hide()
        self.frist = MainW()

class ThirdW(QWidget):

    def __init__(self):

        super().__init__()
        self.thirdUI()

    def thirdUI(self):
        
        self.home_button2 = QPushButton("home", self)
        self.home_button2.clicked.connect(self.mainWindow2)
        self.setGeometry(400, 200, 800, 600)
        self.show()

    def mainWindow2(self):
        self.hide()
        self.frist2 = MainW()

class FourthW(QWidget):

    def __init__(self):

        super().__init__()
        self.fourthUI()

    def fourthUI(self):
        pass

class FifthW(QWidget):

    def __init__(self):

        super().__init__()
        self.fifthUI()

    def fifthUI(self):
        pass


class SixthW(QWidget):

    def __init__(self):

        super().__init__()
        self.sixthUI()

    def sixthUI(self):
        pass
        
if __name__ == '__main__':

    app = QApplication(sys.argv)
    mainWindow = MainW()
    sys.exit(app.exec_())



