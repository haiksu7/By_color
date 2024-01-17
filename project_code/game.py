from random import randint, choice
import pygame
import sqlite3
from project_code.balls import Balls, load_image
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QDialog, QLabel
from project_code.Checking import Checking
from project_code.show_table import Show_Table
FPS = 40
N = 100
lvl = []
result = []


# Создание игры
class Game(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        pygame.font.init()
        self.size = self.width, self.height = 1000, 800
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("По цвету")
        self.clock = pygame.time.Clock()
        self.score = 0
        self.f = pygame.font.SysFont("arial", 50)
        self.backround = load_image("empty.png")
        self.lvl = lvl[-1]

        # Условия уровня
        self.values = Checking.lvl(self, lvl)
        self.indexes = [1, 2, 3, 4, 5, 6, 7, 8]
        self.players = [load_image(filename, (0, 0, 0)) for filename in self.values[0]]
        self.player = self.create_bucket()
        self.player_rect = self.player.get_rect(centerx=430, bottom=self.height - 20)

        pygame.time.set_timer(pygame.USEREVENT, self.values[4])
        self.all_balls = pygame.sprite.Group()
        self.balls_images = self.values[1]
        self.balls_serf = [load_image(filename["filename"], (0, 0, 0)) for filename in self.balls_images]

        self.speed = self.values[3]

        self.run_game()

    # Создание ведра
    def create_bucket(self):
        ind = randint(0, len(self.players) - 1)
        self.bucket_ind = self.indexes[ind]
        return self.players[ind]

    # Создание шариков
    def create_balls(self, group):
        ind = randint(0, len(self.balls_serf) - 1)
        x = randint(20, self.width - 20)
        speed = self.values[2]
        self.ball_ind = self.indexes[ind]
        return Balls(x, speed, self.balls_serf[ind], self.balls_images[ind]['ind'], group)

    # Проверка столкновений
    def collide(self):
        pygame.mixer.pre_init(44100, -16, 1, 512)
        pygame.font.init()
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
                        self.flag = choice(self.values[-1])
                else:
                    self.game_over()
                ball.kill()

    # Запуск игры
    def run_game(self):
        pygame.init()
        pygame.font.init()
        pygame.mixer.music.load("data\empty_sekai.mp3")
        pygame.mixer.music.play(-1)
        self.running = True
        self.gameover = False
        to_left = False
        to_right = False
        self.flag = choice(self.values[-1])
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
                if self.player_rect.x > self.width - N:
                    self.player_rect.x = self.width - N
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
            self.scoretxt = self.f.render("Счёт: " + str(self.score), True, (0, 0, 0))
            self.screen.blit(self.scoretxt, (20, 10))
            pygame.display.update()
            self.clock.tick(FPS)
            self.all_balls.update(self.height)
            pygame.display.flip()
        pygame.display.quit()
        pygame.quit()
        if self.gameover:
            self.gameover = False
            GameOver().exec_()

    def game_over(self):
        self.running = False
        self.all_balls = pygame.sprite.Group()

        result.append((self.lvl, self.score))
        self.gameover = True


# Проигрыш
class GameOver(QDialog):
    def __init__(self):
        super().__init__()

        self.setGeometry(650, 300, 500, 500)
        self.setWindowTitle('Конец игры')

        self.music()
        self.the_best_last()
        self.base_add()
        self.the_best_new()

        self.pixmap = QPixmap('data\Проигрыш.png')
        self.image = QLabel(self)
        self.image.move(0, -150)
        self.image.setPixmap(self.pixmap)

        self.head = QLabel(self)
        self.head.setText('--Вы ошиблись--')
        self.head.move(130, 50)

        self.question = QLabel(self)
        self.question.setText('Ваши очки: ' + str(result[-1][1]))
        self.question.move(100, 110)

        self.bestres = QLabel(self)
        self.bestres.setText('Ваш лучший результат на этом уровне: ' + str(self.best_new))
        self.bestres.move(50, 140)

        if self.best_last < self.best_new:
            self.record = QLabel(self)
            self.record.setText('Рекорд!!')
            self.record.move(370, 150)

        self.again = QPushButton(self)
        self.again.move(140, 180)
        self.again.setText("Заново?")
        self.again.clicked.connect(self.rerun)

        self.getres = QPushButton(self)
        self.getres.move(120, 230)
        self.getres.setText("Показать все результаты?")
        self.getres.clicked.connect(self.get_all_results)

    def get_all_results(self):
        Show_Table().exec_()

    # Создание/обновления БД
    def base_add(self):
        self.bd = sqlite3.connect("database.db")
        self.cursor = self.bd.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS [Все игры] (Уровень TEXT,
                            Очки INT)""")
        self.bd.commit()

        ins = "INSERT INTO [Все игры] VALUES(?,?)"
        self.cursor.execute(ins, (result[-1][0], result[-1][1]))
        self.bd.commit()

    # Проверка на рекорд
    def the_best_last(self):
        self.bd = sqlite3.connect("database.db")
        self.cursor = self.bd.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS [Все игры] (Уровень TEXT,
                            Очки INT)""")
        ress = self.cursor.execute("""SELECT * FROM [Все игры]""").fetchall()
        res = []
        if ress:
            for el in ress:
                if el[0] == result[-1][0]:
                    res.append(el[1])
            if res:
                self.best_last = max(res)
            else:
                self.best_last = 0
        else:
            self.best_last = 0
            print(6)
        self.bd.close()

    # Выявление лучшего результата на уровне
    def the_best_new(self):
        self.bd = sqlite3.connect("database.db")
        self.cursor = self.bd.cursor()
        ress = self.cursor.execute("""SELECT * FROM [Все игры]""").fetchall()
        res = []
        for el in ress:
            if el[0] == result[-1][0]:
                res.append(el[1])
        self.best_new = max(res)
        self.bd.close()

    def music(self):
        pygame.init()
        pygame.mixer.Sound("data\duolingo_wrong.mp3").play()

    # В случае перезапуска
    def rerun(self):
        self.close()
        player = Game()
