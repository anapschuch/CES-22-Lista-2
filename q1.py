# Queremos verficar como 'turtle' funciona.
# Quando as teclas + e - são pressionadas, o 'pensize'
# aumenta ou diminui. Se as teclas R, G e B são pressionadas,
# a cor da caneta muda para vermelho, verde e azul,
# respectivamente. Se as teclas direita e esquerda são
# pressionadas, a 'turtle' rotaciona 90 graus em cada direção.
# Se a barra de espaço é pressionada ela move 10 unidades
# em frente.


import turtle

wn = turtle.Screen()
wn.title("q1 - Lista 2 Python")

wn.bgcolor("lightgreen")
tess = turtle.Turtle()

tess.pensize(3)
tess.pencolor("green")


def change_blue():
    tess.pencolor("blue")


def change_red():
    tess.pencolor("red")


def change_green():
    tess.pencolor("green")


def increase_pen():
    if tess.pensize() < 20:
        tess.pensize(tess.pensize() + 1)


def decrease_pen():
    if tess.pensize() > 1:
        tess.pensize(tess.pensize() - 1)


def rotate_rigth():
    tess.right(90)


def rotate_left():
    tess.left(90)


def move():
    tess.forward(10)


# Bind event handlers to keys
wn.onkey(change_blue, "b")
wn.onkey(change_red, "r")
wn.onkey(change_green, "g")
wn.onkey(increase_pen, "plus")
wn.onkey(decrease_pen, "minus")
wn.onkey(rotate_left, 'Left')
wn.onkey(rotate_rigth, 'Right')
wn.onkey(move, 'space')

wn.listen()  # Listen for events
wn.mainloop()
