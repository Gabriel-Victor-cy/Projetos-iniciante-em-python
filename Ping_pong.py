import turtle

window = turtle.Screen()
window.title("Ping pong by G.Victor")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# barra_A

barra_A = turtle.Turtle()
barra_A.speed(0)
barra_A.shape("square")
barra_A.color("White")
barra_A.shapesize(stretch_wid=5, stretch_len=1)
barra_A.penup()
barra_A.goto(-350, 0)

# barra_B

barra_B = turtle.Turtle()
barra_B.speed(0)
barra_B.shape("square")
barra_B.color("White")
barra_B.shapesize(stretch_wid=5, stretch_len=1)
barra_B.penup()
barra_B.goto(350, 0)

# Ball
bola = turtle.Turtle()
bola.speed(0)
bola.shape("square")
bola.color("White")
bola.penup()
bola.goto(0, 0)
bola.dx = 1
bola.dy = -1



# Movimentação
def barra_A_up():
    y = barra_A.ycor()
    y += 20
    barra_A.sety(y)


def barra_A_down():
    y = barra_A.ycor()
    y -= 20
    barra_A.sety(y)


def barra_B_up():
    y = barra_B.ycor()
    y += 20
    barra_B.sety(y)


def barra_B_down():
    y = barra_B.ycor()
    y -= 20
    barra_B.sety(y)


# Teclado
window.listen()
window.onkeypress(barra_A_up, "w")
window.onkeypress(barra_A_down, "s")
window.onkeypress(barra_B_up, "Up")
window.onkeypress(barra_B_down, "Down")


# Main game loop
while True:
    window.update()

    # movimento da bola
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)

    # Borda
    if bola.ycor() > 290:
        bola.sety(290)
        bola.dy *= -1

    if bola.ycor() < -290:
        bola.sety(-290)
        bola.dy *= -1

    if bola.xcor() > 390:
        bola.goto(0, 0)
        bola.dx *= -1

    if bola.xcor() < -390:
        bola.goto(0, 0)
        bola.dx *= -1

    # colisão
    if bola.xcor() < -340 and bola.ycor() < barra_A.ycor() + 40 and bola.ycor() > barra_A.ycor() - 40:
        bola.setx(-340)
        bola.dx *= -1

    if bola.xcor() > 340 and bola.ycor() < barra_B.ycor() + 40 and bola.ycor() > barra_B.ycor() - 40:
        bola.setx(340)
        bola.dx *= -1



turtle.done()
