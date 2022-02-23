from email.charset import QP
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QToolBar
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import QCoreApplication, QDateTime
import requests
from bs4 import BeautifulSoup
import xlsxwriter 

class exam(QWidget):

    def __init__(self):

        super().__init__()
        
        self.initUI()


    def initUI(self):
        self.제목라벨 = QLabel("(주)캣네생선", self)
        self.제목라벨.move(50, 50)
        self.제목라벨.setFont(QFont("Helvetica", pointSize=20, weight=2))
        
        self.시총라벨 = QLabel("시가 총액 : - 원", self)
        self.시총라벨.move(50, 110)

        self.시총순위라벨 = QLabel("시가 총액 순위 : 위니브 월드 - 위", self)
        self.시총순위라벨.move(50, 140)

        self.현재가 = QLabel("현재가 : - 원", self)
        self.현재가.move(50, 170)

        self.최고최저가 = QLabel("52주 최고 | 최저 : - 원 | - 원", self)
        self.최고최저가.move(50, 200)

        self.배당율 = QLabel("배당율 : - %", self)
        self.배당율.move(50, 230)
      
        self.오픈된날짜 = QLabel("오픈 날짜 : 2020년 1월 1일", self)
        self.오픈된날짜.move(50, 260) 
        
        self.오픈날짜 = QLabel("오픈 된 날짜 : - 일", self)
        self.오픈날짜.move(50, 290) 

        self.매출비용순익 = QLabel("매출/비용/순익 : - 원/ - 원/ - 원", self)
        self.매출비용순익.move(50, 320) 


        작성버튼 = QPushButton("재무 보고서 작성", self)
        작성버튼.move(30, 430)
        작성버튼.resize(340, 50)
        작성버튼.clicked.connect(self.write)




        엑셀버튼 = QPushButton(" 엑셀 보고서 작성", self)
        엑셀버튼.move(30, 490)
        엑셀버튼.resize(340, 50)
        엑셀버튼.clicked.connect(self.excel)



        종료버튼 = QPushButton("프로그램 종료", self)
        종료버튼.move(30, 550)
        종료버튼.resize(340, 50)
        종료버튼.clicked.connect(self.close)







        self.setWindowTitle("재무 보고서를 만들어라.")
        self.setWindowIcon(QIcon("ㄹㄸ.png"))
        self.setGeometry(800, 300, 400, 630)
        self.show()


    def write(self):
        
        url = "http://paullab.synology.me/stock.html"
        response = requests.get(url)
        response.encoding = "utf-8"
        html = response.text
        soup =BeautifulSoup(html, "html.parser")

        values = soup.select(".tables td")
        self.시총라벨.setText(f"시가총액 : {values[0].text}")
        self.시총라벨.resize(400, 20)

        self.시총순위라벨.setText(f"시가총액 순위 : {values[1].text}")
        self.시총순위라벨.resize(400, 20)

        self.현재가.setText(f"현재가 : {values[3].text}")
        self.현재가.resize(400, 20)
     
        s = values[4].text.strip().replace('\n',"").split("l") # strip() 둘다 지움
        # print(s)

        self.최고최저가.setText(f"52주 최고 | 52주 최저 : {s[0]} | {s[1]}")
        self.최고최저가.resize(400, 20)

        i = values[5].text.strip()
        # print(i)

        self.배당율.setText(f"배당율 : {i}")
        self.배당율.resize(400, 20)

        self.매출비용순익.setText(f"매출/비용/순익 :\n{values[6].text}\n/{values[7].text}\n/{values[8].text}")
        self.매출비용순익.resize(400, 80)

        day = QDateTime(2020, 1, 1, 00, 00, 00)
        # print(type(day))  
        # print(dir(day))

        day = str(day.daysTo(QDateTime.currentDateTime()))
        self.오픈된날짜.setText(f"오픈된 날짜 : {day} 일")
        self.오픈된날짜.resize(400, 20)


    def excel(self):
        # workbook 하나의파일  worksheet 셀 선택 조작  cell 격자 데이터 한 개
        
        workbook = xlsxwriter.workbook("재무보고서.xlsx")
    

    def close(self):

        return QCoreApplication.instance().quit()


if __name__ == "__main__":

    app = QApplication(sys.argv)
    a = exam()
    sys.exit(app.exec_())