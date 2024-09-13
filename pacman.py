from random import choice
from turtle import Turtle, bgcolor, clear, goto, dot, up, setup
from turtle import hideturtle, update, ontimer, tracer, listen, onkey, done

from freegames import floor, vector

"""Puntuacion y configuraciones"""
estado = {'score': 0}
camino = Turtle(visible=False)
writer = Turtle(visible=False)

"""Salida del Pacman"""
salida = vector(5, 0)
pacman = vector(-40, -80)

"""Lista de los 4 Fantasmas"""
fantasmas = [
    [vector(-180, 160), vector(5, 0)],
    [vector(-180, -160), vector(0, 5)],
    [vector(100, 160), vector(0, -5)],
    [vector(100, -160), vector(-5, 0)],
]

"""Tablero del juego (0 son los pared, 1 el camino libre)"""

pared = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]


"""Dibuja el cuadrado usando (x,y)"""


def cuadrado(x, y):
    camino.up()
    camino.goto(x, y)
    camino.down()
    camino.begin_fill()

    for count in range(4):
        camino.forward(20)
        camino.left(90)

    camino.end_fill()


"""Conversion de coordenadas a tablero"""


def conversion(punto):
    x = (floor(punto.x, 20) + 200) / 20
    y = (180 - floor(punto.y, 20)) / 20
    indice = int(x + y * 20)
    return indice


"""Verifica si es valido el punto de moverse"""


def valido(punto):
    indice = conversion(punto)

    if pared[indice] == 0:
        return False

    indice = conversion(punto + 19)

    if pared[indice] == 0:
        return False

    return punto.x % 20 == 0 or punto.y % 20 == 0


"""Dibuja el mundo con las paredes cargadas"""


def mundo():
    bgcolor('black')
    camino.color('blue')

    for indice in range(len(pared)):
        muro = pared[indice]

        if muro > 0:
            x = (indice % 20) * 20 - 200
            y = 180 - (indice // 20) * 20
            cuadrado(x, y)

            if muro == 1:
                camino.up()
                camino.goto(x + 10, y + 10)
                camino.dot(2, 'white')


""" Mueve los Pacman y Fantasmas"""


def move():
    writer.undo()
    writer.write(estado['score'])

    clear()

    if valido(pacman + salida):
        pacman.move(salida)

    indice = conversion(pacman)

    if pared[indice] == 1:
        pared[indice] = 2
        estado['score'] += 1
        x = (indice % 20) * 20 - 200
        y = 180 - (indice // 20) * 20
        cuadrado(x, y)

    up()
    goto(pacman.x + 10, pacman.y + 10)
    dot(20, 'yellow')

    for punto, course in fantasmas:
        if valido(punto + course):
            punto.move(course)
        else:
            options = [
                vector(5, 0),
                vector(-5, 0),
                vector(0, 5),
                vector(0, -5),
            ]
            plan = choice(options)
            course.x = plan.x
            course.y = plan.y

        up()
        goto(punto.x + 10, punto.y + 10)
        dot(20, 'red')

    update()

    for punto, course in fantasmas:
        if abs(pacman - punto) < 20:
            return

    """Cambia la velocidad de fantasmas y Pacman"""

    ontimer(move, 10)


"""Cambia personajes en (x,y)"""


def cambio(x, y):
    if valido(pacman + vector(x, y)):
        salida.x = x
        salida.y = y


"""Tamaño de pantalla"""


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
writer.goto(160, 160)
writer.color('white')
writer.write(estado['score'])
listen()
"""Control de pacman"""

onkey(lambda: cambio(5, 0), 'Right')
onkey(lambda: cambio(-5, 0), 'Left')
onkey(lambda: cambio(0, 5), 'Up')
onkey(lambda: cambio(0, -5), 'Down')
mundo()
move()
done()
