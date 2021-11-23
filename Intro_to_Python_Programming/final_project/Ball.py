from random import *
from graphics import *
from shell_game_v2 import *



class Ball():

    def __init__(self, centerPoint:Point, color = 'red', size = 12):
        self.__centerPoint = centerPoint
        self.__x = centerPoint.getX()
        self.__y = centerPoint.getY()
        self.ball = Circle(Point(self.__x, self.__y), size)

        self.color = color

    def __str__(self):
        return f'Ball Position: {self.__centerPoint}'
    
    def drawBall(self, win:GraphWin):
        self.ball.setFill(self.color)
        self.ball.draw(win)

    def undrawBall(self):
        self.ball.undraw()
    
    def getCenterPoint(self):
        return self.__centerPoint
    
    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def setCenterPoint(self, newCenterPoint:Point):
        self.__centerPoint = newCenterPoint

    def setX(self, newX):
        self.__x = newX

    def setY(self, newY):
        self.__y = newY
    
    def moveBall(self, newCenterPoint:Point, speed = .01):
        newX = newCenterPoint.getX()
        newY = newCenterPoint.getY()

        dx = (self.__x - newX) * -1
        dy = (self.__y - newY) * -1

        for i in range(15):
            self.ball.move(dx // 15, dy // 15)
            time.sleep(.008)

        self.__centerPoint = newCenterPoint
        self.__x = newX
        self.__y = newY


def main():
    win = GraphWin("Ball Test", 600, 600)

    Line(Point(150, 0), Point(150, 600)).draw(win)
    Line(Point(300, 0), Point(300, 600)).draw(win)
    Line(Point(450, 0), Point(450, 600)).draw(win)
    Line(Point(600, 0), Point(600, 600)).draw(win)

    Line(Point(0, 150), Point(600, 150)).draw(win)
    Line(Point(0, 300), Point(600, 300)).draw(win)
    Line(Point(0, 450), Point(600, 450)).draw(win)
    Line(Point(0, 600), Point(600, 600)).draw(win)

    ball = Ball(POSITIONS_LIST[1])
    ball.drawBall(win)
    print('ball drawn')
    print(ball)
    win.getMouse()

    for i in range(12):
        ball.moveBall(POSITIONS_LIST_WITH_Y[randrange(0,len(POSITIONS_LIST_WITH_Y))])
        print(ball)
        


if __name__ == '__main__':
    main()