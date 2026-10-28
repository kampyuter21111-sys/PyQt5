import sys
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QListWidget, QVBoxLayout

jadval = {
    "Dushanba": ["Matematika", "Fizika"],
    "Seshanba": ["Ingliz tili", "Tarix"],
    "Chorshanba": ["Informatika", "Kimyo", "Adabiyot"],
}


class Oyna(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dars jadvali")
        self.resize(300, 250)

        self.combo = QComboBox()
        self.combo.addItems(jadval.keys())
        self.combo.currentTextChanged.connect(self.korsat)

        self.royxat = QListWidget()

        yoyilma = QVBoxLayout()
        yoyilma.addWidget(self.combo)
        yoyilma.addWidget(self.royxat)
        self.setLayout(yoyilma)

        self.korsat(self.combo.currentText())

    def korsat(self, kun):
        self.royxat.clear()
        self.royxat.addItems(jadval[kun])


app = QApplication(sys.argv)
oyna = Oyna()
oyna.show()
sys.exit(app.exec_())
