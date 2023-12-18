
import random
import pygame
from project_code.balls import Balls, load_image
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QPushButton
from PyQt5.QtWidgets import QDialog, QLabel

FPS = 40

all_balls = pygame.sprite.Group()


class StartWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(600, 300, 700, 500)
        self.setWindowTitle('По цвету')

        self.pixmap = QPixmap('../data/фонстарт.png')
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
        self.instruction.move(300, 400)
        self.instruction.setText("Инструкция")
        self.instruction.clicked.connect(self.get_instruction)

        self.text = QLabel(self)
        self.text.move(275, 310)
        self.text.setText("★Наполни мир красками!★")

    def run1(self):
        self.checking()
        player = Game()

    def checking(self):
        self.a = self.sender().text()
        if self.a == 'Легко':
            return 1
        elif self.a == 'Нормально':
            return 2
        elif self.a == 'Сложно':
            return 3

    def get_instruction(self):
        get = Instruction()
        get.exec_()

def hard_of_lvl(x):
    if x == 1:
        speed = 30
        count_ball = 30
        return (speed, count_ball)

    elif x == 1:
        speed = 30
        count_ball = 30
        return (speed, count_ball)

    elif x == 1:
        speed = 30
        count_ball = 30
        return (speed, count_ball)


class Instruction(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Инструкция")
        self.setGeometry(650, 400, 630, 300)

        self.pixmap = QPixmap('../data/Инструкцияфон.png')
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




class Cheking:
    def __init__(self, a):
        self.a = a

    def checking(self):
        if self.a == 'Легко':
            return 1
        elif self.a == 'Нормально':
            return 2
        elif self.a == 'Сложно':
            return 3


class Game(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.size = self.width, self.height = 1000, 800
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("По цвету")
        self.screen.fill((255, 255, 255))
       # self.level_hard = StartWindow.checking
        self.clock = pygame.time.Clock()
        self.score = 0
        self.backround = load_image("empty.png")

        self.player = load_image("ведроred.png", (0, 0, 0))
        self.x = 430
        self.y = self.height - 110

        self.speed = 10
        self.b1 = Balls(self.height // 2 - 100, self.speed, "green.png")
        self.b2 = Balls(self.height // 2 + 100, self.speed, "red.png")
        self.b3 = Balls(self.height // 2, self.speed, "blue.png")
        all_balls.add(self.b1, self.b2, self.b3)

        self.run_game()

    def run_game(self):
        running = True
        to_left = False
        to_right = False
        while running:
            flag = random.choice(torf)
            if flag:
                pass

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        to_left = True
                    if event.key == pygame.K_RIGHT:
                        to_right = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        to_left = False
                    if event.key == pygame.K_RIGHT:
                        to_right = False
                    if event.type == pygame.QUIT:
                        running = False
            if to_right:
                self.x += 5
            if to_left:
                self.x -= 5
            self.screen.blit(self.backround, (0, 0))
            all_balls.draw(self.screen)
            self.screen.blit(self.player, (self.x, self.y))
            pygame.display.flip()
            pygame.display.update()
            self.clock.tick(FPS)
            all_balls.update(self.height)
        pygame.quit()

    def game_over(self):
        pass


torf = [True, False]