import sqlite3
from PyQt5.QtWidgets import QDialog, QLabel
from PyQt5.QtGui import QPixmap


class Best_Results(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Лучшие результаты")
        self.setGeometry(650, 400, 300, 200)

        self.pixmap = QPixmap('data\Инструкцияфон.png')
        self.image = QLabel(self)
        self.image.move(0, -35)
        self.image.setPixmap(self.pixmap)

        self.bd = sqlite3.connect("database.db")
        self.cursor = self.bd.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS [Все игры] (Уровень TEXT,
                                    Очки INT)""")
        ress = self.cursor.execute("""SELECT * FROM [Все игры]""").fetchall()
        res_easy = []
        res_norm = []
        res_hard = []
        if ress:
            for el in ress:
                if el[0] == "Легко":
                    res_easy.append(el[1])
                elif el[0] == "Нормально":
                    res_norm.append(el[1])
                elif el[0] == "Сложно":
                    res_hard.append(el[1])
        self.bd.close()

        self.best_easy = QLabel(self)
        if res_easy:
            self.best_easy.setText("Легко: " + str(max(res_easy)))
        else:
            self.best_easy.setText("Легко: 0")
        self.best_easy.move(20, 20)

        self.best_norm = QLabel(self)
        if res_norm:
            self.best_norm.setText("Нормально: " + str(max(res_norm)))
        else:
            self.best_norm.setText("Нормально: 0")
        self.best_norm.move(20, 50)

        self.best_hard = QLabel(self)
        if res_hard:
            self.best_hard.setText("Сложно: " + str(max(res_hard)))
        else:
            self.best_hard.setText("Сложно: 0")
        self.best_hard.move(20, 80)
