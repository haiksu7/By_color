from random import randint
import pygame
import sqlite3
from PyQt5.QtWidgets import QDialog, QTableWidget, QHBoxLayout, QTableWidgetItem
from PyQt5.QtCore import Qt
from project_code.balls import Balls, load_image
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QPushButton, QMessageBox
from PyQt5.QtWidgets import QDialog, QLabel
from Checking import Checking
FPS = 40
lvl = []
result = []


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
        self.instruction.move(300, 400)
        self.instruction.setText("Инструкция")
        self.instruction.clicked.connect(self.get_instruction)

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


class Game(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.size = self.width, self.height = 1000, 800
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("По цвету")
        self.screen.fill((255, 255, 255))
        self.clock = pygame.time.Clock()
        self.score = 0
       # self.f = pygame.font.Font("arial", 30)
        self.backround = load_image("empty.png")
        self.lvl = lvl[-1]
        self.ok = Checking.lvl(self, lvl)
        self.indexes = [1, 2, 3, 4, 5, 6, 7, 8]
        self.players = [load_image(filename, (0, 0, 0)) for filename in self.ok[0]]
        self.player = self.create_bucket()
        self.player_rect = self.player.get_rect(centerx=430, bottom=self.height - 20)

        pygame.time.set_timer(pygame.USEREVENT, self.ok[4])
        self.all_balls = pygame.sprite.Group()
        self.balls_images = self.ok[1]
        self.balls_serf = [load_image(filename["filename"], (0, 0, 0)) for filename in self.balls_images]

        self.speed = self.ok[3]

        self.run_game()

    def create_bucket(self):
        ind = randint(0, len(self.players) - 1)
        self.bucket_ind = self.indexes[ind]
        return self.players[ind]

    def create_balls(self, group):
        ind = randint(0, len(self.balls_serf) - 1)
        x = randint(20, self.width - 20)
        speed = self.ok[2]
        self.ball_ind = self.indexes[ind]
        return Balls(x, speed, self.balls_serf[ind], self.balls_images[ind]['ind'], group)

    def collide(self):
        pygame.mixer.pre_init(44100, -16, 1, 512)
        pygame.init()
        for ball in self.all_balls:
            if self.player_rect.collidepoint(ball.rect.center):
                if self.bucket_ind == ball.ind:
                    pygame.mixer.Sound("data\duolingo_correct.mp3").play()
                    self.score += 1
                    self.counter += 1
                    if self.counter == self.flag:
                        self.player = self.create_bucket()
                        self.counter = 0
                else:
                    self.game_over()
                ball.kill()

    def run_game(self):
        pygame.init()
        pygame.mixer.music.load("data\empty_sekai.mp3")
        pygame.mixer.music.play(-1)
        self.running = True
        to_left = False
        to_right = False
        self.flag = self.ok[-1]
        self.counter = 0
        while self.running:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.USEREVENT:
                    self.create_balls(self.all_balls)

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
                        self.running = False
            if to_right:
                if self.player_rect.x > self.width - 100:
                    self.player_rect.x = self.width - 100
                else:
                    self.player_rect.x += self.speed
            if to_left:
                if self.player_rect.x < 0:
                    self.player_rect.x = 0
                else:
                    self.player_rect.x -= self.speed
            self.collide()
            self.screen.blit(self.backround, (0, 0))
            self.all_balls.draw(self.screen)
            self.screen.blit(self.player, self.player_rect)
            pygame.display.flip()
            pygame.display.update()
            self.clock.tick(FPS)
            self.all_balls.update(self.height)
           # scoretxt = self.f.render(str(self.score), True, (0, 0, 0))
           # self.screen.blit(scoretxt, (20, 10))
        pygame.quit()

    def game_over(self):
        self.running = False
        self.all_balls = []
        result.append((self.lvl, self.score))
        pygame.quit()
        GameOver().exec_()


class GameOver(QDialog):
    def __init__(self):
        super().__init__()

        self.setGeometry(400, 200, 1000, 800)
        self.setWindowTitle('Конец игры')

        self.base_add()
        self.the_best()

        self.pixmap = QPixmap('data\Инструкцияфон.png')
        self.image = QLabel(self)
        self.image.move(0, -35)
        self.image.setPixmap(self.pixmap)

        self.head = QLabel(self)
        self.head.setText('--Вы ошиблись--')
        self.head.move(300, 50)

        self.question = QLabel(self)
        self.question.setText('Ваши очки: ' + str(result[-1][1]))
        self.question.move(200, 120)

        self.bestres = QLabel(self)
        self.bestres.setText('Ваш лучший результат на этом уровне: ' + str(self.best))
        self.bestres.move(150, 140)

        self.again = QPushButton(self)
        self.again.move(300, 400)
        self.again.setText("Заново?")
        self.again.clicked.connect(self.rerun)

        self.getres = QPushButton(self)
        self.getres.move(300, 500)
        self.getres.setText("Показать все результаты?")
        self.getres.clicked.connect(self.get_all_results)

        self.music()

    def get_all_results(self):
        Show_Table().exec_()

    def base_add(self):
        self.bd = sqlite3.connect("database.db")
        self.cursor = self.bd.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS [Все игры] (Уровень TEXT,
                            Очки INT)""")
        self.bd.commit()

        ins = "INSERT INTO [Все игры] VALUES(?,?)"
        self.cursor.execute(ins, (result[-1][0], result[-1][1]))
        self.bd.commit()

    def the_best(self):
        self.bd = sqlite3.connect("database.db")
        self.cursor = self.bd.cursor()
        ress = self.cursor.execute("""SELECT * FROM [Все игры]""").fetchall()
        res = []
        for el in ress:
            if el[0] == result[-1][0]:
                res.append(el[1])
        self.best = max(res)
        self.bd.close()

    def music(self):
        pygame.init()
        pygame.mixer.music.load("data\Infinitely_Gray_Instrumental_N25.mp3")
        pygame.mixer.music.play(-1)

    def rerun(self):
        self.close()
        player = Game()


class Show_Table(QDialog):
    def __init__(self):
        super().__init__()
        self.db = sqlite3.connect('database.db')
        self.cursor = self.db.cursor()
        self.resize(230, 230)
        self.setWindowTitle('Последние действия')

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
