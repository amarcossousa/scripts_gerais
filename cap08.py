#FUNÇÃO DO LIVRO
# Travessia com loop while

fruit = 'banana'
index = 0
while index < len(fruit): # O loop exibe cada letra sozinha
    letter = fruit[index] 
    print(letter)
    index = index +1


# Codigo proprio, exercio proposto

"""" 
A função deve receber uma strig como argumento
e exibe as letras de tras para frente
"""

# def exibe_letras(a):
#     for letter in a:
#         letter += 1
#         return letter