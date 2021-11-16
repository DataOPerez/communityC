
from Snake import *
import random

class Mouse(object):

    miceEaten = 0
    bad_miceEaten = 0

    def __init__(self, win:GraphWin, goodMouse = True):
        self.__x = random.randrange(0, win.getWidth() - 20, 20)
        self.__y = random.randrange(0, win.getHeight() - 20, 20)
        self.mouse = Rectangle(Point(self.__x, self.__y), Point(self.__x + 20, self.__y + 20))
        self.goodMouse = goodMouse

    def __str__(self):
        return f"Mouse Location ({self.__x}, {self.__y})"

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def drawMouse(self, win: GraphWin):
        self.mouse.setFill("Blue")
        self.mouse.draw(win)

    def goodLocation(self, x, y, snake:Snake):
        for part in snake.getParts():
            if part.getX() == x and part.getY() == y:
                return False
        return True

    def eaten(self, snake:Snake, win:GraphWin):
        if self.goodMouse == True:
            Mouse.miceEaten += 1
        else:
            Mouse.bad_miceEaten +=1

        newX = random.randrange(0, win.getWidth() - 20, 20)
        newY = random.randrange(0, win.getHeight() - 20 , 20)
        while not self.goodLocation(newX, newY, snake):
            newX = random.randrange(0, win.getWidth() - 20, 20)
            newY = random.randrange(0, win.getHeight() - 20, 20)
        dx = newX - self.__x
        dy = newY - self.__y
        self.mouse.move(dx, dy)
        self.__x = newX
        self.__y = newY
        if self.goodMouse == False:
            BadMouse.drawMouseRandomSize(self, win)


class BadMouse(Mouse):
    '''Creates a bad mouse. If three bad mice are eaten snake dies.'''

    def __init__(self, win:GraphWin):
        super().__init__(win, goodMouse=False)

    def drawMouse(self, win:GraphWin):
        self.mouse.setFill('BLACK')
        self.mouse.setOutline('RED')
        self.mouse.draw(win)
    
    def drawMouseRandomSize(self, win:GraphWin):
        increase = random.randrange(20, 80, 20)
        self.mouse.undraw()
        self.mouse = Rectangle(Point(self.getX(), self.getY()), Point(self.getX() + increase, self.getY() + increase))
        self.drawMouse(win)
        
        

        

if __name__ == '__main__':
    win = GraphWin("Mouse Test", 600, 600)
    mouse = Mouse(win)
    snake = Snake(300, 400)
    snake.draw(win)
    mouse.drawMouse(win)

    badMouse = BadMouse(win)
    badMouse.drawMouse(win)
    while not win.closed:
        win.getMouse()
        mouse.eaten(snake, win)
        badMouse.eaten(snake, win)
        badMouse.drawMouseRandomSize(win)
        
        print(mouse)
        
