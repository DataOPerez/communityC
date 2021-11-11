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
        ''' Set attributes, I believe I want the attributed handled by methods'''
        self.__location = 1
        self.__size = 12
        self.__color = 'red'

        self.__ball = Circle(Ball.BALL_LOCATIONS[1], self.__size)

    def __str__(self):
        return f'\n-- Ball Information --\nLocation: {self.__location}\nBall drawn: {self.__ball}\n-- End Information --\n'

    def drawBall(self, win):
        ''' Draws the ball. This also updates the location '''

        self.__ball.setFill(self.__color)
        self.__ball.draw(win)

    def moveBallRandomly(self):
        ''' Moves the ball randomly'''
        randomPoint = Ball.BALL_LOCATIONS[random.randrange(0, len(Ball.BALL_LOCATIONS))] # get random point from ball location list
        randX, randY = randomPoint.getX(), randomPoint.getY() # get that x and  coordinate from that random point
        currentX, currentY = self.__ball.getCenter().getX(), self.__ball.getCenter().getY()  # get the circles center point x and y coordinate
        
        # check if dx and dy should be positive or negative
        # text x
        if randX > currentX: #if randomX coordiante is greater than currentX then dx should be positive and move the difference
            dx = randX - currentX 
        elif randX < currentX: # if randomX coordiante is less than currentX then  dx should be negative and move the difference
            dx = (currentX - randX) * -1
        else:
            dx = 0
        
        # test y (same rules apply as x)
        if randY > currentY:
            dy = randY - currentY
        elif randY < currentY:
            dy = (currentY - randY) * -1
        else:
            dy = 0

        # uncomment these if need to check status about points
        # print("random point", randomPoint)
        # print("currentX: ", currentX, "currentY: ", currentY)
        # print("dx: ", dx, "dy: ", dy)
        
        self.__ball.move(dx, dy)
        time.sleep(.2)
    
    def hideBall(self):
        ''' Hides the ball by undrawing. I'm assuming this will be useful when we shuffle around the shells'''
        self.__ball.undraw()



class Shell():
    SHELL_LOCATIONS = (
            
        Point(150, 300),
        Point(300, 300),
        Point(450, 300),
    )

    def __init__(self, shellCenter : Point = SHELL_LOCATIONS[1], color : str = 'yellow'):
        self.__location = shellCenter
        self.__color = color
        self.__shell = Arc(Point(shellCenter.getX() - 50, shellCenter.getY() - 25), Point(shellCenter.getX() + 50, shellCenter.getY() + 75), 0 , 180)
    
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

    def moveShell(self, dx:int = 150, dy:int=0):
        
        if dx == 150:
            for i in range(15):
                self.__shell.move(10, 0)
                time.sleep(.01)
        elif dx == -150:
            for i in range(15):
                self.__shell.move(-10, 0)
                time.sleep(.01)
        elif dx == 300:
            for i in range(15):
                self.__shell.move(20, 0)
                time.sleep(.01)
        elif dx == -300:
            for i in range(15):
                self.__shell.move(-20, 0)
                time.sleep(.01)

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
        
        # LOCATION NEED TO SWITCH AND WE NEED TO FIGURE OUT WHY THE POINTS ARE
        # INCREASING BY 25 ON THE Y AXIS

        

    


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

    ball = Ball()
    ball.drawBall(win)

    for i in range(60):
        ball.moveBallRandomly()
    input('ball moved')

    shell_list = []
    for i in range(0, 3):
        shell = Shell(Shell.SHELL_LOCATIONS[i], color_list[i])
        shell.drawShell(win)
        shell_list.append(shell)

    win.getMouse()
    for i in range(60):
        Shell.shuffle_shells(shell_list)
    win.getMouse()





    



main()

    