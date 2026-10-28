import sys
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QLabel, QHBoxLayout

kitob = {"Ali": "998901234567", "Vali": "998911234567", "Sardor": "998931112233"}


class Oyna(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Telefon kitobi")
        self.resize(350, 80)

        self.combo = QComboBox()
        self.combo.addItems(kitob.keys())
        self.combo.currentTextChanged.connect(self.korsat)

        self.label = QLabel()

        yoyilma = QHBoxLayout()
        yoyilma.addWidget(self.combo)
        yoyilma.addWidget(self.label)
        self.setLayout(yoyilma)

        self.korsat(self.combo.currentText())

    def korsat(self, ism):
        self.label.setText(kitob[ism])


app = QApplication(sys.argv)
oyna = Oyna()
oyna.show()
sys.exit(app.exec_())
