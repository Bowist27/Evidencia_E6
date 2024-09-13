# Tic-Tac-Toe Game - Jorge Nieto A01711060

This is a simple Tic-Tac-Toe game built using the Python `turtle` graphics library. 
The starting program can be downloaded using the freegames module or this link https://grantjenks.com/docs/freegames/tictactoe.html.
Players take turns clicking on the grid to place either an X (in red) or an O (in blue). The game includes features to validate whether a cell is already occupied before making a move.

## Features

- Tic-Tac-Toe grid drawn using turtle graphics.
- X and O symbols have different colors (red for X and blue for O).
- X and O symbols have customizable widths.
- The game prevents a player from placing a symbol in an already occupied cell.

## Process to solve the challenge
1. Initial Commit - '**Add tic-tac-toe.py**'
Uploaded the base Tic-Tac-Toe game to my branch to initiate version control.

2. Fix F403 Error - '**Fix F403 error by refactoring turtle star import**'
Resolved the F403 error by modifying the turtle import. The issue was caused by importing everything using a wildcard (*), which was addressed using flake8 to ensure better code quality.

3. Symbol Modifications - '**Modify size, color, and centering of X and O symbols**'
Updated the drawx() and drawo() functions to adjust the size of the X and O symbols. Also added pencolor() and pensize() to change the colors and increase the line width for both symbols.

4. Cell Validation - '**Validate if a cell is already occupied in Tic-Tac-Toe**'
Implemented functionality to check if a cell is already occupied. If a player tries to place a symbol in an occupied cell, the terminal will display "Cell already occupied!" and the move will be ignored.

5. PEP8 Compliance - '**Validate PEP8 compliance using flake8**'
Refactored the code to meet PEP8 standards by using flake8 for style checking, ensuring the code is clean and follows Python's best practices.

6. README Update - '**Update README with game description, features, and preview of game**'
Enhanced the README with a game description, features list, and a preview image of the Tic-Tac-Toe game.


## Preview of the game

![tictactoe](https://github.com/user-attachments/assets/8e6c6df9-943c-4835-8b78-57f5ba6f49e0)
