# create a shell game

# objects: shell, the ball

# shell
'''
### Data attributes
-  number of shells
- position of shells

### Methods
- Draw the shell
'''

# ball
'''
### Data attributes
- location of ball
- position
### Methods
- draw the ball

'''

from graphics import *
import random as rand

win = GraphWin('Shell Game', 600, 600)

class Ball_Prize():
    location_dict = {
        1 : [150, 300],
        2 : [300, 300],
        3 : [450, 300]
    }
    
    def __init__(self, xPos = 300, yPos = 300,):
        ''' Creates data attributes for the ball. '''
        self.__xPos = xPos
        self.__yPos = yPos
        self.__location = 2
        self.__size = 10
        self.__color = 'red'
        self.__ball = Circle(Point(self.__xPos, self.__yPos), self.__size)

    def __str__(self):
        ''' Returns a string representation of the instance of "Ball_Prize. Returning size, color, and location". '''
        return f'Ball size: {self.__size} Ball Color: {self.__color} Ball Position: {self.location_dict[self.__location]}'

    def drawBall(self, win:GraphWin, xPos=300, yPos=300):
        ''' Draws the ball. '''
        self.__ball.undraw() # undrawing. mainly bc the moveBallLocation calls this method and passes new xPos and yPos.
        self.__ball = Circle(Point(xPos, yPos), self.__size)
        self.__ball.setFill(self.__color)
        self.__ball.draw(win)

    def moveBallLocation(self):
        ''' Randomly selects a position for the ball'''
        newLocation = rand.randrange(1, 4) # using random.randrange one of three positions
        xPos, yPos = self.location_dict[newLocation] # get new pre-assigned xPos and yPos
        
        self.drawBall(win, xPos, yPos) # redraw the ball calling the drawBall method



def main():
    ball = Ball_Prize()

    ball.drawBall(win)
    win.getMouse()

    for i in range(20):
        ball.moveBallLocation()
        time.sleep(.5)



main()
