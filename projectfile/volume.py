import sys
# import winsound
import threading
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
from PyQt5 import uic 
import pygame

# self.btn.clicked.connect(QCoreApplication.instance().quit)
#pip install pygame



class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #누르면 소리나오는 버튼
        self.btn = QPushButton('Quit', self)
        self.btn.move(50, 50)
        self.btn.resize(self.btn.sizeHint())
        self.btn.clicked.connect(self.playSound)

        #볼륨 조절하는 슬라이더
        self.slider=QSlider(self)
        self.slider.setRange(0,100)

        self.setWindowTitle('Quit Button')
        self.setGeometry(300, 300, 300, 200)
        self.show()
    
    #버튼 누를때 쓰래드 작동
    #이거 쓰래드로 안하면 소리 나오는동안 프로그램 멈춤
    def playSound(self):
        h1=Thread1(self, self.slider.value())
        h1.start()

#쓰레드로 소리설정 돌림
class Thread1(QThread):
    def __init__(self, parent, volume):
        super().__init__(parent)
        self.parent = parent
        #슬라이더 값 받아서 run에서 쓸라구 self.volume로 다시 받음
        #볼륨값이 0~1이여야되서 100으로 나눔
        self.volume=float(volume/100)
        

    def run(self):
        # winsound.PlaySound('attention.wav',winsound.SND_ASYNC) 이것도 가능한데 소리설정 불가능
        #소리내는거 여러개있던데 볼륨설정 하는거 찾은게 이거뿐
        #https://www.pygame.org/docs/ref/mixer.html
        pygame.init()
        pygame.mixer.init()
        sound = pygame.mixer.Sound("attention.wav")
        # 0~1값
        sound.set_volume(self.volume)
        sound.play()     

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())