import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel
from UI_MainWindow import Ui_MainWindow
from UI_AddEditCoffeeForm import Ui_AddEditCoffeeForm


class AddEditCoffeeForm(QWidget, Ui_AddEditCoffeeForm):
    def __init__(self, model, db, mode: str, row_id: int = -1):
        super().__init__()
        self.setupUi(self)
        self.mode = mode
        self.row_id = row_id
        self.model = model
        self.db = db
        self.load_ui_for_adding() if mode == 'add' else self.load_ui_for_editing()
        self.applyChanges.clicked.connect(self.save_changes)

    def load_ui_for_adding(self):
        self.coffeeID.setText(str(self.model.rowCount() + 1))
        self.coffeeID.setReadOnly(True)

    def load_ui_for_editing(self):
        if self.row_id >= 0:

            row_data = []
            for column in range(self.model.columnCount()):
                item = self.model.data(self.model.index(self.row_id, column))
                row_data.append(item)

            self.coffeeID.setText(str(row_data[0]))
            self.coffeeID.setReadOnly(True)
            self.coffeeName.setText(row_data[1])
            self.coffeeRoastLevel.setCurrentText(row_data[2])
            self.coffeeGOrB.setCurrentText(row_data[3])
            self.coffeeDescription.setText(row_data[4])
            self.coffeePrice.setValue(int(row_data[5]))
            self.packageSize.setValue(int(row_data[6]))

    def save_changes(self):

        name = self.coffeeName.text()
        roast_level = self.coffeeRoastLevel.currentText()
        coffee_type = self.coffeeGOrB.currentText()
        description = self.coffeeDescription.text()
        price = self.coffeePrice.value()
        package_size = self.packageSize.value()

        if not name:
            QMessageBox.critical(self, "Ошибка", "Необходимо ввести название кофе.")
            return

        if not description:
            QMessageBox.critical(self, "Ошибка", "Необходимо ввести описание кофе.")
            return

        if price <= 0:
            QMessageBox.critical(self, "Ошибка", "Необходимо ввести цену кофе.")
            return

        if package_size <= 0:
            QMessageBox.critical(self, "Ошибка", "Необходимо ввести размер пакета.")
            return

        if self.mode == "add":
            row = self.model.rowCount()
            self.model.insertRow(row)
        else:
            row = self.row_id

        self.model.setData(self.model.index(row, 1), name)
        self.model.setData(self.model.index(row, 2), roast_level)
        self.model.setData(self.model.index(row, 3), coffee_type)
        self.model.setData(self.model.index(row, 4), description)
        self.model.setData(self.model.index(row, 5), price)
        self.model.setData(self.model.index(row, 6), package_size)

        if not self.model.submitAll():
            QMessageBox.critical(self, "Ошибка", "Не удалось сохранить запись: " + self.model.lastError().text())
            return

        QMessageBox.information(self, "Успех", "Запись успешно добавлена.")

        self.close()


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.model = QSqlTableModel(self, self.db)
        self.init_table()
        self.update_table()
        self.addButton.clicked.connect(self.call_add_edit_form)
        self.editButton.clicked.connect(self.call_add_edit_form)

    def init_table(self):
        self.db.setDatabaseName("./data/coffee.sqlite")

        if not self.db.open():
            QMessageBox.critical(
                self, "Ошибка базы данных",
                "Не удалось открыть базу данных: " + self.db.lastError().text(),
                QMessageBox.StandardButton.Ok
            )
            sys.exit(1)

        self.model.setTable("coffee")
        self.model.setEditStrategy(QSqlTableModel.EditStrategy.OnManualSubmit)

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

    def update_table(self):
        self.model.select()

    def call_add_edit_form(self):
        if self.sender().text() == "Добавить":
            self.add_edit_form = AddEditCoffeeForm(self.model, self.db, mode="add")
            self.add_edit_form.setWindowTitle("Добавить кофе")
            self.add_edit_form.show()
        else:
            index = self.coffeeTable.currentIndex().row()

            if index < 0:
                QMessageBox.critical(self, "Ошибка", "Не выбрана запись для редактирования.")
            else:
                self.add_edit_form = AddEditCoffeeForm(
                    self.model, self.db,
                    row_id=self.coffeeTable.currentIndex().row(), mode="edit"
                )
                self.add_edit_form.setWindowTitle("Редактировать кофе")
                self.add_edit_form.show()
        self.update_table()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
