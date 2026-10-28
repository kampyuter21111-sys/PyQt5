import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QListWidget, QVBoxLayout

kitoblar = ["Python Asoslari", "Flask Dasturlash", "Sun'iy Intellekt"]


class Oyna(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kutubxona katalogi")
        self.resize(300, 250)

        self.qidiruv = QLineEdit()
        self.qidiruv.setPlaceholderText("Kitob nomini yozing...")
        self.qidiruv.textChanged.connect(self.qidir)

        self.royxat = QListWidget()

        yoyilma = QVBoxLayout()
        yoyilma.addWidget(self.qidiruv)
        yoyilma.addWidget(self.royxat)
        self.setLayout(yoyilma)

        self.qidir("")

    def qidir(self, matn):
        self.royxat.clear()
        for kitob in kitoblar:
            if matn.lower() in kitob.lower():
                self.royxat.addItem(kitob)


app = QApplication(sys.argv)
oyna = Oyna()
oyna.show()
sys.exit(app.exec_())
