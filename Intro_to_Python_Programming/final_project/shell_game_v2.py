from graphics import *
from Ball import *
from Shell import *
import dialogue

POSITIONS_LIST = [
    Point(150, 300),
    Point(300, 300),
    Point(450, 300)
]

POSITIONS_LIST_WITH_Y = [
    Point(150, 150),
    Point(300, 150),
    Point(450, 150),

    Point(150, 300),
    Point(300, 300),
    Point(450, 300),

    Point(150, 450),
    Point(300, 450),
    Point(450, 450)
]

SHELL_COLOR_LIST = [
    'blue',
    'green',
    'orange',
    'purple',
    'brown',
    'pink',
    'black',
    'gray',
    'red'

]

def mainText():
    title = Text(Point(300, 50), 'Shell Game')
    title.setStyle('bold italic')
    title.setSize(36)

    subTitle = Text(Point(300, 100), 'Complete the settings menu before starting!')
    subTitle.setStyle('italic')
    subTitle.setSize(24)

    clickToContinue = Text(Point(300, 100), 'Click to continue!')
    clickToContinue.setStyle('italic')
    clickToContinue.setSize(24)

    clickToHideBall = Text(Point(300, 100), 'Click to hide the ball')
    clickToHideBall.setStyle('italic')
    clickToHideBall.setSize(24)

    clickToShuffle = Text(Point(300, 100), 'Click to shuffle the shells')
    clickToShuffle.setStyle('italic')
    clickToShuffle.setSize(24)

    whichShellHasTheBall = Text(Point(300, 100), 'Which shell has the ball?')
    whichShellHasTheBall.setStyle('italic')
    whichShellHasTheBall.setSize(24)

    winner = Text(Point(300, 100), 'You won!')
    winner.setStyle('italic')
    winner.setSize(24)

    loser = Text(Point(300, 100), 'You lose!')
    loser.setStyle('italic')
    loser.setSize(24)
    

    mainMenu_dict = {
        'title' : title,
        'subTitle' : subTitle,
        'clickToContinue' : clickToContinue,
        'clickToHideBall' : clickToHideBall,
        'clickToShuffle' : clickToShuffle,
        'whichShellHasTheBall' : whichShellHasTheBall,
        'winner' : winner,
        'loser' : loser
    }

    return mainMenu_dict

def settingsMenuText():

    shellSpeed = Text(Point(150, 50), "Enter shell speed ('Slow', 'Medium', 'Fast'):")
    shellSpeed.setStyle('bold')
    shellSpeed.setSize(12)

    shellSpeedInput = Entry(Point(150, 100), 30)
    shellSpeedInput.setStyle('bold')
    shellSpeedInput.setSize(12)

    
    numOfShells = Text(Point(150, 150), "Enter the number of shells (3-9):")
    numOfShells.setStyle('bold')
    numOfShells.setSize(12)

    numOfShellsInput = Entry(Point(150, 200), 30)
    numOfShellsInput.setStyle('bold')
    numOfShellsInput.setSize(12)

    submitButton = Rectangle(Point(100, 250), Point(200, 280))
    submitButton.setFill('lightgreen')

    submitButtonText = Text(Point(150, 266), 'Press Enter')
    submitButtonText.setStyle('bold')
    submitButtonText.setSize(12)
    

    
    settingsMenu_dict = {
        'shellSpeed' : shellSpeed,
        'shellSpeedInput' : shellSpeedInput,
        'numOfShells' : numOfShells,
        'numOfShellsInput' : numOfShellsInput,
        'submitButton' : submitButton,
        'submitButtonText' : submitButtonText,
        

    }

    return settingsMenu_dict




def main():

    win = GraphWin('Final Game', 600, 600)
    
    Line(Point(150, 0), Point(150, 600)).draw(win)
    Line(Point(300, 0), Point(300, 600)).draw(win)
    Line(Point(450, 0), Point(450, 600)).draw(win)
    Line(Point(600, 0), Point(600, 600)).draw(win)

    Line(Point(0, 150), Point(600, 150)).draw(win)
    Line(Point(0, 300), Point(600, 300)).draw(win)
    Line(Point(0, 450), Point(600, 450)).draw(win)
    Line(Point(0, 600), Point(600, 600)).draw(win)

    SHELL_SPEED = {
        'slow' : .10,
        'medium' : .03,
        'fast' : .009
    }

    # Setup the windows
    # win = GraphWin('Testing Text', 600, 600)
    settingsWin = GraphWin('Settings Menu', 300, 300)
    
    # Get all the text
    mainMenu_dict = mainText()
    settingsMenu_dict = settingsMenuText()

    # main game
    mainMenu_dict['title'].draw(win)
    mainMenu_dict['subTitle'].draw(win)

    # settins menu
    settingsMenu_dict['shellSpeed'].draw(settingsWin)
    settingsMenu_dict['shellSpeedInput'].draw(settingsWin)

    settingsMenu_dict['numOfShells'].draw(settingsWin)
    settingsMenu_dict['numOfShellsInput'].draw(settingsWin)

    #settingsMenu_dict['submitButton'].draw(settingsWin)
    settingsMenu_dict['submitButtonText'].draw(settingsWin)



    key = settingsWin.getKey()
    while key.lower() != 'return':
        key = settingsWin.getKey()

    # get the values
    shellSpeed = settingsMenu_dict['shellSpeedInput'].getText()
    numOfShells = settingsMenu_dict['numOfShellsInput'].getText()

    if numOfShells == '':
        numOfShells = 3
    elif int(numOfShells) < 3:
        numOfShells = 3
    elif int(numOfShells) > 9:
        numOfShells = 9
    else:
        numOfShells = int(numOfShells)

    if shellSpeed not in SHELL_SPEED:
        shellSpeed = 'medium'

    settingsWin.close()
    mainMenu_dict['subTitle'].undraw()

    ball = Ball(POSITIONS_LIST_WITH_Y[4])
    ball.drawBall(win)
    mainMenu_dict['clickToContinue'].draw(win)

    while win.checkMouse() == None:
        ball.moveBall(POSITIONS_LIST_WITH_Y[randrange(3, 6)], .001)
    ball.moveBall(POSITIONS_LIST_WITH_Y[0])

    mainMenu_dict['title'].undraw()
    mainMenu_dict['clickToContinue'].undraw()

    mainMenu_dict['clickToHideBall'].draw(win)
    win.getMouse()
    
    shell_list = []
    for i in range(int(numOfShells)):
        #shell = Shell(POSITIONS_LIST_WITH_Y[i],SHELL_COLOR_LIST[i])
        shell = Shell(POSITIONS_LIST_WITH_Y[i])
        shell.drawShell(win)
        shell.checkIfSellHasBall(ball)
        if shell.getWinningShellStatus():
            winning_shell = shell
        shell_list.append(shell)
    
    ball.undrawBall()
    mainMenu_dict['clickToHideBall'].undraw()
    mainMenu_dict['clickToShuffle'].draw(win)
    win.getMouse()
    mainMenu_dict['clickToShuffle'].undraw()

    for i in range(12):
        rand1 = randrange(0, len(shell_list))
        rand2 = randrange(0, len(shell_list))
        while rand1 == rand2:
            rand1 = randrange(0, len(shell_list))
            rand2 = randrange(0, len(shell_list))
        Shell.shuffleTwoShells(shell_list[rand1], shell_list[rand2], SHELL_SPEED[shellSpeed])
    
    mainMenu_dict['whichShellHasTheBall'].draw(win)
    click = win.getMouse()
    mainMenu_dict['whichShellHasTheBall'].undraw()

    rec = Rectangle(Point(winning_shell.getX() - 48, winning_shell.getY() - 36), Point(winning_shell.getX() + 48, winning_shell.getY() + 60))

    if Rectangle.testCollision_RectVsPoint(rec, click):
        mainMenu_dict['winner'].draw(win)
    else:
        mainMenu_dict['loser'].draw(win)
    win.getMouse()
    
    
    
    

if __name__ == '__main__':
    main()