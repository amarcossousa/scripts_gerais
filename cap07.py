# Exercico 01
import math

def mysqrt(a, x):
    while True:
        print(x)
        y = (x + a/x)/2
        if y == x:
            break
        x = y
    return y

def square_math(a, x):
    while True:
        print(x,)
        y = math.sqrt(a)
        if y == x:
            break
        x = y
    return y

def teste_square_root(a, b):
    if a == mysqrt:
        return mysqrt 
    if b == square_math:
        return square_math
    return a, b




