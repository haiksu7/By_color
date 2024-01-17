import sqlite3
from PyQt5.QtWidgets import QTableWidget, QHBoxLayout, QTableWidgetItem
from PyQt5.QtWidgets import QDialog


# Отображение БД в виде таблицы
class Show_Table(QDialog):
    def __init__(self):
        super().__init__()
        self.db = sqlite3.connect('database.db')
        self.cursor = self.db.cursor()
        self.resize(230, 235)
        self.setWindowTitle('Все результаты')

        query = "SELECT * FROM [Все игры]"
        res = self.cursor.execute(query).fetchall()
        res.reverse()

        TableWidget = QTableWidget()
        TableWidget.setRowCount(len(res))
        TableWidget.setColumnCount(2)
        TableWidget.move(self.rect().center())

        layout = QHBoxLayout()

        TableWidget.setHorizontalHeaderLabels(['Уровень', 'Очки'])

        QTableWidget.resizeColumnsToContents(TableWidget)
        QTableWidget.resizeRowsToContents(TableWidget)

        for i, value in enumerate(res):
            newItem = QTableWidgetItem(str(value[0]))
            TableWidget.setItem(i, 0, newItem)
            newItem = QTableWidgetItem(str(value[1]))
            TableWidget.setItem(i, 1, newItem)

        layout.addWidget(TableWidget)

        self.setLayout(layout)
