decrescente = True
anterior = int(input("Digite o primeiro número da sequencia: "))

valor = 1

while valor != 0 and decrescente:
    valor = int(input("Digite um número da sequencia: "))
    if valor > anterior:
        decrescente = False
    anterior = valor


if decrescente == True:
    print(" A sequencia é decrescente")
else:
    print(" A sequencia não é decrescente")
