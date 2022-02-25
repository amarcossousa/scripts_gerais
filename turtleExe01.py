import turtle
import math

# flower = turtle.Turtle()

# def polyline_d(t, n):
#     for i in range(n):
#         t.fd(10)
#         t.lt(10)
    
        

# def polyline_e(t, n):
#     for i in range(n):
#         t.fd(10)
#         t.lt(10)

# def print_flower():
#     polyline_d(flower, 10)
#     polyline_e(flower, 10) 

# print_flower()




# """Flores"""


 
# def polyline():
#      pass

# def arc():
#     pass

# def flor():
#     pass


# turtle.mainloop()   

# """CODIGO DO LIVRO"""

# """This module contains a code example related to

# Think Python, 2nd Edition
# by Allen Downey
# http://thinkpython2.com

# Copyright 2015 Allen Downey

# License: http://creativecommons.org/licenses/by/4.0/
# """

# from mypoligon import arc


# def petal(t, r, angle):
#     """Draws a petal using two arcs.

#     t: Turtle
#     r: radius of the arcs
#     angle: angle (degrees) that subtends the arcs
#     """
#     for i in range(2):
#         arc(t, r, angle)
#         t.lt(180-angle)


# def flower(t, n, r, angle):
#     """Draws a flower with n petals.

#     t: Turtle
#     n: number of petals
#     r: radius of the arcs
#     angle: angle (degrees) that subtends the arcs
#     """
#     for i in range(n):
#         petal(t, r, angle)
#         t.lt(360.0/n)


# def move(t, length):
#     """Move Turtle (t) forward (length) units without leaving a trail.
#     Leaves the pen down.
#     """
#     t.pu()
#     t.fd(length)
#     t.pd()


# bob = turtle.Turtle()

# # draw a sequence of three flowers, as shown in the book.
# move(bob, -100)
# flower(bob, 7, 60.0, 60.0)

# move(bob, 100)
# flower(bob, 10, 40.0, 80.0)

# move(bob, 100)
# flower(bob, 20, 140.0, 20.0)

# bob.hideturtle()
# turtle.mainloop()


"""SEGUNDO EXERCICIO"""

triang = turtle.Turtle()

def triangulo(t, n):
    for i in range(n):
        t.fd(60)
        t.lt(120)

# triangulo(triang, 3)

def pent():
    for i in range(5):
        triangulo(triang, 3)

pent()
turtle.mainloop()

