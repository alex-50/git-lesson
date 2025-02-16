import sys
import sqlite3

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)

        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("coffee.sqlite")

        if not self.db.open():
            QMessageBox.critical(
                self, "Ошибка базы данных",
                "Не удалось открыть базу данных: " + self.db.lastError().text(),
                QMessageBox.StandardButton.Ok
            )
            sys.exit(1)

        self.model = QSqlTableModel(self, self.db)
        self.model.setTable("coffee")
        self.model.setEditStrategy(QSqlTableModel.EditStrategy.OnManualSubmit)
        self.model.select()

        if self.model.lastError().isValid():
            QMessageBox.critical(
                self, "Ошибка модели",
                "Не удалось заполнить модель: " + self.model.lastError().text(),
                QMessageBox.StandardButton.Ok
            )
            sys.exit(1)

        self.coffeeTable.setModel(self.model)
        self.coffeeTable.setAlternatingRowColors(True)
        self.coffeeTable.horizontalHeader().setStretchLastSection(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
