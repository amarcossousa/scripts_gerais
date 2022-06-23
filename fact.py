nfact = int(input("Digite um valor para fatorial: "))
fact = 1
x = 1

if nfact == 0:
    fact = 1
    print(f'O valor fatorial de {nfact} é: ', fact)
else:
    while x <= nfact:
        fact *= x
        x += 1
    print(f'O valor fatorial de {nfact} é: ', fact) 