"""
condicionais e recursividade
"""

# Teorema de Fermat

# a**n + b**n = c**n
# se o valor de 'n' for maior que. 

from tkinter import mainloop


def check_fermat(a, b,  c, n):
    check_f = a**n + b**n == c**n
    if check_f == True:
        print('Holy Smokes, Fermat was wrong! ')
    else:
        print("No, that doesn't work. ")


