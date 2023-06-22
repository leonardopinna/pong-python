import constants as k

class Player:
    def __init__(self, x, y, width, heigth, step):
        self.x = x
        self.y = y
        self.width = width
        self.heigth = heigth
        self.step = step
        self.score = 0
        

    def move_up(self):
        self.y = self.y - self.step
        if self.y <= 0:
            self.y = 0
        print("up")

    def move_down(self):
        self.y = self.y + self.step
        if self.y + self.heigth >= k.HEIGHT:
            self.y = k.HEIGHT-self.heigth
        print("down")


    def on_release(key):
        print("released")

