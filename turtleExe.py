import turtle
import math

def square(t, length):
    """Desenha um quadrado com lados do comprimento dado.
    Retorna a tartaruga para a posição inicial e localização.
    """
    for i in range(4):
        t.fd(length)
        t.lt(90)


def polyline(t, n, length, angle):
    """Desenha n segmentos de linha.
    t: objeto tartaruga
    n: número de segmentos de linha
    comprimento: comprimento de cada segmento
    ângulo: graus entre segmentos
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def polygon(t, n, length):
    """Desenha um polígono com n lados.
    t: Tartaruga
    n: número de lados
    comprimento: comprimento de cada lado.
    """
    angle = 360.0/n
    polyline(t, n, length, angle)


def arc(t, r, angle):
    """Desenha um arco com o raio e ângulo fornecidos.
    t: Tartaruga
    r: raio
    ângulo: ângulo subtendido pelo arco, em graus
    """ 
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n

    # fazer uma pequena curva à esquerda antes de começar reduz
    # o erro causado pela aproximação linear do arco
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)


def circle(t, r):
    """Desenha um círculo com o raio dado.
    t: Tartaruga
    r: raio
    """
    arc(t, r, 360)


# a condição a seguir verifica se estamos
# executando como um script, nesse caso execute o código de teste,
# ou sendo importado, nesse caso não.

if __name__ == '__main__':
    bob = turtle.Turtle()

    # desenha um círculo centrado na origem
    radius = 100
    bob.pu()
    bob.fd(radius)
    bob.lt(90)
    bob.pd()
    circle(bob, radius)

    # espera o usuário fechar a janela
    turtle.mainloop()