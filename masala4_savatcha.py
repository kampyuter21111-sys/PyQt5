import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QComboBox, QSpinBox,
                             QPushButton, QLabel, QVBoxLayout)

narxlar = {"Olma": 5000, "Banan": 7000, "Sut": 12000}


class Oyna(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Supermarket savatchasi")
        self.resize(350, 250)

        self.jami = 0  # savatdagi umumiy summa

        self.combo = QComboBox()
        self.combo.addItems(narxlar.keys())

        self.miqdor = QSpinBox()
        self.miqdor.setMinimum(1)
        self.miqdor.setMaximum(1000)

        self.btn = QPushButton("Savatga qo'shish")
        self.btn.clicked.connect(self.qosh)

        self.btn_tozala = QPushButton("Savatni tozalash")
        self.btn_tozala.clicked.connect(self.tozala)

        self.label = QLabel("Umumiy summa: 0 so'm")
        self.chegirma = QLabel("")

        yoyilma = QVBoxLayout()
        yoyilma.addWidget(self.combo)
        yoyilma.addWidget(self.miqdor)
        yoyilma.addWidget(self.btn)
        yoyilma.addWidget(self.btn_tozala)
        yoyilma.addWidget(self.label)
        yoyilma.addWidget(self.chegirma)
        self.setLayout(yoyilma)

    def qosh(self):
        mahsulot = self.combo.currentText()
        son = self.miqdor.value()
        self.jami += narxlar[mahsulot] * son
        self.label.setText(f"Umumiy summa: {self.jami} so'm")

        # Bonus: 100 mingdan oshsa chegirma
        if self.jami > 100000:
            self.chegirma.setText("Chegirma qo'llandi")
        else:
            self.chegirma.setText("")

    def tozala(self):
        self.jami = 0
        self.label.setText("Umumiy summa: 0 so'm")
        self.chegirma.setText("")


app = QApplication(sys.argv)
oyna = Oyna()
oyna.show()
sys.exit(app.exec_())
