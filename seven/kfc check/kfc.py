import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class KFC_Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('kfc.ui', self)

        self.goods = 5
        self.goodCost = ['74', '109', '229', '204', '214']

        self.pushButton_accept.clicked.connect(self.calculate)

    def calculate(self):
        self.spinBoxes = [self.spinBox_potato, self.spinBox_milkshake, self.spinBox_strips, self.spinBox_twister,
                          self.spinBox_boxmaster]
        self.checkBoxes = [self.checkBox_potato, self.checkBox_milkshake, self.checkBox_strips, self.checkBox_twister,
                          self.checkBox_boxmaster]
        self.totalCost = 0
        self.text = ''
        self.is_empty = True

        self.text += '\t\t КАССОВЫЙ ЧЕК \n\n'

        for i in range(self.goods):
            if self.spinBoxes[i].value != 0 and self.checkBoxes[i].isChecked():
                self.is_empty = False
                self.text += self.checkBoxes[i].text() + '\n\t\t\t\t' + str(self.spinBoxes[i].value()) + '*' + self.goodCost[i] + '\n'
                self.text += '\t\t\t\t=' + str(self.spinBoxes[i].value() * int(self.goodCost[i])) + '\n\n'
                self.text += '################################################\n'
                self.totalCost += self.spinBoxes[i].value() * int(self.goodCost[i])
        if self.is_empty:
            self.check.setPlainText('')
        else:
            self.text += '\n\nИТОГ:\t\t\t=' + str(self.totalCost)
            self.check.setPlainText(self.text)





app = QApplication(sys.argv)
ex = KFC_Widget()
ex.show()
sys.exit(app.exec_())
