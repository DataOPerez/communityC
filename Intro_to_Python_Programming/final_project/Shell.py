
from random import *
from Ball import *
from graphics import *
from shell_game_v2 import *

class Shell():

    def __init__(self, centerPoint, color='pink'):
        self.__centerPoint = centerPoint
        self.__x = centerPoint.getX()
        self.__y = centerPoint.getY()
        self.__winningShellStatus = False

        self.shell = Arc(Point(self.__x - 48, self.__y - 36), Point(self.__x + 48, self.__y + 60), 0, 180)
        self.color = color

    def __str__(self):
        return f'Shell position: {self.__centerPoint}'
    
    def drawShell(self, win:GraphWin):
        self.shell.setFill(self.color)
        self.shell.draw(win)

    def undrawShell(self):
        self.shell.undraw()

    def getCenterPoint(self):
        return self.__centerPoint

    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def getWinningShellStatus(self):
        return self.__winningShellStatus

    def setWinningShellStatus(self, status:bool):
        self.__winningShellStatus = status

    def checkIfSellHasBall(self, ball):
        if Circle.testCollision_CircleVsPoint(ball.ball, self.__centerPoint):
            self.__winningShellStatus = True
        else:
            pass

    def moveShell(self, newCenterPoint:Point, speed = .01):
        newX = newCenterPoint.getX()
        newY = newCenterPoint.getY()

        dx = (self.__x - newX) * -1
        dy = (self.__y - newY) * -1

        for i in range(15):
            self.shell.move(dx // 15, dy // 15)
            time.sleep(speed)

        self.__centerPoint = newCenterPoint
        self.__x = newX
        self.__y = newY

    @staticmethod
    def shuffleTwoShells(shell1, shell2, speed = .01):
        shell1_centerPoint = shell1.getCenterPoint()
        shell2_centerPoint = shell2.getCenterPoint()

        shell1.moveShell(shell2_centerPoint, speed)
        shell2.moveShell(shell1_centerPoint, speed)

def main():
    win = GraphWin('Shell Test', 600, 600)

    Line(Point(150, 0), Point(150, 600)).draw(win)
    Line(Point(300, 0), Point(300, 600)).draw(win)
    Line(Point(450, 0), Point(450, 600)).draw(win)
    Line(Point(600, 0), Point(600, 600)).draw(win)

    Line(Point(0, 150), Point(600, 150)).draw(win)
    Line(Point(0, 300), Point(600, 300)).draw(win)
    Line(Point(0, 450), Point(600, 450)).draw(win)
    Line(Point(0, 600), Point(600, 600)).draw(win)

    shell_list = []
    for i in range(0, 4):
        shell = Shell(POSITIONS_LIST_WITH_Y[i], SHELL_COLOR_LIST[i])
        shell.drawShell(win)
        shell_list.append(shell)
        

    ball = Ball(POSITIONS_LIST_WITH_Y[3])
    ball.drawBall(win)
    win.getMouse()

    for shell in shell_list:
        shell.checkIfSellHasBall(ball)
        if shell.getWinningShellStatus():
            print(shell.color, "has the ball ")
    win.getMouse()


if __name__ == '__main__':
    main()