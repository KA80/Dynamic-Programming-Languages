import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('html_editor.ui', self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.textEdit_2.setText(self.textEdit.toPlainText())


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())