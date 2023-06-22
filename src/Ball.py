import constants as k
import cmath

class Ball:
    def __init__(self,x,y,speed, alpha, radius):
        self.alpha = alpha
        self.speed = speed
        self.x = x
        self.y = y
        self.dx = self.speed * cmath.cos(alpha).real
        self.dy = self.speed * cmath.sin(alpha).real
        self.radius = radius

    def move(self):
        self.x = self.x + self.dx 
        self.y = self.y + self.dy
    
    def bounce_wall(self):
        self.dy = -self.dy*1.05
        self.dx = +self.dx*1.05

    def bounce_player_side(self):
        self.dy = -self.dy
    
    def bounce_player_front(self):
        self.dx = -self.dx
    

    