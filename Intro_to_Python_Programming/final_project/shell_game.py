# objects
'''
PrizeBall
# attributes: location, color, size, ball itself
# global attributes: predefined locations
# methods: draw the ball, move the ball randomly


Shells
# attributes: location, color, shell itself
# global attribute: predefined locations


-- All Six Ball Locations --
BALL_LOCATIONS = [
    Point(150, 150),
    Point(300, 150),
    Point(450, 150),
        
    Point(150, 300),
    Point(300, 300),
    Point(450, 300),

    Point(300, 450),
    Point(150, 450),
    Point(450, 450),
    ]

'''


from time import sleep
from tkinter import getint
from tkinter.constants import CURRENT

from graphics import *
import random

color_list = [
    'lime',
    'aqua',
    'fuchsia'
]



class Ball():
    ''' Creates a ball object '''

    # Ball Locations
    BALL_LOCATIONS = (
    Point(150, 300),
    Point(300, 300),
    Point(450, 300),
    )

    def __init__(self):
        self.__location = Point(300, 300)
        self.__size = 12
        self.__color = 'red'
        self.__ball = Circle(self.__location, self.__size)

    def __str__(self):
        return f'\n-- Ball Information --\nLocation: {self.__location}\nBall drawn: {self.__ball}\n-- End Information --\n'

    def drawBall(self, win):
        ''' Draws the ball. This also updates the location '''

        self.__ball.setFill(self.__color)
        self.__ball.draw(win)
    
    def moveBall(self, dx:int = 150, dy:int = 0):

        if dx == 150:
            for i in range(15):
                self.__ball.move(10, 0)
                time.sleep(.01)
        elif dx == -150:
            for i in range(15):
                self.__ball.move(-10, 0)
                time.sleep(.01)
        elif dx == 300:
            for i in range(15):
                self.__ball.move(20, 0)
                time.sleep(.01)
        elif dx == -300:
            for i in range(15):
                self.__ball.move(-20, 0)
                time.sleep(.01)


    def shuffleBall(self, win:GraphWin):
        ''' Moves the ball randomly'''
        ball_locations = Ball.BALL_LOCATIONS # just makes it easier to read

        print()
        currentPoint = self.__location # get current point with x and y values
        print('current point: ', currentPoint)
        currentPoint_x = currentPoint.getX()
        currentPoint_y = currentPoint.getY()

        randomPoint = ball_locations[random.randrange(0, len(ball_locations))] # get a random point within the range of our list with x and y values
        randomPoint_x = randomPoint.getX()
        randomPoint_y = randomPoint.getY()

        while currentPoint_x == randomPoint_x and currentPoint_y == randomPoint_y: # check that the point isn't the same as the current point
            randomPoint = ball_locations[random.randrange(0, len(ball_locations))]
            randomPoint_x = randomPoint.getX()
            randomPoint_y = randomPoint.getY()
        print('random point: ',randomPoint)

        if currentPoint_x > randomPoint_x: # check which way we are moving the ball
            dx = (currentPoint_x - randomPoint_x) * -1 # if the current point x is bigger than assume it towards the right of the screen. which means we need to go left
        elif currentPoint_x < randomPoint_x:
            dx = randomPoint_x - currentPoint_x  # if the current point x is smaller than vice versa.
        else:
            dx = 0

        print('change: ', dx)
        self.moveBall(dx) # move the ball
        self.setBallLocation(randomPoint) # keep track of the ball's location
        
    
    def hideBall(self):
        ''' Hides the ball by undrawing. I'm assuming this will be useful when we shuffle around the shells'''
        self.__ball.undraw()
    
    def setBallLocation(self, location):
        self.__location = location

    
    def getLocation(self):
        return self.__location
    
    def getBall(self):
        return self.__ball

class Shell():
    SHELL_LOCATIONS = (
        Point(150, 300),
        Point(300, 300),
        Point(450, 300),
    )

    SHELL_SPEED = {
        'easy' : .05,
        'medium' : .03,
        'hard' : .01 
    }

    def __init__(self, shellCenter : Point = SHELL_LOCATIONS[1], color : str = 'yellow'):
        self.__location = shellCenter
        self.__color = color
        self.__shell = Arc(Point(shellCenter.getX() - 50, shellCenter.getY() - 25), Point(shellCenter.getX() + 50, shellCenter.getY() + 75), 0 , 180)
        self.__hidingBallStatus = False
    
    def __str__(self):
        return f'\nShell Location: {self.__location}\nShell Color: {self.__color}'
    
    def drawShell(self, win: GraphWin):
        self.__shell.setFill(self.__color)
        self.__shell.draw(win)

    def getLocation(self):
        return self.__location

    def setLocation (self, location: Point):
        self.__location = location
    
    def getColor(self):
        return self.__color

    def getShell(self):
        return self.__shell
    
    def getColor(self):
        return self.__color


    def moveShell(self, dx:int = 150, dy:int=0, speed = .01):
        
        if dx == 150:
            for i in range(15):
                self.__shell.move(10, 0)
                time.sleep(speed)
        elif dx == -150:
            for i in range(15):
                self.__shell.move(-10, 0)
                time.sleep(speed)
        elif dx == 300:
            for i in range(15):
                self.__shell.move(20, 0)
                time.sleep(speed)
        elif dx == -300:
            for i in range(15):
                self.__shell.move(-20, 0)
                time.sleep(speed)
        

    @staticmethod
    def shuffle_shells(shell_list : list):
        ''' Shuffles shells at random'''

        randomNumbersList = [] # create random number list to keep track of random shell selection
        while len(randomNumbersList) < 2: # loop checking length of list
            randomNumber = random.randint(0, len(shell_list) - 1 ) # random number 
            if randomNumber not in randomNumbersList: # if the # is not in the list append
                randomNumbersList.append(randomNumber)
        
        shell1 = shell_list[randomNumbersList[0]]
        shell2 = shell_list[randomNumbersList[1]]

        shell1_location = shell1.getLocation()
        shell2_location = shell2.getLocation()

        shell1_x = shell1.__location.getX() # get x location of both shells
        shell2_x = shell2.__location.getX()

        if shell1_x > shell2_x: # test which x location is greater and subtract the greater from the lower value
            dx = shell1_x - shell2_x

            shell2.moveShell(dx, 0) # move shell according to which is bigger
            shell1.moveShell(dx * -1, 0)

        elif shell1_x < shell2_x:
            dx = shell2_x - shell1_x

            shell1.moveShell(dx, 0)
            shell2.moveShell(dx * -1, 0)

        else:
            dx = 0

        shell1.setLocation(shell2_location)
        shell2.setLocation(shell1_location)

    def sethidingBallStatus(self, booleanValue:bool):
        self.__hidingBallStatus = booleanValue

    def getHidingBallStatus(self):
        return self.__hidingBallStatus

def intoMessage():
    title = Text(Point(300, 75), 'Shell Game!')
    title.setSize(36)
    title.setStyle('bold italic')
    

    toStart_text = Text(Point(300, 150), 'Click to start!')
    toStart_text.setSize(18)
    toStart_text.setStyle('bold italic')

    toSeeShells_text = Text(Point(300, 150), 'Click to hide the ball.')
    toSeeShells_text.setSize(18)
    toSeeShells_text.setStyle('bold italic')

    toShuffle_text = Text(Point(300, 150), 'Click to shuffle!')
    toShuffle_text.setSize(18)
    toShuffle_text.setStyle('bold italic')

    ballQuestion = Text(Point(300, 150), "Where's the ball?")
    ballQuestion.setSize(18)
    ballQuestion.setStyle('bold italic')

    win_text = Text(Point(300, 150), "You Win!")
    win_text.setSize(18)
    win_text.setStyle('bold italic')

    lose_text = Text(Point(300, 150), "You're not good at this.")
    lose_text.setSize(18)
    lose_text.setStyle('bold italic')

    diffculty = Text(Point(300, 150), "Choose a difficult setting ('Easy', 'Medium', 'Hard')")
    diffculty.setSize(18)
    diffculty.setStyle('bold italic')

    messages = {
        'title' : title,
        'toStart' : toStart_text,
        'toSeeShells' : toSeeShells_text,
        'toShuffle' : toShuffle_text,
        'ballQuestion' : ballQuestion,
        'diffculty' : diffculty,
        'win' : win_text,
        'lose' : lose_text
    }

    return messages
    


def main():
    win = GraphWin('Shell Game', 600, 600) # window for the shell game
    Line(Point(150, 0), Point(150, 600)).draw(win)
    Line(Point(300, 0), Point(300, 600)).draw(win)
    Line(Point(450, 0), Point(450, 600)).draw(win)
    Line(Point(600, 0), Point(600, 600)).draw(win)

    Line(Point(0, 150), Point(600, 150)).draw(win)
    Line(Point(0, 300), Point(600, 300)).draw(win)
    Line(Point(0, 450), Point(600, 450)).draw(win)
    Line(Point(0, 600), Point(600, 600)).draw(win)


    ### start of the final project ###
    messages_dict = intoMessage()

    messages_dict['title'].draw(win)
    messages_dict['toStart'].draw(win)

    ball = Ball()
    ball.drawBall(win)

    while win.checkMouse() == None:
        ball.shuffleBall(win)
    
    messages_dict['title'].undraw()
    messages_dict['toStart'].undraw()
    messages_dict['toSeeShells'].draw(win)

    win.getMouse()
    messages_dict['toSeeShells'].undraw()

    shell_list = []
    winning_shell = None
    for i in range(0, 3):
        shell = Shell(Shell.SHELL_LOCATIONS[i], color_list[i])
        shell.drawShell(win)
        if ball.getBall().testCollision_CircleVsRectangle(shell.getShell()):
            shell.sethidingBallStatus(True)
            winning_shell = shell
            print(f"{shell.getColor()} has the ball")
        shell_list.append(shell)
    ball.getBall().undraw()
    messages_dict['toShuffle'].draw(win)
    win.getMouse()
    messages_dict['toShuffle'].undraw()



    for i in range(12):
        Shell.shuffle_shells(shell_list)

    messages_dict['ballQuestion'].draw(win)
    click = win.getMouse()
    messages_dict['ballQuestion'].undraw()

    r = Rectangle(winning_shell.getShell().getP1(), winning_shell.getShell().getP2())
    if Rectangle.testCollision_RectVsPoint(r, click):
        messages_dict['win'].draw(win)
    else:
        messages_dict['lose'].draw(win)
    
    win.getMouse()

main()

    