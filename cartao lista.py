meuCartão = int(input("Digite o numero do seu cartão: "))

cartãoLido = 1
encontreiMeuCartãoNaLista = False

while cartãoLido != 0 and not encontreiMeuCartãoNaLista:
    cartãoLido = int(input("Digite o numero do seu cartão: "))
    if cartãoLido == meuCartão:
        encontreiMeuCartãoNaLista = True

if encontreiMeuCartãoNaLista:
    print("Meu cartão está na lista")
else:
    print("Meu cartão nem tá lá")
