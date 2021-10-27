from graphics import *

def background(win:GraphWin, backgroundColor, time):
    """Sets the background. Depending on the time time parameter. If day then day if night then night"""
    if time == "Day":
        win.setBackground(backgroundColor)
        sun = Circle(Point(800, 150), 60)
        sun.setFill("Yellow")
        sun.draw(win)
    else:
        win.setBackground(backgroundColor)
        moon = Circle(Point(800, 150), 60)
        moon.setFill("ivory")
        moon.draw(win)


def drawOutline(win:GraphWin):
    """Creates two squares that makes up the house. The back of the house has a pattern. To create the
    pattern I used a for loop."""
    fillColorA = "brown"
    increase = 0
    
    houseBack = Rectangle(Point(150, 75), Point(575, 650))
    houseBack.setOutline("black")
    houseBack.setFill(fillColorA)
    houseBack.draw(win)

    for i in range(23):
        houseBackPattern = Line(Point(150, 75 + increase), Point(575, 75 + increase))
        houseBackPattern.draw(win)
        increase += 25


    houseMain = Rectangle(Point(375, 225), Point(600, 650))
    houseMain.setOutline("black")
    houseMain.setFill(fillColorA)
    houseMain.setWidth(2)
    
    houseMain.draw(win)   

def drawDoor(win:GraphWin):
    """Draws a door with an outline. """
    fillColorA = "skyblue"
    fillColorB = "black"
    door = Rectangle(Point(400, 375), Point(450, 550))
    door.setOutline(fillColorA)
    door.setFill(fillColorA)
    door.draw(win)


    
    doorKnob = Circle(Point(440, 475), 3)
    doorKnob.setFill(fillColorB)
    doorKnob.draw(win)

def drawWindow(win:GraphWin, tlX, tlY, width, height):
    """Draws a window given the top left X and Y coordinate. The user also includes the width and height. Those
    values are added to the top left X and Y coordniates."""
    fillColorA = "azure"
    window = Rectangle(Point(tlX, tlY), Point(tlX + width, tlY + height) )
    window.setFill(fillColorA)
    window.draw(win)

def drawRoof(win:GraphWin):
    """Draws a polygons for the roof. assuming three points."""
    fillColorA = "olivedrab"
    roof = Polygon(Point(75, 100), Point(300, 25), Point(450, 100))
    roof.setFill(fillColorA)
    roof.draw(win)

    roofTwo = Polygon(Point(300, 100), Point(550, 25), Point(625, 100))
    roofTwo.setFill(fillColorA)
    roofTwo.draw(win)

def drawStairs(win:GraphWin, numOfStairs, tlX, tlY, blX, blY):
    """Creates steps in front of the house. On of the parameters is number of states.
    Uses a loop to create stairs based on the parameter."""
    fillColorA = "slateGray"
    increase = 0
    for stair in range(numOfStairs):
        currentStair = Rectangle(Point(tlX - increase, tlY + increase), Point(blX, blY + increase))
        currentStair.setFill(fillColorA)
        currentStair.draw(win)
        increase += 25

def drawPatio(win:GraphWin):
    """Simple rectange to fill the space between the door and the stairs"""
    fillColorA = "orange"
    patio = Rectangle(Point(375, 550), Point(600, 575))
    patio.setFill(fillColorA)
    patio.draw(win)

def drawHouseAccents(win:GraphWin):
    """Draws rectangles to give the house a bit more depth."""
    fillcolorA = "gray"
    topAccent = Rectangle(Point(150, 75), Point(575, 100))
    topAccent.setFill(fillcolorA)
    topAccent.draw(win)

    leftAccent = Rectangle(Point(150, 75), Point(175, 650))
    leftAccent.setFill(fillcolorA)
    leftAccent.draw(win)

    aboveMain = Rectangle(Point(350, 200), Point(575, 225))
    aboveMain.setFill(fillcolorA)
    aboveMain.draw(win)

    leftMain = Rectangle(Point(350, 200), Point(375, 650))
    leftMain.setFill(fillcolorA)
    leftMain.draw(win)


def drawDarkness(win:GraphWin):
    """The image I based this off of had an over hanging flat roof that casted a shadow. This is that shadow"""
    fillColorA = "black"
    darkness = Polygon(Point(575,100), Point(550,175), Point(175,175), Point(175, 100))
    darkness.setFill(fillColorA)
    darkness.draw(win)

def drawBush (win:GraphWin, pointAA, PointAB, PointBA, PointBB,):
    """I'm using a couple of ovals to create bushes. 4 points make the oval. The first defines the box the second defines the oval."""
    bushO = Oval(Point(pointAA, PointAB), Point(PointBA, PointBB))
    bushO.setFill("Green")
    bushO.draw(win)

def drawChimney(win:GraphWin):
    """Two recntagles stacked on top of each other to form a chimney."""
    fillColorA = "darkgoldenrod"
    chimenyBase = Rectangle(Point(350, 25), Point(425, 75))
    chimenyBase.setFill(fillColorA)
    chimenyBase.draw(win)

    chimenyTop = Rectangle(Point(325, 0), Point(450, 25))
    chimenyTop.setFill(fillColorA)
    chimenyTop.draw(win)
    
    
    
def drawFence(win:GraphWin):
    """Using a foor loop to create a white fence. Draws from left to right."""
    fillColorA = "White"
    increase = 0

    for i in range (39):

        fence = Rectangle(Point(0 + increase, 425), Point(50 + increase, 650))
        fence.setFill(fillColorA)
        fence.setWidth(3)
        fence.draw(win)

        fenceTop = Polygon(Point(0 + increase, 425), Point(25 + increase, 400), Point(50 + increase, 425))
        fenceTop.setFill(fillColorA)
        fenceTop.setWidth(3)
        fenceTop.draw(win)
        increase += 25
    


def drawTopRail(win:GraphWin):
    """As mentioned previously the image I based this off of had an over hanging roof with an open concept.
    In order to preventn people from falling there was a rail. This function creates multiple verticle lines with
    a for loop. Then a single line to be the hand rail."""
    fillColorA = "Silver"
    increase = 0

    for i in range(32):
        rail = Line(Point(175 + increase, 125), Point(175 + increase, 175) )
        rail.setFill(fillColorA)
        rail.draw(win)
        increase += 12.5

    topRail = Line(Point(175, 125), Point(575, 125))
    topRail.setFill(fillColorA)
    topRail.draw(win)

def drawMistakes(win:GraphWin, time):
    """In the picture I based this off of the roof would come back on it's self. Exposing the sky.
    This function creates a polygon to fix that mistake denpding if it's day or night mode."""
    if time == "Day" or time == "day":
        rail_house_fix = Polygon(Point(575, 100), Point(550, 175), Point(575, 175))
        rail_house_fix.setFill("skyblue")
        rail_house_fix.setOutline("skyblue")
        rail_house_fix.draw(win)
    elif time == "Night" or time == "night":
        rail_house_fix = Polygon(Point(575, 100), Point(550, 175), Point(575, 175))
        rail_house_fix.setFill("darkslateblue")
        rail_house_fix.setOutline("darkslateblue")
        rail_house_fix.draw(win)
    

def askTime(win:GraphWin):
    """Ask the user for input if day or night. This function calls the background function and
    pass the correct parameters to make everything function It returns time to help run the drawMistake function later on."""
    time = input("Is it Day or Night time? [Day/Night]")
    if time == "Day" or time == "day":
        background(win, "skyblue", time)
        return time
    elif time == "Night" or time == "night":
        background(win, "darkslateblue", time) 
        return time

def drawBall(win:GraphWin):
    "draws a simple circle to represent a ball. returns the ball to be used in a function."
    ball = Circle(Point(825, 626), 24)
    ball.setFill("Red")
    ball.draw(win)
    return ball

def moveBall(win:GraphWin, object):
    """Moves the ball, Takes an object as a parameter. Uses a for statement to check if the ball is going
    up or down to switch to the opposite movement."""
    up = 25
    for i in range(100):
        if up == 25:
            up = -25
        else:
            up = 25

        object.move(-25, up)
        update(30)

def drawImage(win:GraphWin):
    """adding an image to the window"""
    image = Image(Point(525, 450), '/Users/tech/Documents/gitLocal/cis2531/Week 4/pythonGraphics-master/skull.png')
    image.transform(scale=.25)
    image.draw(win)

    

#MAIN PROGRAM BELOW
def main():
    """'The console will ask you right away to input if it is Day or Night. Day or Night will change the scene.
    
    After the user enters the Day or Night they can click the screen to make the ball move."""
    win = GraphWin("House Drawing", 1000, 650, autoflush= False)

    time = askTime(win)
    drawFence(win)

    drawOutline(win)
    drawDoor(win)

    drawWindow(win, 200, 250, 50, 125) #top left window
    drawWindow(win, 200, 400, 125, 125) #bottom left window
    drawWindow(win, 400, 225, 175, 100) #top right window

    

    drawStairs(win, 3, 375, 575, 500, 600)
    drawPatio(win)

    drawDarkness(win)
    drawHouseAccents(win)

    drawChimney(win)
    drawRoof(win)

    drawBush(win, 100, 575, 350, 650)
    drawBush(win, 300, 500, 375, 650)
    drawBush(win, 475, 550, 600, 650)
    drawBush(win, 575, 450, 635, 650)
    

    drawTopRail(win)
    drawMistakes(win, time)

    drawImage(win)

    redBall = drawBall(win)
    print("Click to move the ball.")
    clicked = win.getMouse()
    if clicked != None:
        moveBall(win, redBall)
    
    win.getMouse()
    win.close()
    
    

if __name__ == '__main__':
    main()
