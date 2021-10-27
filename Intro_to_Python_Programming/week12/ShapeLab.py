from graphics import *


# create classes here and their methods
class Shape():
    def __init__(self, numSides, shapeName, nameAnchor, messageAnchor):
        self.__numSides = numSides
        self.__shapeName = shapeName
        self.__nameAnchor = nameAnchor
        self.__messageAnchor = messageAnchor

    def displayName(self, win:GraphWin):
        message = f'{self.__shapeName}'

    def displayNumSides(self, win:GraphWin):
        message = f'{self.__numSides}'

class Square(Shape):

    def __init__(self, numSides, shapeName, nameAnchor, messageAnchor):
        super().__init__(numSides, shapeName, nameAnchor, messageAnchor)
        self.__nameAnchor = nameAnchor
        self.__messageAnchor = messageAnchor

    def drawShape(self, win:GraphWin):
        pass

class Ball(Shape):
    pass

class Triangle(Shape):
    pass

class Octagon(Shape):
    pass





def main():
    win = GraphWin("Shape Test", 600, 600)
    l1 = Line(Point(300, 0), Point(300, 600))
    l2 = Line(Point(0, 300), Point(600, 300))
    l1.draw(win)
    l2.draw(win)

    shapes = []
    shapes.append(Square(Point(50, 20), Point(100, 280)))
    # shapes.append(Ball(Point(350, 20), Point(400, 280)))  # remove comment to test Ball
    # shapes.append(Triangle(Point(50, 320), Point(100, 570)))  # remove comment to test Triangle
    # shapes.append(Octagon(Point(350, 320), Point(400, 570)))  # remove comment to test Octagon

    for shape in shapes:
        shape.displayName(win)
        shape.displayNumSides(win)
        shape.drawShape(win)


    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()




