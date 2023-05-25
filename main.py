import sys

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import *
from PyQt5 import uic
import getData

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("_uiFiles/mainPage.ui")[0]
form_second=uic.loadUiType('_uiFiles/graphPage.ui')[0]
#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.initUi()
    def initUi(self):
        self.timer = QTimer(self)  # timer 변수에 QTimer 할당
        self.timer.start(10000)  # 10000msec(10sec) 마다 반복
        self.timer.timeout.connect(self.changeSound)  # start time out시 연결할 함수
    def changeSound(self):
        self.level.setText(str(getData.getData()))
    def btn_main_to_second(self):
        self.hide()
        self.second=secondWindow()
        self.second.exec()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


class secondWindow(QDialog,QWidget,form_second):
    def __init__(self):
        super(secondWindow,self).__init__()
        self.initUi()
        self.show()


    def initUi(self):
        self.setupUi(self)

    def btn_second_to_main(self):
        self.close()




if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)
    #WindowClass의 인스턴스 생성
    myWindow = WindowClass()
    #프로그램 화면을 보여주는 코드
    myWindow.show()
    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()