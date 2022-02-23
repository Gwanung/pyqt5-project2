
from re import search
import sys
from PyQt5.QtWidgets import *
import requests
from bs4 import BeautifulSoup


                    
class MyApp(QWidget):

    def __init__(self):

        super().__init__()
       

        self.initUI()


    def initUI(self):

        self.le = QLineEdit()
        self.le.setPlaceholderText("Enter your search word")
        self.le.returnPressed.connect(self.crawl_news)

        self.btn = QPushButton("search")
        self.btn.clicked.connect(self.crawl_news)

        self.lb = QLabel(" ")

        self.tb =QTextBrowser()
        self.tb.setAcceptRichText(True)
        self.tb.setOpenExternalLinks(True)


        grid = QGridLayout()
        grid.addWidget(self.le, 0, 0, 1, 3)
        grid.addWidget(self.btn, 0, 3, 1, 1)
        grid.addWidget(self.lb, 1, 0, 1, 4)
        grid.addWidget(self.tb, 2, 0, 1, 4)

        self.setLayout(grid)

        self.setGeometry(100, 100, 700, 450)
        self.show()


    def crawl_news(self):
        search_word = self.le.text()


        if search_word:

         self.lb.setText("BBC " + search_word + " ")
         self.tb.clear()

         url_search = "https://www.bbc.co.uk/search?q="
         url =url_search + search_word
         r = requests.get(url)
         html = r.content 
         soup  = BeautifulSoup(html, "html.parser")
         titles_html = soup.select(" .search-results > " " li > article > div > hi > a" )


         for i in range(len(titles_html)):

            title = titles_html[i].text

            link = titles_html[i].get("href")
            self.tb.append(str(i + 1)+ '. '+ title + ' ( '
             + '<a href = "' + link + '">Link</a>' + ')') 
        
if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())






        

