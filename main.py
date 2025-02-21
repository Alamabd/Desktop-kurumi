import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel
from PyQt5.QtCore import Qt, QTimer, QPoint
from PyQt5.QtGui import QIcon, QMovie
from PyQt5.QtMultimedia import QSound

class MainWindow(QMainWindow, QWidget):
    def __init__(self):
        self.path = ""

        # setting window
        super(MainWindow, self).__init__()
        self.setWindowIcon(QIcon( self.path + "icon/icon.png"))

        # self.setWindowOpacity(0.5)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowFlag(Qt.WindowStaysOnTopHint)

        #set label 570
        self.label = QLabel(self)
        self.setGeometry(1166, 568, 200, 200)
        self.label.setGeometry(0, 0, 200, 200)

        self.gif( self.path + "gif/oke.gif")

        # random gif with interval
        self.timer = QTimer()
        self.timer.timeout.connect(lambda: self.random(2, 12))
        self.timer.setInterval(8000)
        self.timer.start()

    # gravity
    def gravity(self):
        # set gif
        self.random(0,2)
        self.timer.stop()

        self.posY = self.y()
        def to_bottom():
            self.posY +=1
            self.move(self.x(), self.posY)
            if self.pos().y() >= 570:
                self.delay.stop()
                # set random  
                self.random(2, 12)            
                self.timer.start()

        if self.pos().y() <= 565:
            self.delay = QTimer()
            self.delay.timeout.connect(to_bottom)
            self.delay.setInterval(3)
            self.delay.start()

        
    # random
    def random(self, min, max):
        value = 0
        value = random.randrange(min, max)
        if value == 0:
            self.gif( self.path + "gif/no.gif")
        elif value == 1:
            self.gif( self.path + "gif/fly.gif")
        elif value == 2:
            QTimer.singleShot(0, lambda: QSound.play(self.path + "audio/anime-chill.wav"))
            self.gif( self.path + "gif/love2.gif")
        elif value == 3:
            self.gif( self.path + "gif/popcorn.gif")
        elif value == 4:
            self.gif( self.path + "gif/oke.gif")
        elif value == 5:
            self.gif( self.path + "gif/i_love_you.gif")
        elif value == 6:
            self.gif( self.path + "gif/arrow_love.gif")
        elif value == 7:
            self.gif( self.path + "gif/boring.gif")
        elif value == 8:
            self.gif( self.path + "gif/hello.gif")
        elif value == 9:
            self.gif( self.path + "gif/love.gif")
        elif value == 10:
            self.gif( self.path + "gif/sad.gif")
        elif value == 11:
            self.gif( self.path + "gif/selfie.gif")
        elif value == 12:
            self.gif( self.path + "gif/weak.gif")

    def gif(self, file):
        # movie gif
        self.movie = QMovie(file)
        self.label.setMovie(self.movie)
        self.movie.setSpeed(50)
        self.movie.start()    

    # event input
    def mousePressEvent(self, event):
        self.oldPosition = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPosition)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPosition = event.globalPos()

    def mouseReleaseEvent(self, event):
        self.gravity()

    def mouseDoubleClickEvent(self, event):
        self.close()

    # def keyPressEvent(self, event):
    #     if event.key() == Qt.Key_A:


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
