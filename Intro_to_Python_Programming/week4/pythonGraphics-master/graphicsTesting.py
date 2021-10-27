from graphics import *

win = GraphWin("Test window", 600, 400)


myCircle = Circle(Point(200, 250), 100)
myCircle.setFill("Red")
myCircle.setOutline("Blue")
myCircle.setWidth(5)
myCircle.draw(win)

win.getMouse()
win.close()
