from graphics import *
from random import *

class RecursiveGraphic(object):
    COLORS_LIST= [
        'RED',
        'PINK',
        'YELLOW',
        'PURPLE',
        'BLUE',
        'GREEN',
        'ORANGE',
    ]
    
    def __init__(self, win: GraphWin):
        self.startWidth = 250
        self.startHeight = 200
        self.tlX = win.getWidth() // 2 - self.startWidth // 2
        self.tlY = win.getHeight() // 2 - self.startHeight // 2

    def drawRectangles(self, win):
        self.drawCenterRectangle(win)
        # Make the initial call to your method(s) here
        # self.drawRectangle(self.startWidth, self.startHeight, self.tlX, self.tlY, win)

        self.drawTopLeft(self.startWidth, self.startHeight, self.tlX, self.tlY, win)
        self.drawTopRight(self.startWidth, self.startHeight, self.tlX, self.tlY, win)
        self.drawBottomRight(self.startWidth, self.startHeight, self.tlX, self.tlY, win)
        self.drawBottomLeft(self.startWidth, self.startHeight, self.tlX, self.tlY, win)


    def drawCenterRectangle(self, win):
        rect = Rectangle(Point(self.tlX, self.tlY), Point(self.tlX + self.startWidth, self.tlY + self.startHeight))
        rect.setFill('Black')
        rect.draw(win)

    def drawRectangle(self, width, height, tlX, tlY, win:GraphWin, color='black'):
        rect = Rectangle(Point(tlX, tlY), Point(tlX + width, tlY + height))
        rect.setFill(color)
        rect.draw(win)

    # Create your recursive method(s) here     

    def drawTopLeft(self, width, height, tlX, tlY, win):
        color_list = RecursiveGraphic.COLORS_LIST
        randomColor = color_list[randrange(0, len(color_list) - 1)]
        if width > 1:
            halfWidth = width // 2
            halfHeight = height // 2

            new_tlX = tlX - halfWidth
            new_tlY = tlY - halfHeight

            self.drawRectangle(halfWidth, halfHeight, new_tlX, new_tlY, win, randomColor)

            self.drawTopLeft(halfWidth, halfHeight, new_tlX, new_tlY, win)
            self.drawTopRight(halfWidth, halfHeight, new_tlX, new_tlY, win)
            self.drawBottomLeft(halfWidth, halfHeight, new_tlX, new_tlY, win)
    
    def drawTopRight(self, width, height, tlX, tlY, win):
        color_list = RecursiveGraphic.COLORS_LIST
        randomColor = color_list[randrange(0, len(color_list) - 1)]
        if width > 1:
            halfWidth = width // 2
            halfHeight = height // 2

            new_tlX = tlX + (halfWidth * 2)
            new_tlY = tlY - halfHeight

            self.drawRectangle(halfWidth, halfHeight, new_tlX, new_tlY, win, randomColor)

            self.drawTopRight(halfWidth, halfHeight, new_tlX, new_tlY, win)
            self.drawTopLeft(halfWidth, halfHeight, new_tlX, new_tlY, win)
            self.drawBottomRight(halfWidth, halfHeight, new_tlX, new_tlY, win)

    def drawBottomRight(self, width, height, tlX, tlY, win):
        color_list = RecursiveGraphic.COLORS_LIST
        randomColor = color_list[randrange(0, len(color_list) - 1)]
        if width > 1:
            halfWidth = width // 2
            halfHeight = height // 2

            new_tlX = tlX + (halfWidth * 2)
            new_tlY = tlY + (halfHeight * 2)

            self.drawRectangle(halfWidth, halfHeight, new_tlX, new_tlY, win, randomColor)

            self.drawBottomRight(halfWidth, halfHeight, new_tlX, new_tlY, win)
            self.drawTopRight(halfWidth, halfHeight, new_tlX, new_tlY, win)
            self.drawBottomLeft(halfWidth, halfHeight, new_tlX, new_tlY, win)

    def drawBottomLeft(self, width, height, tlX, tlY, win):
        color_list = RecursiveGraphic.COLORS_LIST
        randomColor = color_list[randrange(0, len(color_list) - 1)]
        if width > 1:
            halfWidth = width // 2
            halfHeight = height // 2

            new_tlX = tlX - halfWidth
            new_tlY = tlY + (halfHeight * 2)

            self.drawRectangle(halfWidth, halfHeight, new_tlX, new_tlY, win, randomColor)

            self.drawBottomLeft(halfWidth, halfHeight, new_tlX, new_tlY, win)
            self.drawTopLeft(halfWidth, halfHeight, new_tlX, new_tlY, win)
            self.drawBottomRight(halfWidth, halfHeight, new_tlX, new_tlY, win)



def main():
    win = GraphWin("Recursive Rectangles", 1000, 650)
    rg = RecursiveGraphic(win)
    rg.drawRectangles(win)
    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()