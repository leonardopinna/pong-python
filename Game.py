import constants as k

class Game:
    def __init__(self, player1, player2, ball) -> None:
        self.player1 = player1
        self.player2 = player2
        self.ball = ball
        self.is_running = True
        self.counter = 0 #necessario per evitare rimbalzi multipli nel giro di alcuni frame consecutivi

    def game_loop(self):
        self.ball.move()
        self.check_bounce_with_players()
        self.check_bounce_with_walls()
    
    def ball_reached_walls(self):
        return self.ball.y <=k.STEP or self.ball.y >=k.HEIGHT-k.STEP
    
    def check_bounce_with_walls(self):
        if self.ball_reached_walls():
            self.ball.bounce_wall()

    def check_bounce_with_player1(self):
        if self.counter == 0:
            if (self.ball.x - self.ball.radius  <= self.player1.x + self.player1.width and self.ball.x - self.ball.radius  >= self.player1.x + self.player1.width*0.5) and (self.ball.y >= self.player1.y and self.ball.y <= self.player1.y + self.player1.heigth):
                self.ball.bounce_player_front()
                self.counter = 5
            elif (self.ball.y + self.ball.radius >= self.player1.y and self.ball.y - self.ball.radius <= self.player1.y + self.player1.heigth) and (self.ball.x >= self.player1.x and self.ball.x <= self.player1.x + self.player1.width):
                self.ball.bounce_player_side()
                self.counter = 5    
        elif self.counter > 0:
                self.counter -= 1
    
    def check_bounce_with_player2(self):
        if (self.ball.x + self.ball.radius  >= self.player2.x and self.ball.x + self.ball.radius  <= self.player2.x + self.player2.width*0.5) and (self.ball.y >= self.player2.y and self.ball.y <= self.player2.y + self.player2.heigth):
                self.ball.bounce_player_front()
                self.counter = 5
        elif (self.ball.y + self.ball.radius >= self.player2.y and self.ball.y - self.ball.radius <= self.player2.y + self.player2.heigth) and (self.ball.x <= self.player2.x + self.player2.width and self.ball.x >= self.player2.x):
                self.ball.bounce_player_side()
                self.counter = 5 

    def check_bounce_with_players(self):
        self.check_bounce_with_player1()
        self.check_bounce_with_player2()

    def new_game(self):
        self.isrunning = True
        self.player1.score = 0
        self.player2.score = 0
        self.counter = 0