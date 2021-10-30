from graphics import *


# create classes here and their methods
class Shape():

    def __init__(self, numSides, shapeName, nameAnchor, messageAnchor):
        self.__numSides = numSides
        self.__shapeName = shapeName
        self.__nameAnchor = nameAnchor
        self.__messageAnchor = messageAnchor

    def displayName(self, win:GraphWin):
        shapName = Text(self.__nameAnchor,f'{self.__shapeName}')
        shapName.draw(win)

    def displayNumSides(self, win:GraphWin):
        numSides = Text(self.__messageAnchor, f'A shape as {self.__numSides} sides')
        numSides.draw(win)


class Square(Shape):

    def __init__(self, nameAnchor, messageAnchor):
        super().__init__(4, 'Square', nameAnchor, messageAnchor)
    
    def drawShape(self, win:GraphWin):
        squareShape = Rectangle(Point(50, 50), Point(250, 250))
        squareShape.setFill('blue')
        squareShape.draw(win)

class Ball(Shape):
    def __init__(self, nameAnchor, messageAnchor):
        super().__init__(0, "Circle", nameAnchor, messageAnchor)

    def drawShape(self, win:GraphWin):
        circleShape = Circle(Point(450, 100), 50)
        circleShape.setFill('Yellow')
        circleShape.draw(win)

class Triangle(Shape):

    def __init__(self, nameAnchor, messageAnchor):
        super().__init__(3, "Triangle", nameAnchor, messageAnchor)

    def drawShape(self, win:GraphWin):
        triangleShape = Polygon(Point(50, 500), Point(100, 400), Point(150, 500))
        triangleShape.setFill('Orange')
        triangleShape.draw(win)


class Octagon(Shape):

    def __init__(self, nameAnchor, messageAnchor):
        super().__init__("8", "Octagon", nameAnchor, messageAnchor)

    def drawShape(self, win:GraphWin):
        octagonShape = Polygon(Point(400, 400), Point(450, 400), Point(500, 450), Point(500, 500), Point(450, 550), Point(400, 550), Point(350, 500), Point(350, 450))
        octagonShape.setFill("Purple")
        octagonShape.draw(win)

    



def main():
    win = GraphWin("Shape Test", 600, 600)
    l1 = Line(Point(300, 0), Point(300, 600))
    l2 = Line(Point(0, 300), Point(600, 300))
    l1.draw(win)
    l2.draw(win)

    shapes = []
    shapes.append(Square(Point(50, 20), Point(100, 280)))
    shapes.append(Ball(Point(350, 20), Point(400, 280)))  # remove comment to test Ball
    shapes.append(Triangle(Point(50, 320), Point(100, 570)))  # remove comment to test Triangle
    shapes.append(Octagon(Point(350, 320), Point(400, 570)))  # remove comment to test Octagon

    for shape in shapes:
        shape.displayName(win)
        shape.displayNumSides(win)
        shape.drawShape(win)


    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()




