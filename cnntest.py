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

#(none,none,none,none) 이게 (batch_size,width,height,channels)이거임
#flow_from_directory여기 리턴값 찾다가 나옴
#https://stackoverflow.com/questions/44842097/how-to-get-list-of-values-in-imagedatagenerator-flow-from-directory-keras

#해결법 다 찾음! flow_from뭐라 리턴값만 찾아서 모양 바꿔주면 끝!

#데이터 전처리 필요한거
#마스크 유무
#모자 유무
#배경 차이

from tensorflow import keras

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("HI")
        self.setGeometry(150,150,650,540)
        self.initUI()

    def initUI(self):
        #초기값
        self.cam=cv2.VideoCapture(0)
        self.cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) 
        self.timer=QTimer()
        from keras.models import load_model #모델 들고오기
        self.model = keras.models.load_model('./test-model2')
        self.fps=60
        self.turtleScale=0
        
        #region layoutH1
        #홈버튼
        self.button_Home = QPushButton("Home",self)
        self.button_Home.clicked.connect(self.clickHome)
        # self.button_Home.setIcon(QIcon('./image/home.png'))
        self.button_Home.size()
        # self.button.setStyleSheet("background-image : url(image.png);")
        #endregion
        
        
        #region layoutV1
        self.frame_Camera = QLabel(self)
        self.frame_Camera.resize(640,480)
        self.frame_Camera.setScaledContents(True)   #영상 크기에 맞게 자동 조절
        #endregion
        
        
        #region layoutH2
        #On
        self.button_On = QPushButton("ON",self)
        self.button_On.clicked.connect(self.clickOn)
        
        #Off
        self.button_Off = QPushButton("OFF",self)
        self.button_Off.clicked.connect(self.clickOff)
        
        #progress bar
        self.progressBar_turtle_scale=QProgressBar(self)
        
        #레이아웃 생성
        self.layoutH1 = QHBoxLayout()   #타이틀
        self.layoutV1 = QVBoxLayout()   #카메라
        self.layoutH2 = QHBoxLayout()   #버튼
        
        #레이아웃addWidget
        self.layoutH1.addWidget(self.button_Home)
        self.layoutV1.addLayout(self.layoutH1)
        self.layoutV1.addWidget(self.frame_Camera)
        self.layoutH2.addWidget(self.button_On)
        self.layoutH2.addWidget(self.button_Off)
        self.layoutH2.addWidget(self.progressBar_turtle_scale)
        self.layoutV1.addLayout(self.layoutH2)
        
        self.setLayout(self.layoutV1)
        
        self.show()
        
        
    def clickHome(self):
        print("Home")
        
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
        self.progressBar_turtle_scale.setValue(int(self.turtleScale[0][0]))

        
    def clickOff(self):
        self.timer.stop()
        # self.frame_Camera.setPixmap(QPixmap('./image/error.png'))
        


def main():
    app = QApplication(sys.argv)
    
    mainWindow = Main()
    
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()