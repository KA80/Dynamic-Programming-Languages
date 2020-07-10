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
        self.__spinBoxes = [self.spinBox_potato, self.spinBox_milkshake, self.spinBox_strips, self.spinBox_twister,
                            self.spinBox_boxmaster]
        self.__checkBoxes = [self.checkBox_potato, self.checkBox_milkshake, self.checkBox_strips, self.checkBox_twister,
                             self.checkBox_boxmaster]
        self.__totalCost = 0
        self.__text = ''

        self.__text += '\t\t КАССОВЫЙ ЧЕК \n\n'

        for i in range(self.goods):
            if self.__spinBoxes[i].value != 0 and self.__checkBoxes[i].isChecked():
                self.__text += self.__checkBoxes[i].text() + '\n\t\t\t\t' + str(self.__spinBoxes[i].value()) + '*' + \
                               self.goodCost[i] + '\n'
                self.__text += '\t\t\t\t=' + str(self.__spinBoxes[i].value() * int(self.goodCost[i])) + '\n\n'
                self.__text += '################################################\n'
                self.__totalCost += self.__spinBoxes[i].value() * int(self.goodCost[i])

        if self.__totalCost > 0:
            self.__text += '\n\nИТОГ:\t\t\t\t=' + str(self.__totalCost)
            self.check.setPlainText(self.__text)
        else:
            self.check.setPlainText('')


app = QApplication(sys.argv)
ex = KFC_Widget()
ex.show()
sys.exit(app.exec_())
