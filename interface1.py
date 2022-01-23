import sys
from PyQt5 import QtWidgets


class interface1(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
		self.variable=0
		self.contrainte=0

		self.init_ui()


	def init_ui(self):

		# Label variable plus Ligne edit variable
		self.l1=QtWidgets.QLabel('Nombre de variable')
		self.le1 =QtWidgets.QLineEdit()

		# Label contrainte plus Ligne edit contrainte
		self.l2=QtWidgets.QLabel('Nombre de contrainte')
		self.le2 =QtWidgets.QLineEdit()

		# Bouton calcul
		self.b = QtWidgets.QPushButton('Calcul')
		self.b.clicked.connect(self.btn_calcul_clk)

		#Layout
		v_box = QtWidgets.QVBoxLayout()

		v_box.addWidget(self.l1)
		v_box.addWidget(self.le1)

		v_box.addWidget(self.l2)
		v_box.addWidget(self.le2)

		v_box.addWidget(self.b)

		self.setLayout(v_box)

		#Fenetre
		self.setWindowTitle('Interface')
		self.show()


	def btn_calcul_clk(self):
		self.variable= int(self.le1.text())
		print('Nombre de variable : ',self.variable)

		self.contrainte= int(self.le2.text())
		print('Nombre de contrainte : ',self.contrainte)
			

app = QtWidgets.QApplication(sys.argv)
a_window = interface1()
sys.exit(app.exec_())