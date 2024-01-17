import pygame
from project_code.all_best_results import Best_Results
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QPushButton, QDialog
from PyQt5.QtWidgets import QLabel
from project_code.game_and_end import Game, lvl


# Начальное окно
class StartWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(600, 300, 700, 500)
        self.setWindowTitle('По цвету')

        self.pixmap = QPixmap('data\фонстарт.png')
        self.image = QLabel(self)
        self.image.move(0, -35)
        self.image.setPixmap(self.pixmap)

        self.head = QLabel(self)
        self.head.setText('--По цвету--')
        self.head.move(300, 50)

        self.question = QLabel(self)
        self.question.setText('Выберите уровень:')
        self.question.move(200, 120)

        self.button_1 = QPushButton(self)
        self.button_1.move(100, 200)
        self.button_1.setText("Легко")
        self.button_1.clicked.connect(self.run1)

        self.button_2 = QPushButton(self)
        self.button_2.move(300, 200)
        self.button_2.setText("Нормально")
        self.button_2.clicked.connect(self.run1)

        self.button_3 = QPushButton(self)
        self.button_3.move(500, 200)
        self.button_3.setText("Сложно")
        self.button_3.clicked.connect(self.run1)

        self.instruction = QPushButton(self)
        self.instruction.move(300, 380)
        self.instruction.setText("Инструкция")
        self.instruction.clicked.connect(self.get_instruction)

        self.bestresults = QPushButton(self)
        self.bestresults.move(280, 430)
        self.bestresults.setText("!Лучшие результаты!")
        self.bestresults.clicked.connect(self.get_best)

        self.text = QLabel(self)
        self.text.move(275, 310)
        self.text.setText("★Наполни мир красками!★")

        self.music()

    def music(self):
        pygame.init()
        pygame.mixer.music.load("data\Infinitely_Gray_Instrumental_N25.mp3")
        pygame.mixer.music.play(-1)

    def run1(self):
        self.a = self.sender().text()
        lvl.append(self.a)
        player = Game()

    def get_instruction(self):
        get = Instruction()
        get.exec_()

    def get_best(self):
        get = Best_Results()
        get.exec_()


# Инструкция
class Instruction(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Инструкция")
        self.setGeometry(650, 400, 630, 300)

        self.pixmap = QPixmap('data\Инструкцияфон.png')
        self.image = QLabel(self)
        self.image.move(0, -35)
        self.image.setPixmap(self.pixmap)

        self.instruction = QLabel(self)
        self.instruction.setText('                                       ★Инструкция★' + '\n' + '\n'+ '\n'
                                 '●По цвету - аркадная игра, где игрок управляет ведром определённого цвета,' + '\n'
                                 'двигая его вправо или влево с помощью стрелочек на клавиатуре.' + '\n'+ '\n'
                                 '●Цель - собирать падающие шарики такого же цвета, как и ведро, не ошибаясь' + '\n'
                                 'и получая очки за каждый правильно пойманный шарик.' + '\n'+ '\n'
                                 '●Игра заканчивается при ошибочно пойманном шарике')
        self.instruction.move(20, 50)
