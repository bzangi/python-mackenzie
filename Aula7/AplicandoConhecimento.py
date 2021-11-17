def valorPagamento(valPrestacao,dias):
    if dias == 0:
        return valPrestacao
    elif dias > 0:
        valMulta = (valPrestacao*1.03)+(valPrestacao*0.1*dias/100)
        return valMulta
    else:
        print('insira um valor válido de dias')

def main():
    valPrestacao = float(input())
    dias = int(input())
    print(valorPagamento(valPrestacao, dias))

main()