
import math


# # #Valores de retorno

# """
# def area(radius): #codigo geral
#     a = math.pi * radius**2
#     return a
# """

# def area(radius):# codigo simplificado
#     return math.pi * radius**2


# # def absolute_value(x): #executa apenas uma função por conta da condicional
# #     if x < 0:
# #         return -x
# #     else:
# #         return x

# # def absolute_value(x): #atinge as duas condicinal 
# #     if x < 0:
# #         return -x
# #     if x > 0:
# #         return x

# def distance(x1, y1, x2, y2):
#     dx = x2 - x1
#     dy = y2 - y1
#     dsquared = dx**2 + dy**2
#     result = math.sqrt(dsquared)
#     return result

# """
# def circle_area(xc, yc, xp, yp): #codigo normal
#     radius = distance(xc, yc, xp, yp)
#     result = area(radius)
#     return result
# """

# def circle_area(xc, yc, xp, yp):# mesmo codigo, mais conciso
#     return area(distance(xc, yc, xp, yp))





#FUNCÇÕES BOLEANAS

# def is_divisible(x, y): # Codigo normal
#     if x % y == 0:
#         return True
#     else:
#         return False

# def is_divisible (x, y):# Mesmo codigo, mais conciso
#     return x % y == 0

# print(is_divisible(6, 8))

# def is_between (x, y, z): # Codigo normal
#     if x <= y <= z:
#         return False
#     else:
#         return True

# def is_between(x, y, z): # Codigo mais conciso
#     return x <= y <= z 

# def factorial (n):
#     if n == 0:
#         return 1
#     else:
#         recurse = factorial(n-1)
#         result = n * recurse
#         return result

# # print(factorial(4))
# def fibonacci (n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
#DEPURAÇÃO
# #corrigindo factorial para corrigir recursividade infinita com numeros  tipo float
# def factorial (n):
#     if not isinstance(n, int):
#         print('Factorial is only defined for integers.')
#         return None
#     elif n < 0:
#         print('factorial is not defined for negative integers.')
#         return None
#     elif n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

#EXERCÍCIOS
#Desenhar diagrama da pilha do seguinte codigo:
# def b(z):
#     prod = a(z, z)
#     print(z, prod)
#     return prod

# def a(x, y):
#     x = x + 1
#     return x * y

# def c(x, y, z):
#     total = x + y + z
#     square = b(total)**2
#     return square

# x = 1
# y = x + 1
# print(c(x, y+3, x+y))

def distance(x1, y1, x2, y2):
    return x1 + y1 / x2 - y2








