import turtle
kturtle = turtle.Turtle()
# This is a EPIC square

def square():
    for t in range(1, 4):
        kturtle.forward(100)
        kturtle.right(90)

def triangle():
    kturtle.forward(100)
    kturtle.right(120)
    kturtle.forward(100)
    kturtle.right(120)
    kturtle.forward(100)



# square()
# kturtle.forward(200)
# square()
# kturtle.forward(100)
elephant_weight = 3000
ant_weight = 0.1
#if elephant_weight > ant_weight:
#    square()
#    kturtle.forward(100)
#else:
#    kturtle.forward(100)
#for count in range(2):
#    square()
for count in range(4):
    triangle()
input()