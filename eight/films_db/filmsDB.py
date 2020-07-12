import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QDialog


class TableWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('database.ui', self)

        self.con = sqlite3.connect('films.db')
        self.cur = self.con.cursor()

        self.reader = []

        self.genres = []
        self.cur_genre = 0
        self.loadTable()
        self.add_film = AddFilm(self)
        self.del_film = DeleteFilm(self)
        self.pushButton_search.clicked.connect(self.searchFilms)
        self.pushButton_edit.clicked.connect(self.editFilm)
        self.pushButton_add.clicked.connect(self.add_film.show)

    def loadTable(self):
        self.comboBox_genres.addItem('Все жанры')
        self.genres = self.cur.execute('SELECT * FROM genres').fetchall()
        for i in self.genres:
            self.comboBox_genres.addItem(i[1])

        self.table_db.setColumnCount(5)
        self.table_db.setHorizontalHeaderLabels(('id', 'Название', 'Год выхода', 'Жанр', 'Длительность'))
        self.reader = self.cur.execute('SELECT * FROM Films').fetchall()
        self.printTable()

    def keyToString(self, elem):
        for i in self.genres:
            if elem == i[0]:
                return i[1]
        return 'Все'

    def stringToKey(self, elem):
        for i in self.genres:
            if elem == i[1]:
                return i[0]
        return 0

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Delete:
            self.del_film.show()

    def searchFilms(self):

        genre = self.comboBox_genres.currentText()
        genre = self.stringToKey(genre)

        name = self.textEdit_name.toPlainText()
        name = '%' + name + '%'
        try:
            date = int(self.textEdit_date.toPlainText()) if self.textEdit_date.toPlainText() != '' else '%'
        except ValueError:
            self.textEdit_date.setText('Ошибка')
            return

        try:
            duration = int(self.textEdit_duration.toPlainText()) if self.textEdit_duration.toPlainText() != '' else 0
        except ValueError:
            self.textEdit_duration.setText('Ошибка')
            return

        if genre != 0:
            self.reader = self.cur.execute(
                'SELECT * FROM Films WHERE genre == ? and title LIKE ? and year LIKE ? and duration >= ?',
                (genre, name, date, duration)).fetchall()
        else:
            self.reader = self.cur.execute('SELECT * FROM Films WHERE title LIKE ? and year LIKE ? and duration >= ?',
                                           (name, date, duration)).fetchall()
        self.printTable()

    def printTable(self):
        self.table_db.setRowCount(0)
        for i, row in enumerate(self.reader):
            self.table_db.setRowCount(self.table_db.rowCount() + 1)
            for j, elem in enumerate(row):
                if j == 3:
                    elem = self.keyToString(elem)
                if j == 0:
                    self.table_db.setItem(i, j, self.createItem(str(elem), Qt.ItemIsSelectable | Qt.ItemIsEnabled))
                else:
                    self.table_db.setItem(i, j, self.createItem(str(elem)))
        self.table_db.resizeColumnsToContents()

    def editFilm(self):
        prev_table = self.reader
        table = []
        for i in range(len(self.reader)):
            id = self.table_db.item(i, 0).text()
            name = self.table_db.item(i, 1).text()
            date = self.table_db.item(i, 2).text()
            duration = self.table_db.item(i, 4).text()
            table.append((id, name, date, duration))
        for i, row in enumerate(table):
            if row[1] != prev_table[i][1]:
                self.cur.execute('UPDATE films SET title = ? WHERE id = ?', (row[1], row[0]))
            if row[2] != prev_table[i][2]:
                self.cur.execute('UPDATE films SET year = ? WHERE id = ?', (row[2], row[0]))
            if row[3] != prev_table[i][4]:
                self.cur.execute('UPDATE films SET duration = ? WHERE id = ?', (row[3], row[0]))
        self.con.commit()

    @staticmethod
    def createItem(text, flags=Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable):
        tableWidgetItem = QTableWidgetItem(text)
        tableWidgetItem.setFlags(flags)
        return tableWidgetItem


class AddFilm(QDialog):
    def __init__(self, mainWidget):
        super().__init__()
        uic.loadUi('add.ui', self)
        self.main = mainWidget
        for i in self.main.genres:
            self.comboBox_genres.addItem(i[1])
        self.buttonBox.accepted.connect(self.add)
        self.buttonBox.rejected.connect(self.closeDialog)

    def add(self):
        genre = self.main.stringToKey(self.comboBox_genres.currentText())
        name = self.textEdit_name.toPlainText()
        try:
            date = int(self.textEdit_date.toPlainText())
        except ValueError:
            date = 0
        try:
            duration = int(self.textEdit_duration.toPlainText())
        except ValueError:
            duration = 0
        if genre != 0 and name != '' and date > 1900 and duration > 0:
            self.main.cur.execute("INSERT INTO films(title, genre,year,duration) VALUES(?,?,?,?)", (name, genre, date,
                                                                                                    duration))
            self.main.loadTable()
        self.main.con.commit()
        self.closeDialog()

    def closeDialog(self):
        self.textEdit_name.clear()
        self.textEdit_date.clear()
        self.textEdit_duration.clear()
        self.close()


class DeleteFilm(QDialog):
    def __init__(self, mainWidget):
        super().__init__()
        uic.loadUi('delete.ui', self)
        self.main = mainWidget
        self.buttonBox.accepted.connect(self.delete)
        self.buttonBox.rejected.connect(self.closeDialog)

    def delete(self):
        indexes = self.main.table_db.selectionModel().selectedIndexes()
        for i in indexes:
            id = int(self.main.reader[i.row()][0])
            self.main.cur.execute('DELETE from films WHERE id = ?', (id,))
        self.main.loadTable()
        ex.con.commit()
        self.closeDialog()

    def closeDialog(self):
        self.close()


app = QApplication(sys.argv)
ex = TableWidget()
ex.show()
sys.exit(app.exec_())
