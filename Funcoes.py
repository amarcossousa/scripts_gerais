# #valores de retorno 
# import math 

# def area(radius):
#     a = math.pi * radius**2
#     return a

# def compare(x, y):
#     if x > y:
#         return 1
#     if x==y:
#         return 0
#     if x < y:
#         return -1

"""CAPITULO 3"""

#DESENVLVIMENTO INCREMENTAL
#Exercico 3.1
#Printa monty na linha 70
# def rigth_justify(s):
#     string = "monty"
#     return string

# result = rigth_justify(s=0)
# espaço = "                                                                      "
# # print(result.rjust(70))
# # print(len(result))  #solução 2 do youtube
# print(espaço, result)


# #Exercicio 3.2 minha solução
# def do_twice(f, g):
#     f()
#     g()
# def print_spam():
#     print('spam')

# #do_twice(print_spam, print_spam)

# def print_twice(spam):
#     return do_twice
# print(do_twice)

# # Exercicio 3.2 solução do livro

# def do_twice(func, arg):
#     """Executa uma função duas vezes.
    
#     func: objeto da função
#     arg: argumento passado para a função
#     """
#     func(arg)
#     func(arg)


# def print_twice(arg):
#     """Imprime o argumento duas vezes. 
#     arg: qualquer coisa imprimível
#     """
#     print(arg)
#     print(arg)

# def do_four(func, arg):
#     """Executa uma função quatro vezes.

#     func: objeto de função
#     arg: argumento passado para a função
#     """
#     do_twice(func, arg)
#     do_twice(func, arg)

# do_twice(print, 'spam')
# print('')

# do_four(print, 'spam')

# def print_beam():
#     print('+ - - - -', end=' ')

# def print_trace():
#     print('|', '        |')

# def mass():
#     print('+')


# def four_trace():
#     print_trace()
#     print_trace()
#     print_trace()
#     print_trace()

# def grade(): 
#     print_beam()
#     mass()
#     four_trace()

# def grade_final():
#     print_beam()
#     mass()



# def print_grade():
#     grade()
#     grade()
#     grade_final()

# print_grade()


# """CAPITULO 4"""

# import turtle

# bob = turtle.Turtle()

# turtle.mainloop()























    