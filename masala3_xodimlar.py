import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLineEdit, QPushButton,
                             QLabel, QVBoxLayout)

xodimlar = {"Dilshod": "Direktor", "Aziza": "Hisobchi"}


class Oyna(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ofis xodimlari")
        self.resize(350, 250)

        # Qidirish qismi
        self.ism_input = QLineEdit()
        self.ism_input.setPlaceholderText("Xodim ismini kiriting")
        self.btn_qidir = QPushButton("Lavozimni ko'rsat")
        self.btn_qidir.clicked.connect(self.qidir)
        self.natija = QLabel("")

        # Yangi xodim qo'shish qismi
        self.yangi_ism = QLineEdit()
        self.yangi_ism.setPlaceholderText("Yangi xodim ismi")
        self.yangi_lavozim = QLineEdit()
        self.yangi_lavozim.setPlaceholderText("Yangi xodim lavozimi")
        self.btn_qosh = QPushButton("Xodim qo'shish")
        self.btn_qosh.clicked.connect(self.qosh)
        self.xabar = QLabel("")

        yoyilma = QVBoxLayout()
        yoyilma.addWidget(self.ism_input)
        yoyilma.addWidget(self.btn_qidir)
        yoyilma.addWidget(self.natija)
        yoyilma.addWidget(QLabel("--- Yangi xodim qo'shish ---"))
        yoyilma.addWidget(self.yangi_ism)
        yoyilma.addWidget(self.yangi_lavozim)
        yoyilma.addWidget(self.btn_qosh)
        yoyilma.addWidget(self.xabar)
        self.setLayout(yoyilma)

    def qidir(self):
        ism = self.ism_input.text().strip()
        if ism in xodimlar:
            self.natija.setText(f"{ism} - {xodimlar[ism]}")
        else:
            self.natija.setText("Bunday xodim topilmadi")

    def qosh(self):
        ism = self.yangi_ism.text().strip()
        lavozim = self.yangi_lavozim.text().strip()
        if ism == "" or lavozim == "":
            self.xabar.setText("Ism va lavozimni to'liq kiriting!")
            return
        xodimlar[ism] = lavozim
        self.xabar.setText(f"{ism} qo'shildi!")
        self.yangi_ism.clear()
        self.yangi_lavozim.clear()


app = QApplication(sys.argv)
oyna = Oyna()
oyna.show()
sys.exit(app.exec_())
