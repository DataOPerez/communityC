import warnings
from graphics import *
from Ball import *
from Shell import *

def mainText():
    title = Text(Point(300, 50), 'Shell Game')
    title.setStyle('bold italic')
    title.setSize(36)

    subTitle = Text(Point(300, 100), 'Complete the settings menu before starting!')
    subTitle.setStyle('italic')
    subTitle.setSize(24)
    

    mainMenu_dict = {
        'title' : title,
        'subTitle' : subTitle

    }

    return mainMenu_dict

def settingsMenuText():

    ballSpeed = Text(Point(150, 50), "Enter ball speed ('Slow', 'Medium', 'Fast'):")
    ballSpeed.setStyle('bold')
    ballSpeed.setSize(12)

    ballSpeedInput = Entry(Point(150, 100), 30)
    ballSpeedInput.setStyle('bold')
    ballSpeedInput.setSize(12)

    
    numOfShells = Text(Point(150, 150), "Enter the number of shells (1-9):")
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

    blankError = Text(Point(150, 25), 'Error, one or more fields blank')
    blankError.setStyle('bold')
    blankError.setFill('red')
    blankError.setSize(12)
    

    
    settingsMenu_dict = {
        'ballSpeed' : ballSpeed,
        'ballSpeedInput' : ballSpeedInput,
        'numOfShells' : numOfShells,
        'numOfShellsInput' : numOfShellsInput,
        'submitButton' : submitButton,
        'submitButtonText' : submitButtonText,
        'blankError' : blankError

    }

    return settingsMenu_dict

def settingsMenu(settingsMenu_dict, settingsWin):
     # settins menu
    settingsMenu_dict['ballSpeed'].draw(settingsWin)
    settingsMenu_dict['ballSpeedInput'].draw(settingsWin)

    settingsMenu_dict['numOfShells'].draw(settingsWin)
    settingsMenu_dict['numOfShellsInput'].draw(settingsWin)

    #settingsMenu_dict['submitButton'].draw(settingsWin)
    settingsMenu_dict['submitButtonText'].draw(settingsWin)

    # get the values
    ballSpeed = settingsMenu_dict['ballSpeedInput'].getText()
    numOfShells = settingsMenu_dict['numOfShellsInput'].getText()




def main(win):
    ball_speed = [
        'easy',
        'medium',
        'fast'
    ]

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
    settingsMenu_dict['ballSpeed'].draw(settingsWin)
    settingsMenu_dict['ballSpeedInput'].draw(settingsWin)

    settingsMenu_dict['numOfShells'].draw(settingsWin)
    settingsMenu_dict['numOfShellsInput'].draw(settingsWin)

    #settingsMenu_dict['submitButton'].draw(settingsWin)
    settingsMenu_dict['submitButtonText'].draw(settingsWin)



    key = settingsWin.getKey()
    while key.lower() != 'return':
        key = settingsWin.getKey()

    # get the values
    ballSpeed = settingsMenu_dict['ballSpeedInput'].getText()
    numOfShells = settingsMenu_dict['numOfShellsInput'].getText()
    settingsWin.close()




if __name__ == '__main__':
    main()