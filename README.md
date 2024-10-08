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



Nombre: José Antonio López Saldaña
Matrícula: A01710367


Commit Inicial/Crear repositorio - Hice la creacion de un repositorio nuevo, comparti el repositorio con mi compañero de equipo y creé una rama nueva (Develop_A01710367)

Commit/Copiar Pacman - Descargue el codigo de pacman.py con un codigo de una libreria, y lo agregue al repo

Commit/Modificar Tablero - Hice las modificaciones pertinentes para que pudiera jugar con los muros y el fondo del mapa, en el cual se encontraba como una matriz, modificando de esta forma el tablero de juego de Pacman

Commit/Modificar Velocidad - Hice un cambio dentro de la funcion ontimer, en la cual encontre que reduciendo la variable disminuia la velocidad de todos los personajes del juego

Commit/Comentarios y Cambio de Variables a Español - Le puse comentarios de acuerdo a un estandar, ademas de hacerlos en español para que todo tuviera una coherencia, asi como el mismo cambio en las variables.

Commit/Correcion PEP8 - Hice los cambios que me pedia al correr el PEP-8, hasta que mi codigo siguiera el estandar establecido por este mismo

Commit/Actualizar README - Para explcar de una forma adecuada los cambios realizados en la rama hago una descripcion de estos mismos

Despues un merge de la rama que trabaje hacia la main.

Finalmente verifique en Github
