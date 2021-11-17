def atualiza_preco(valor) :
    valor = valor * 1.1
    return  valor

def taxa(valor):
    return valor * 0.025

def main():
    valor = float(input())
    precoAtt = atualiza_preco(valor)
    print(f'{precoAtt:.2f}')
    print(f'{taxa(precoAtt):.2f}')
    
main()