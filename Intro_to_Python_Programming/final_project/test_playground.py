import random
from graphics import *


dict = {
    1 : 'duck',
    2 : 'horse',
    3: 'goat'
}


def main():

    win = GraphWin("Testing", 600, 600)
    ball = Circle(Point(300, 300), 12)

    ball.setFill('red')
    ball.draw(win)

    for i in range (100):
        ball.move(2, 0)
        time.sleep(.02)
    
    input()

main()