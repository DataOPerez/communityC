from graphics import *
import random
import math
class Bug(object):
    """Blueprint for a bug object"""

    def __init__(self, win:GraphWin):
        self.__size = 10
        self.__centerX = random.randint(self.__size + 5, win.getWidth() - self.__size - 5)
        self.__centerY = random.randint(self.__size + 5, win.getHeight() - self.__size - 5)
        self.__bug = Circle(Point(self.__centerX, self.__centerY), self.__size)
        self.__blue = 255
        self.__red = 0   #increase when it eats other Bug
        self.__dx = random.randrange(-5, 6, 2)
        self.__dy = random.randrange(-5, 6, 2)


    def __str__(self):
        output = f"My bug\n"
        output += f"Size: {self.__size}\n"
        output += f"X: {self.__centerX}\n"
        output += f"Y: {self.__centerY}\n"
        output += f"red: {self.__red}\n"
        output += f"dx: {self.__dx}\n"
        output += f"dy: {self.__dy}\n"
        return output

    def drawBug(self, win):
        """Draw a bug object"""
        self.__bug.setFill(color_rgb(self.__red, 0, self.__blue))
        self.__bug.draw(win)

    def moveBug(self, win:GraphWin):
        """Moves a bug in a random direction"""
        value = random.randint(1, 10)
        if value <= 1:
            self.__dx = random.randrange(-5, 6, 2)
            self.__dy = random.randrange(-5, 6, 2)

        if self.__dx + self.__centerX <= 0:
            self.__dx *= -1
        if self.__dx + self.__centerX >= win.getWidth():
            self.__dx *= -1
        if self.__dy + self.__centerY <= 0:
            self.__dy *= -1
        if self.__dy + self.__centerY >= win.getHeight():
            self.__dy *= -1

        self.__centerX += self.__dx
        self.__centerY += self.__dy
        self.__bug.move(self.__dx, self.__dy)

    def eatBug(self, bugList, win:GraphWin):
        """Defines how one bug eats another bug"""
        for bug in bugList:
            if self.getDistanceToBug(bug) <= self.__size + bug.__size and self.getDistanceToBug(bug) != 0:
                if self.__size >= bug.__size:
                    bug.__bug.undraw()
                    bugList.remove(bug)
                    self.__red += 20
                    self.__size += 20
                    self.__bug.undraw()
                    self.__bug = Circle(Point(self.__centerX, self.__centerY), self.__size )
                    self.drawBug(win)


        # if self.getDistanceToBug(otherBug) <= self.__size + otherBug.__size:
        #     otherBug.__bug.undraw()
        #     self.__bug.undraw()
        #     self.__red += 5
        #     self.__size += 5
        #     self.__bug = Circle(Point(self.__centerX, self.__centerY), self.__size )
        #     self.__bug.draw(win)
        #     return otherBug

    def getDistanceToBug(self, otherBug):
        dx = self.__centerX - otherBug.__centerX
        dy = self.__centerY - otherBug.__centerY
        dis = math.sqrt(dx ** 2 + dy **2)
        return dis







def main():
    win = GraphWin("Bugging Out", 1000, 650, autoflush= False)
    win.setBackground("white")
    bugList = []
    for i in range(40):
        barry = Bug(win)
        barry.drawBug(win)
        bugList.append(barry)
    win.getMouse()
    while True:
        for bug in bugList:
            bug.moveBug(win)
            bug.eatBug(bugList, win)
        

        win.update()
        time.sleep(.02)


        # for bug in bugList:
        #     bug.moveBug(win)
        #     for bug in bugList: #  How do I eat every other bug
        #         bug.eatBug()



    win.close()

if __name__ == '__main__':
    main()