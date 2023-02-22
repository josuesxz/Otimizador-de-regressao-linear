import variaveis_00

while True:
    print(" ")
    print("--------- Menu de funcao -------------")
    print("M - Media dos valores")
    print("V - Valor e sua incerteza")
    print("R - Equacao de regressao")
    print("X - Mudar os dados")
    print("S - Sair")
    print(" ")

    q = str(input("Qual a opcção: ")).upper()

    if q == "M": variaveis_00.media()

    if q == "V": variaveis_00.valor_incerteza()

    if q == "R": variaveis_00.correlacao_regressao()

    print(" ")
    if q == "S": break