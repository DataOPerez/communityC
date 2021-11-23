from Snake import *
from Mouse import *
from obstacle import *
from graphics import *
import time

Rectangle

def getDirection(win:GraphWin, currentDirection):
    key = win.checkKey().lower()
    if key == "up":
        return "N"
    elif key == "down":
        return "S"
    elif key == "right":
        return "E"
    elif key == "left":
        return "W"
    else:
        return currentDirection

def isEaten(mouse:Mouse, snake:Snake):
    bodyParts = snake.getParts()
    if Rectangle.testCollision_RectVsRect(mouse.mouse, bodyParts[0].body):
        return True
    # if mouse.getX() == bodyParts[0].getX() and mouse.getY() == bodyParts[0].getY():
    #     return True
    return False

def hitObstacle(obstacle: Obstacle, snake: Snake):
    bodyParts = snake.getParts()
    if obstacle.getX() == bodyParts[0].getX() and obstacle.getY() == bodyParts[0].getY():
        return True
    return False

def main():
    win = GraphWin("Snake Game", 600, 600)
    snake = Snake(300, 400)
    mouse = Mouse(win)
    badMouse = BadMouse(win)

    snake.draw(win)
    mouse.drawMouse(win)
    badMouse.drawMouse(win)


    while snake.alive:
        direction = getDirection(win, snake.getDirection())
        snake.move(direction, win)
        if isEaten(mouse, snake):
            mouse.eaten(snake, win)
            snake.appendBody(win)
            print(Mouse.miceEaten)
        if isEaten(badMouse, snake):
            badMouse.eaten(snake, win)
            print(Mouse.bad_miceEaten)
        
        if Mouse.bad_miceEaten == 3:
            snake.alive = False

        time.sleep(.1)


if __name__ == '__main__':
    main()