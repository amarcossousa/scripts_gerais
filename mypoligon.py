import turtle
import math

bob = turtle.Turtle()
# #print(bob)
# bob.fd(100)
# bob.lt(90)
# bob.fd(100)
# bob.lt(90)
# bob.fd(100)
# bob.lt(90)
# bob.fd(100)

# for i in range(4):
#     bob.fd(100)
#     bob.lt(90)

# def square(t, length ):
#     for i in range(4):
#         t.fd(length)
#         t.lt(90)
        
# square(bob, 150)


# def poligon(t, length, n):
#     angle = 360/n
#     for i in range(n):
#         t.fd(length)
#         t.lt(angle)


# def circle(t, r):
#     circuference = 2 * math.pi
#     for i in range(r):
#         t.fd(5)
#         t.lt(circuference)

# circle()
    
# #poligon(bob, 100, 5)
# turtle.mainloop()

""""Codigos do livro
    modelos para circle
"""

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, n, lengh):
    angle = 360/n
    polyline(t, n, lengh, angle)

# polygon(bob, 7, 70)

def circle(t, r):
    arc(t, r, 360)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

    # for i in range(n):
    #     t.fd(step_length)
    #     t.lt(step_angle)
arc(bob, 100, 180)

turtle.mainloop()


