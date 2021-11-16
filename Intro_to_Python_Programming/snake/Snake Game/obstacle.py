
import random
from Snake import *
from graphics import *

class Obstacle():
    '''Creates a block the snake should avoid'''

    obstaclesHit_limit = 0

    def __init__(self, win:GraphWin):
        self.__x = random.randrange(0, win.getWidth() - 20, 20)
        self.__y = random.randrange(0, win.getWidth() - 20, 20)
        self.obstacle = Rectangle(Point(self.__x, self.__y), Point(self.__x + 20, self.__y + 20))

    def __str__(self):
        return f'Obstacle location ({self.__x}, {self.__y})'
    
    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def drawObstacle(self, win: GraphWin):
        self.obstacle.setFill('BLACK')
        self.obstacle.draw(win)

    def goodLocation(self, x, y, snake:Snake):
        for part in snake.getParts():
            if part.getX() == x and part.getY() == y:
                return False
        return True
    
    def hit(self, snake: Snake, win:GraphWin):
        Obstacle.obstaclesHit_limit += 1
        randomX = random.randrange(0, win.getWidth() - 20, 20)
        randomY = random.randrange(0, win.getHeight() - 20 , 20)
        while not self.goodLocation(randomX, randomY, snake):
            randomX = random.randrange(0, win.getWidth() - 20, 20)
            randomY = random.randrange(0, win.getHeight() - 20, 20)
        dx = randomX - self.__x
        dy = randomY - self.__y

        self.obstacle.move(dx, dy)
        self.__x = randomX
        self.__y = randomY

if __name__ == "__main__":
    win = GraphWin('Obstalce Test', 600, 600)
    obstacle = Obstacle(win)
    snake = Snake(300, 300)
    snake.draw(win)
    obstacle.drawObstacle(win)
    while not win.closed:
        win.getMouse()
        obstacle.eaten(snake, win)
        print(obstacle)
    
