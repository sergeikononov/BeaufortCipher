import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 button - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 500
        self.height = 200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        button = QPushButton('Encode', self)
        button.setToolTip('This is an example button')
        button.move(100, 70)
        button.clicked.connect(self.on_click_encode)

        button1 = QPushButton('Decode', self)
        button1.setToolTip('This is an example button')
        button1.move(300, 70)
        button1.clicked.connect(self.on_click_decode)

        self.show()

    @pyqtSlot()
    def on_click_decode(self):
        string = open('encode.txt', 'r')
        arrayString = string.read()
        string.close()

        key = open('key.txt', 'r')
        arrayKey = key.read()
        key.close()

        # подгоняем ключ по размеру

        arrayKey = (arrayKey * (len(arrayString)) + arrayKey)[:len(arrayString)]

        # кодируем и записываем в файл
        c = ''.join([chr(((ord(arrayString[i]) + ord(arrayKey[i])) % 26) + ord("A")) for i in range(len(arrayString))])
        enc = open('decode.txt', 'w')
        for index in c:
            enc.write(index)
        enc.close()

    def on_click_encode(self):
        string = open('str.txt', 'r')
        arrayString = string.read()
        string.close()

        key = open('key.txt', 'r')
        arrayKey = key.read()
        key.close()

        # подгоняем ключ по размеру

        arrayKey = (arrayKey * (len(arrayString)) + arrayKey)[:len(arrayString)]

        #кодируем и записываем в файл
        c = ''.join([chr(((ord(arrayString[i]) - ord(arrayKey[i])) % 26) + ord("A")) for i in range(len(arrayString))])
        enc = open('encode.txt', 'w')
        for index in c:
            enc.write(index)
        enc.close()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())