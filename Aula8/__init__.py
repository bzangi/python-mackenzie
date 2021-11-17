carros = []
consumo = []


def entrada_carro():
    i = 0
    while i < 4:
        carro = input()
        carros.append(carro)
        i = i + 1


def entrada_consumo():
    for i in range(4):
        cons = int(input())
        consumo.append(cons)


def economico():
    carro_menor = 0
    carro_menor_consumo = 0
    for i in range(4):
        if i == 0:
            carro_menor = consumo[i]
            carro_menor_consumo = i
        else:
            if consumo[i] < carro_menor:
                carro_menor = consumo[i]
                carro_menor_consumo = i
    return carros[carro_menor_consumo]

def main():
    entrada_carro()
    entrada_consumo()
    print(economico())

main()