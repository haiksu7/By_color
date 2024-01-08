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
            self.speedball = 5
            self.speedplayer = 10
            self.eventball = 2000
            self.flag = -1

        elif lvl[-1] == "Нормально":
            self.players = players[:5]
            self.balls_images = databall[:5]
            self.speedball = 10
            self.speedplayer = 15
            self.eventball = 900
            self.flag = 5

        elif lvl[-1] == "Сложно":
            self.players = players
            self.balls_images = databall
            self.speedball = 15
            self.eventball = 300
            self.speedplayer = 20
            self.flag = 3
        return (self.players, self.balls_images, self.speedball, self.speedplayer, self.eventball, self.flag)