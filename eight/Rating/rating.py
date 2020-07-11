import sys
import csv

from PyQt5 import uic
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


def commaToDot(s):
    return s.replace(',', '.').split()[0]


class TableWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('app.ui', self)

        self.loadTable('rating.csv')

    def loadTable(self, file):
        with open(file, encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')

            title = next(reader)[1:15]
            title[13] = 'Зачет'
            self.table.setColumnCount(len(title))
            self.table.setHorizontalHeaderLabels(title)
            self.table.setRowCount(0)

            for i, row in enumerate(reader):
                self.table.setRowCount(self.table.rowCount() + 1)
                for j, elem in enumerate(row):
                    if j > 0:
                        self.table.setItem(i, j - 1, QTableWidgetItem(elem))  # 11
                if self.table.item(i, 11).text() != '':
                    tmp = self.table.item(i, 11).text()
                    tmp = commaToDot(tmp)
                    self.colorSelection(i, float(tmp))

            self.table.resizeColumnsToContents()

    def colorSelection(self, row, points):
        if points >= 95:
            self.setColor(row, QColor('#32b141'))
        elif points >= 80:
            self.setColor(row, QColor('#ffe777'))
        elif points >= 60:
            self.setColor(row, QColor('#c75f4e'))
        else:
            self.setColor(row, QColor('#dedfe4'))

    def setColor(self, row, color):
        self.table.item(row, 1).setBackground(color)


app = QApplication(sys.argv)
ex = TableWidget()
ex.show()
sys.exit(app.exec_())
