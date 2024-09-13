"""Tic Tac Toe

Exercises

1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot?
3. How would you detect when someone has won?
4. How could you create a computer player?
"""

from turtle import (up, goto, down, circle, update, setup, hideturtle,
                    tracer, onscreenclick, done, pencolor, pensize, bye)

from freegames import line


def grid():
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Draw X player."""
    pencolor("red") # Turtle color set to red
    padding = 20 # Padding to change the dimension of the X
    line(x + padding, y + padding, x + 133 - padding, y + 133 - padding)
    line(x + padding, y + 133 - padding, x + 133 - padding, y + padding)


def drawo(x, y):
    """Draw O player."""
    pencolor("blue") # Color turtle ser to blue
    up()
    goto(x + 67, y + 25)  # Location where the turtle will start drawing
    down()
    circle(40) # Draw a circle with radious 40


def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + 200) // 133) * 133 - 200


state = {'player': 0}
players = [drawx, drawo]


def tap(x, y):
    """Draw X or O in tapped square, only if the cell is not already occupied."""
    x = floor(x)
    y = floor(y)

    # Check if the cell is already used
    if (x, y) in cell_state:
        print("Cell already occupied!")  # Notify the player
        return  # Do not draw if the cell is already occupied
    
    player = state['player']
    draw = players[player]
    draw(x, y)
    update()

    # Store the player mark ("X" or "O") in the cell state
    cell_state[(x, y)] = "X" if player == 0 else "O"

    # Switch to other player
    state['player'] = not player


setup(420, 420, 370, 0)
cell_state = {} # Track the state of all cells
pensize(5) # Change the width of all the lines
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
