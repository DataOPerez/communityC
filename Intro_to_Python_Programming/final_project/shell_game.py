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
        self.__location = Shell.SHELL_LOCATIONS.index(shellCenter)
        self.__color = color
        self.__shell = Arc(Point(shellCenter.getX() - 50, shellCenter.getY() - 25), Point(shellCenter.getX() + 50, shellCenter.getY() + 75), 0 , 180) #Arc(Point(250, 275), Point(350, 375), 0, 180)
    
    def __str__(self):
        return f'Shell Location: {self.__location} Shell Color: {self.__color}'
    
    def drawShell(self, win: GraphWin):
        self.__shell.setFill(self.__color)
        self.__shell.draw(win)

    def moveShell(self, win:GraphWin):
        for i in range(12):
            self.__shell.move(6, -6)
            update(30)
            
        for i in range(12):
            self.__shell.move(6, 6)
            update(30)

    def moveShell_V2(self, dx_multipler = 1, dy_multipler = 1):
        ONE_DISTANCE = 150

        if dx_multipler > dy_multipler:
            for i in range(dx_multipler * ONE_DISTANCE):
                self.__shell.move()


    @staticmethod
    def shuffleShells(shell1, shell2):
        ''' I need to figure out how to switch the shell positions'''
        s1x = shell1.__shell.getCenter().getX()
        s1y = shell1.__shell.getCenter().getY()

        s2x = shell2.__shell.getCenter().getX()
        s2y = shell2.__shell.getCenter().getY()


        print("shell1 ", s1x, s1y)
        print("shell2 ",s2x, s2y)

        if s2x > s1x:
            dx = s2x - s1x
        elif s2x < s1x:
            dx = (s1x - s2x) * -1
        else:
            dx = 0
        

        if s2y > s1y:
            dy = s2y - s1y
        elif s2y < s1y:
            dy = (s1y - s2y) * -1
        else:
            dy = 0

        print('direction change in x: ', dx)
        print('direction change in y: ', dy)

        if dx > 0:
            for i in range(int(abs(dx))):
                shell1.__shell.move(1, 0)
                shell2.__shell.move(1 * -1, 0 * -1)
        else:
            for i in range(int(abs(dx))):
                shell2.__shell.move(1, 0)
                shell1.__shell.move(1 * -1, 0 * -1)



    


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

    # for i in range(6):
    #     ball.moveBallRandomly()
    # input('ball moved')

    # shell_list = []
    # for i in range(0, 3):
    #     shell = Shell(Shell.SHELL_LOCATIONS[i], color_list[i])
    #     shell.drawShell(win)
    #     print(shell)
    #     shell_list.append(shell)

    shell  = Shell(Shell.SHELL_LOCATIONS[0], 'aqua')
    shell2 = Shell(Shell.SHELL_LOCATIONS[1], 'pink')
    shell.drawShell(win)
    shell2.drawShell(win)
    win.getMouse()
    Shell.shuffleShells(shell, shell2)
    win.getMouse()




    



main()

    