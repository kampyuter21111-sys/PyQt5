import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

talabalar = ["Ali", "Vali", "Sardor", "Madina", "Nilufar", "Jasur"]


class Oyna(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tasodifiy tanlash")
        self.resize(300, 120)

        self.btn = QPushButton("Tanlash")
        self.btn.clicked.connect(self.tanla)

        self.label = QLabel("Tugmani bosing")

        yoyilma = QVBoxLayout()
        yoyilma.addWidget(self.btn)
        yoyilma.addWidget(self.label)
        self.setLayout(yoyilma)

    def tanla(self):
        ism = random.choice(talabalar)
        self.label.setText(f"Tanlangan talaba: {ism}")


app = QApplication(sys.argv)
oyna = Oyna()
oyna.show()
sys.exit(app.exec_())
