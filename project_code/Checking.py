# Проверка уровня, установление порядка для выбранной сложности
class Checking:
    def lvl(self, lvl):
        players = ["ведроred.png", "ведроgreen.png", "ведроblue.png", "ведроyellow.png", "ведроpink.png",
                   "ведроlightblue.png", "ведроorange.png", "ведроviolet.png"]

        databall = [{"filename": "red.png", "ind": 1}, {"filename": "green.png", "ind": 2},
                    {"filename": "blue.png", "ind": 3},
                    {"filename": "yellow.png", "ind": 4}, {"filename": "pink.png", "ind": 5},
                    {"filename": "lightblue.png", "ind": 6},
                    {"filename": "orange.png", "ind": 7}, {"filename": "violet.png", "ind": 8}]

        if lvl[-1] == "Легко":
            self.players = players[:3]
            self.balls_images = databall[:3]
            self.speedball = 10
            self.speedplayer = 15
            self.eventball = 1000
            self.flag = [-1]

        elif lvl[-1] == "Нормально":
            self.players = players[:5]
            self.balls_images = databall[:5]
            self.speedball = 15
            self.speedplayer = 20
            self.eventball = 500
            self.flag = [4, 5]

        elif lvl[-1] == "Сложно":
            self.players = players
            self.balls_images = databall
            self.speedball = 20
            self.eventball = 300
            self.speedplayer = 25
            self.flag = [1, 2, 3]
        return (self.players, self.balls_images, self.speedball, self.speedplayer, self.eventball, self.flag)
