import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt, QTimer
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Matplotlib Figure 및 Canvas 생성
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)

        # 그래프를 그릴 수 있는 Axes 생성
        self.ax = self.figure.add_subplot(111)
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')

        # 파이어베이스 연결 및 데이터 참조
        cred = credentials.Certificate('key.json')
        firebase_admin.initialize_app(cred, {'databaseURL': 'https://capstone-116d0-default-rtdb.firebaseio.com/'})
        self.ref = db.reference('soundData')

        # 그래프 업데이트 타이머 생성
        self.timer = QTimer()
        self.timer.setInterval(1000)  # 1초마다 그래프 업데이트
        self.timer.timeout.connect(self.update_graph)

        # 메인 윈도우 레이아웃 설정
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.addWidget(self.canvas)

        # 그래프 업데이트 타이머 시작
        self.timer.start()

    def update_graph(self):
        # 파이어베이스에서 데이터 가져오기
        data = self.ref.get()

        if data is not None:
            # 데이터가 존재하는 경우 그래프 업데이트
            x = []
            y = []

            for key, value in data.items():
                x.append(int(key))
                y.append(int(value))

            self.ax.clear()
            self.ax.plot(x, y, 'b-')
            self.canvas.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
