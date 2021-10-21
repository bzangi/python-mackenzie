print('Selecione uma opção do menu')
print('1. Somar dois números')
print('2. Número ao cubo')
opcao=input()
if opcao == '1':
print('insira os números a serem somados')
n1=float(input())
n2=float(input())
n3=n1+n2
print('a soma é igual a ', n3)
elif opcao =='2':
print('insira o número a ser elevado ao cubo ')
n1=float(input())
n3=n1*n1*n1
print('%.1f elevado ao cubo é igual a' %n1, n3)
else:
print('OPÇÃO INVÁLIDA')