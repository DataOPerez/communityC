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

from time import sleep
from graphics import *
import random as rand

win = GraphWin('Shell Game', 600, 600, autoflush=False)

ball_locations = {
        0 : [150, 300],
        1 : [300, 300],
        2 : [450, 300]
    }

shell_locations = {
        0 : [Point(100, 275), Point(200, 375)],
        1 : [Point(250, 275), Point(350, 375)],
        2 : [Point(400, 275), Point(500, 375)]
    }

color_list = [
    'lime',
    'aqua',
    'fuchsia'
]

class Ball_Prize():
    
    def __init__(self, xPos = 300, yPos = 300):
        ''' Creates data attributes for the ball. '''
        self.__xPos = xPos
        self.__yPos = yPos
        self.__location = 2
        self.__size = 10
        self.__color = 'red'
        self.__ball = Circle(Point(self.__xPos, self.__yPos), self.__size)

    def __str__(self):
        ''' Returns a string representation of the instance of "Ball_Prize. Returning size, color, and location". '''
        return f'Ball size: {self.__size}\nBall Color: {self.__color}\nBall location: {ball_locations[self.__location]},\nBall Center: {self.__ball.getCenter()}'

    def drawBall(self, win:GraphWin, xPos = 300, yPos = 300):
        ''' Draws the ball. '''
        self.__ball.undraw() # undrawing. mainly bc the moveBallLocation calls this method and passes new xPos and yPos.
        self.__ball = Circle(Point(xPos, yPos), self.__size)
        self.__ball.setFill(self.__color)
        self.__ball.draw(win)

    def moveBallLocation(self):
        ''' Randomly selects a position for the ball'''
        self.__location = rand.randrange(0, 3) # using random.randrange one of three positions
        self.__xPos, self.__yPos = ball_locations[self.__location] # get new pre-assigned xPos and yPos
        
        self.drawBall(win, self.__xPos, self.__yPos) # redraw the ball calling the drawBall method

class Shell():
    ''' Crates shell object'''
    def __init__(self, boundBox_pointA, boundBox_pointB, location, color = 'yellow'):
        self.__location = location
        self.__shell = Arc(boundBox_pointA, boundBox_pointB, 0, 180)
        self.__color = color

    def __str__(self):
        return f'Shell Color: {self.__color}\n Shell Location: {self.__location}\n Shell Center: {self.__shell.getCenter()}'
    
    def drawShell(self, win, pointA, pointB = Point(350, 375)):
        self.__shell.undraw()
        self.__shell = Arc(pointA, pointB, 0, 180)
        self.__shell.setFill(self.__color)
        self.__shell.draw(win)

    @staticmethod
    def shuffleShells(shellList: list):
        '''I believe the idea is shuffle the first one up and the second down everytime. '''
        randomNumberList = []

        while len(randomNumberList) < 2:
            num = rand.randrange(0, 3)
            if num not in randomNumberList:
                randomNumberList.append(num)
        if randomNumberList[0] < randomNumberList[1]:
            
            shellOne = shellList[randomNumberList[0]]
            shellTwo = shellList[randomNumberList[1]]
        else:
            shellOne = shellList[randomNumberList[1]]
            shellTwo = shellList[randomNumberList[0]]

            shellOneLocation = shellOne.__location
            shellTwoLocation = shellTwo.__location

            if shellOne.__location == 0:
                print('location 0')
                shellOne.__shell.move(150, -150)
                update(3)
                shellOne.drawShell(win, shell_locations[shellTwo.__location][0], shell_locations[shellTwo.__location][1])
                shellOne.__location = shellTwoLocation
            elif shellOne.__location == 1:
                print('location 1')
                shellOne.__shell.move(0, -150)
                update(3)
                shellOne.drawShell(win, shell_locations[shellTwo.__location][0], shell_locations[shellTwo.__location][1])
                shellOne.__location = shellTwoLocation
            else:
                print('location 2, this shouldnt be possible')
            
            if shellTwo.__location == 0:
                print('location 0, this shouldn\'t be possible')
            elif shellTwo.__location == 1:
                print('location 1')
                shellTwo.__shell.move(0, 150)
                update(3)
                shellTwo.drawShell(win, shell_locations[shellOne.__location][0], shell_locations[shellOne.__location][1])
                shellTwo.__location = shellOneLocation
            else:
                print('location 2')
                shellTwo.__shell.move(-150, 150)
                update(3)
                shellTwo.drawShell(win, shell_locations[shellOne.__location][0], shell_locations[shellOne.__location][1])
                shellTwo.__location = shellOneLocation




def main():
    ball = Ball_Prize()
    ball.drawBall(win)

    win.getMouse()

    shell_list = []
    for i in range(0, 3):
        shell = Shell(shell_locations[i][0], shell_locations[i][1], i, color_list[i])
        shell.drawShell(win, shell_locations[i][0], shell_locations[i][1])
        shell_list.append(shell)

    win.getMouse()

    for i in range(20):
        Shell.shuffleShells(shell_list)
        update(2)
        #win.getMouse()
        
    
        

    win.getMouse()


main()
