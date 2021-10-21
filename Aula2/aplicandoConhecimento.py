from math import ceil
print("insira o custo do espetáculo e, em seguida, o preço do convite")
custo=float(input("custo do espetáculo = "))
convite=float(input("preço do convite = "))
precoMedio=custo/convite
print("A quantidade de convites vendidos para alcançar o custo deve ser de ", ceil(precoMedio))
print("para lucrar 23% devem ser vendidos ", ceil(precoMedio*1.23))