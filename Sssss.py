from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import vk
import time


class PopupWindowClass(QtWidgets.QWidget):


    def __init__(self):
        super(PopupWindowClass, self).__init__()
        self.setWindowFlags(QtCore.Qt.SplashScreen | QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)

        self.setMinimumSize(QtCore.QSize(300, 100))
        self.animation = QtCore.QPropertyAnimation(self, b"windowOpacity")
        self.animation.finished.connect(self.hide)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.hideAnimation)
        self.setupUi()

        self.setPopupText(txt)

    def setupUi(self):
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.label = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignVCenter)
        self.verticalLayout.addWidget(self.label)
        appearance = self.palette()
        appearance.setColor(QtGui.QPalette.Normal, QtGui.QPalette.Window,
                            QtGui.QColor("red"))

        self.setPalette(appearance)

    def setPopupText(self, text):
        self.label.setText(text)

        self.label.adjustSize()


    def show(self):
        self.setWindowOpacity(1000.0)
        self.animation.setDuration(500)
        self.animation.setStartValue(0.0)
        self.animation.setEndValue(1.0)
        QtWidgets.QWidget.show(self)
        self.animation.start()
        self.timer.start(500)

    def hideAnimation(self):
        self.timer.stop()
        self.animation.setDuration(500)
        self.animation.setStartValue(1.0)
        self.animation.setEndValue(0.0)
        self.animation.stop()







    def NEW(self, txt):

        while True:
            nxt = API()

            if txt != nxt:
                txt = nxt

                main_window.setPopupText(txt)
                main_window.show()
                time.sleep(5)
                main_window.hide()
            time.sleep(14)

def API():
    a = []
    session = vk.Session(
        access_token='enter_yout_token')
    api = vk.API(session)
    messages = api.messages.get()
    for i in messages:
        try:
            a.append(i.get('body'))
            break
        except AttributeError:
            i = i
    yoy = str(a[0])

    return yoy



txt = API()
app = QtWidgets.QApplication(sys.argv)

main_window = PopupWindowClass()
main_window.move(1600,900)


main_window.NEW(txt)


sys.exit(app.exec_())
