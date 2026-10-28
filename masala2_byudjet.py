import sys
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QLabel, QVBoxLayout

xarajatlar = {
    "Yanvar": [1200000, 500000],
    "Fevral": [2000000, 800000],
    "Mart": [900000, 300000, 150000],
}


class Oyna(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Oyma-oy byudjet nazorati")
        self.resize(350, 120)

        self.combo = QComboBox()
        self.combo.addItems(xarajatlar.keys())
        self.combo.currentTextChanged.connect(self.hisobla)

        self.label = QLabel()

        yoyilma = QVBoxLayout()
        yoyilma.addWidget(self.combo)
        yoyilma.addWidget(self.label)
        self.setLayout(yoyilma)

        self.hisobla(self.combo.currentText())

    def hisobla(self, oy):
        jami = sum(xarajatlar[oy])
        self.label.setText(f"{oy} oyi umumiy xarajati: {jami} so'm")


app = QApplication(sys.argv)
oyna = Oyna()
oyna.show()
sys.exit(app.exec_())
