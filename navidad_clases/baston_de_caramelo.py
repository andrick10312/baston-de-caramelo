import turtle


def draw_cane(t, x, y, radius, height, stripe_width):
    # dibujar parte curvada del baston
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.pencolor("red")
    t.width(stripe_width)
    t.seth(90)
    for _ in range(90): #arco de 90 grados
       t.forward(radius * 3.1416 / 180) #longitud del arco
       t.right(2)


    #dibujar la parte recta del baston
    t.setheading(-90)
    for _ in range(height):
        t.forward(1)
        t.penup()
        t.forward(stripe_width)
        t.pendown()


 #configuracion inicial
screen = turtle.Screen()
screen.bgcolor("sky blue")
screen.title("Bastón de Caramelo Navideño")
t = turtle.Turtle()
t.speed(0)
t.hideturtle()


#dibujar el baston
draw_cane(t, 0, 100, 50, 150, 10)

#mostrar resultado
turtle.done()

